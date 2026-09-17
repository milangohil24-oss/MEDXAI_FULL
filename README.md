# 🧠 MedXAI

### Explainable MRI Intelligence for AI-Assisted Medical Image Analysis

<p align="center">
  <img src="https://raw.githubusercontent.com/milangohil24-oss/MEDXAI_FULL/main/MEDXAI-FULL/medxai-home.png" alt="MedXAI Medical AI Platform" width="100%">
</p>

<p align="center">
  <b>AI-powered MRI image classification with Explainable AI (XAI)</b>
</p>

---

## 🚀 Live Demo

<p align="center">
  <a href="https://medxai-frontend.onrender.com">
    <b>🌐 Open MedXAI Live →</b>
  </a>
</p>

MedXAI is deployed as a web-based application for interacting with an AI-powered MRI image analysis system.

---

## 📌 About the Project

**MedXAI** is an AI-based medical image analysis project that combines **Deep Learning** with **Explainable AI (XAI)**.

The system uses a deep learning classification model to analyze MRI images and generate predictions. **Grad-CAM (Gradient-weighted Class Activation Mapping)** is used to provide a visual explanation of the model's prediction by highlighting important regions of the input image.

The project demonstrates how an AI model can be integrated into a complete web application using a **React frontend, Python backend, REST APIs, authentication, and Explainable AI techniques**.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **AI Classification** | Classifies MRI images using a deep learning model |
| 🔬 **EfficientNetB0** | Uses EfficientNetB0 for image classification |
| ⚡ **Transfer Learning** | Uses a pretrained deep learning architecture |
| 🔍 **Explainable AI** | Uses Grad-CAM to visualize model predictions |
| 🖼️ **MRI Image Upload** | Allows users to upload images for analysis |
| 🌐 **Web Application** | React-based interactive user interface |
| 🔗 **REST API** | Frontend communicates with backend through APIs |
| 🔐 **Authentication** | Provides user authentication functionality |
| 📊 **Prediction Results** | Displays AI prediction and visual explanation |

---

## 🧠 AI & Explainability

### Model Pipeline

```text
                    MRI Image
                        │
                        ▼
              Image Preprocessing
                        │
                        ▼
                 EfficientNetB0
                        │
                        ▼
                Model Prediction
                        │
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
            Prediction       Grad-CAM
                               │
                               ▼
                     Visual Explanation
                               │
                               ▼
                         Final Result
```

### 🔍 Explainable AI with Grad-CAM

**Grad-CAM** is used to make the deep learning prediction more interpretable.

It generates a heatmap that highlights image regions that contributed to the model's prediction. This provides a visual representation of the areas that were important to the model during classification.

MedXAI therefore combines:

- **Deep Learning** for image classification
- **Transfer Learning** for model development
- **Grad-CAM** for explainability
- **Web technologies** for application integration

---

## 🛠️ Technology Stack

### 🎨 Frontend

- React.js
- Vite
- JavaScript / TypeScript
- HTML5
- CSS3
- REST API Integration

### ⚙️ Backend

- Python
- FastAPI
- REST APIs
- Authentication
- Database Integration

### 🤖 AI / Machine Learning

- TensorFlow
- Keras
- EfficientNetB0
- Transfer Learning
- Deep Learning
- Grad-CAM

### ☁️ Deployment

- GitHub
- Render

---

## 📂 Project Structure

```text
MEDXAI_FULL/
│
├── MEDXAI-FULL/
│   │
│   ├── backend/
│   │   ├── model/
│   │   ├── services/
│   │   ├── uploads/
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── test.jpeg
│   │   ├── test_gradcam.py
│   │   ├── test_model.py
│   │   └── test_prediction.py
│   │
│   ├── frontend/
│   │   ├── src/
│   │   ├── .env.example
│   │   ├── index.html
│   │   ├── package.json
│   │   ├── package-lock.json
│   │   └── vite.config.ts
│   │
│   ├── medxai-home.png
│   ├── .gitignore
│   └── README.md
│
└── README.md
```

---

## ⚙️ How It Works

### 1. Upload MRI Image

The user uploads an MRI image through the MedXAI frontend.

### 2. Send Image to Backend

The frontend sends the uploaded image to the backend through a REST API.

### 3. Image Processing

The backend receives and processes the image before passing it to the trained model.

### 4. AI Prediction

The **EfficientNetB0** model analyzes the image and generates a classification prediction.

### 5. Generate Explanation

**Grad-CAM** generates a visual heatmap showing the regions that contributed to the model's prediction.

### 6. Display Results

The prediction and explanation are returned to the frontend and displayed to the user.

---

## 🔄 Application Architecture

```text
┌─────────────────────┐
│        User         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   React Frontend    │
│      + Vite         │
└──────────┬──────────┘
           │
        REST API
           │
           ▼
┌─────────────────────┐
│   FastAPI Backend   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ EfficientNetB0 Model│
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
Prediction    Grad-CAM
     │           │
     └─────┬─────┘
           ▼
┌─────────────────────┐
│   Final AI Result   │
└─────────────────────┘
```

---

## 💻 Local Setup

### 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd MEDXAI_FULL/MEDXAI-FULL
```

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Start the FastAPI backend using the project's configured entry point.

### 3️⃣ Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

---

## 🔐 Environment Variables

Create a `.env` file inside the frontend folder:

```text
frontend/.env
```

Add:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

An example configuration is provided in:

```text
frontend/.env.example
```

> ⚠️ **Security:** Never upload `.env` files containing private credentials, passwords, API keys, tokens, or other sensitive information to GitHub.

---

## 🌐 Application

### 🚀 Live Application

**[Open MedXAI Live →](https://medxai-frontend.onrender.com)**

The deployed application provides the MedXAI interface for interacting with the AI-powered MRI image analysis system.

---

## 🎯 Project Objectives

- Apply deep learning to MRI image classification.
- Implement Transfer Learning using EfficientNetB0.
- Implement Explainable AI using Grad-CAM.
- Build a complete AI-powered web application.
- Connect a machine learning model with a web interface.
- Implement frontend-backend communication using REST APIs.
- Provide visual explanations for AI predictions.
- Demonstrate practical integration of AI and web technologies.

---

## 🔮 Future Improvements

- Improve model performance using larger and more diverse datasets.
- Add support for additional medical image categories.
- Improve Grad-CAM visualization.
- Add model evaluation and performance dashboards.
- Improve application scalability.
- Strengthen authentication and application security.
- Add additional AI models for medical image analysis.
- Explore additional Explainable AI techniques.

---

## ⚠️ Disclaimer

**MedXAI is an academic and portfolio project intended for educational and demonstration purposes.**

The predictions generated by this system should **not** be considered a medical diagnosis and should not replace professional medical advice, clinical judgment, or evaluation by a qualified healthcare professional.

---

## 👨‍💻 Author

### Milan Gohil

**B.Tech — Artificial Intelligence & Data Science**

`Artificial Intelligence` • `Machine Learning` • `Deep Learning` • `Generative AI`

---

<p align="center">

⭐ <b>If you find this project interesting, consider giving the repository a star!</b>

<br><br>

<a href="https://medxai-frontend.onrender.com">
  <b>🚀 Try MedXAI Live</b>
</a>

</p>
