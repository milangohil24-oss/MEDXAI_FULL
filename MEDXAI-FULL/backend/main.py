
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import shutil
import os
import uuid

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from database import Base, engine, get_db
from models import User
from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from services.prediction import predict_image, model
from services.gradcam import (
    make_gradcam_heatmap,
    create_gradcam_overlay
)


app = FastAPI(
    title="MedXAI API",
    description="Explainable AI Alzheimer's Disease Detection API",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


app.mount(
    "/uploads",
    StaticFiles(directory=UPLOAD_DIR),
    name="uploads"
)


@app.get("/")
def home():

    return {
        "message": "MedXAI API is running",
        "status": "success"
    }


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # --------------------------------
    # Generate unique filename
    # --------------------------------

    file_id = str(
        uuid.uuid4()
    )

    filename = (
        file_id +
        "_" +
        file.filename
    )

    image_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    # --------------------------------
    # Save uploaded image
    # --------------------------------

    with open(
        image_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # --------------------------------
    # Prediction
    # --------------------------------

    result = predict_image(
        image_path
    )

    # --------------------------------
    # Grad-CAM
    # --------------------------------

    heatmap, original_image, predicted_index, predictions = (
        make_gradcam_heatmap(
            image_path,
            model,
            pred_index=None
        )
    )

    # --------------------------------
    # Create overlay
    # --------------------------------

    overlay = create_gradcam_overlay(
        original_image,
        heatmap
    )

    # --------------------------------
    # Save Grad-CAM image
    # --------------------------------

    gradcam_filename = (
        "gradcam_" +
        filename
    )

    gradcam_path = os.path.join(
        UPLOAD_DIR,
        gradcam_filename
    )

    from PIL import Image

    Image.fromarray(
        overlay
    ).save(
        gradcam_path
    )

    # --------------------------------
    # Return response
    # --------------------------------

    return {

        "filename": file.filename,

        "prediction": result[
            "prediction"
        ],

        "confidence": result[
            "confidence"
        ],

        "confidence_percentage": result[
            "confidence_percentage"
        ],

        "probabilities": result[
            "probabilities"
        ],

        "gradcam_url":
            "/uploads/" +
            gradcam_filename
    }
class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@app.post("/auth/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        name=request.name,
        email=request.email,
        password_hash=hash_password(
            request.password
        )
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }


@app.post("/auth/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        request.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    auto_error=True
)


@app.get("/auth/me")
def get_me(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    from jose import JWTError, jwt

    try:
        payload = jwt.decode(
            token,
            "MEDXAI_SUPER_SECRET_KEY_CHANGE_THIS",
            algorithms=["HS256"]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }