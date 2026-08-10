from services.prediction import predict_image

image_path = input("Enter MRI image path: ")

result = predict_image(image_path)

print("\nPrediction:", result["prediction"])
print(
    "Confidence:",
    str(result["confidence_percentage"]) + "%"
)

print("\nClass Probabilities:")

for class_name, probability in result["probabilities"].items():
    print(
        class_name,
        ":",
        f"{probability * 100:.2f}%"
    )