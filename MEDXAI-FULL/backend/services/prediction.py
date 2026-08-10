import tensorflow as tf
import numpy as np
import json
from PIL import Image

MODEL_PATH = "model/alzheimer_efficientnetb0.keras"
CLASS_NAMES_PATH = "model/class_names.json"

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)

IMG_SIZE = (224, 224)


def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = np.array(image).astype(np.float32)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    predictions = model.predict(
        image_array,
        verbose=0
    )[0]

    predicted_index = int(
        np.argmax(predictions)
    )

    predicted_class = class_names[
        predicted_index
    ]

    confidence = float(
        predictions[predicted_index]
    )

    probabilities = {
        class_names[i]: float(predictions[i])
        for i in range(len(class_names))
    }

    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "confidence_percentage": round(
            confidence * 100,
            2
        ),
        "probabilities": probabilities
    }