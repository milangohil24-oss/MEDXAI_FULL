import tensorflow as tf
import json

MODEL_PATH = "model/alzheimer_efficientnetb0.keras"
CLASS_NAMES_PATH = "model/class_names.json"

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)

with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)

print("Classes:", class_names)