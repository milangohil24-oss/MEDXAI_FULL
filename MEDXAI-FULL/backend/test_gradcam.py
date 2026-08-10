import tensorflow as tf
import matplotlib.pyplot as plt

from services.gradcam import (
    make_gradcam_heatmap,
    create_gradcam_overlay
)


MODEL_PATH = "model/alzheimer_efficientnetb0.keras"
IMAGE_PATH = "test.jpeg"

CLASS_NAMES = [
    "MildDemented",
    "ModerateDemented",
    "NonDemented",
    "VeryMildDemented"
]


print("Loading model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


# Generate Grad-CAM
heatmap, original_image, predicted_index, predictions = (
    make_gradcam_heatmap(
        IMAGE_PATH,
        model
    )
)


predicted_class = CLASS_NAMES[
    predicted_index
]

confidence = float(
    predictions[predicted_index]
)


print()
print("Prediction:", predicted_class)
print(
    "Confidence:",
    round(confidence * 100, 2),
    "%"
)

print()
print("Generating Grad-CAM overlay...")


overlay = create_gradcam_overlay(
    original_image,
    heatmap
)


print("Grad-CAM generated successfully.")


# Display results
plt.figure(figsize=(14, 5))


plt.subplot(1, 3, 1)

plt.imshow(
    original_image
)

plt.title(
    "Original MRI"
)

plt.axis("off")


plt.subplot(1, 3, 2)

plt.imshow(
    heatmap,
    cmap="jet"
)

plt.title(
    "Grad-CAM Heatmap"
)

plt.axis("off")


plt.subplot(1, 3, 3)

plt.imshow(
    overlay
)

plt.title(
    "Grad-CAM Overlay"
)

plt.axis("off")


plt.tight_layout()

plt.show()