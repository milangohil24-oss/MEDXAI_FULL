import tensorflow as tf
import numpy as np
import cv2
from PIL import Image


IMG_SIZE = (224, 224)


def get_efficientnet_base(model):

    for layer in model.layers:

        if isinstance(layer, tf.keras.Model):

            if "efficientnet" in layer.name.lower():
                return layer

    for layer in model.layers:

        if isinstance(layer, tf.keras.Model):
            return layer

    raise ValueError("EfficientNet base model not found.")


def get_last_conv_layer(base_model):

    for layer in reversed(base_model.layers):

        try:

            shape = layer.output.shape

            if len(shape) == 4:
                return layer

        except Exception:
            continue

    raise ValueError(
        "No suitable convolutional layer found."
    )


def make_gradcam_heatmap(
    image_path,
    model,
    pred_index=None
):

    # ============================
    # LOAD IMAGE
    # ============================

    image = Image.open(
        image_path
    ).convert("RGB")

    original_image = np.array(image)

    resized = image.resize(
        IMG_SIZE
    )

    img_array = np.array(
        resized
    ).astype(
        np.float32
    )

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # ============================
    # FIND EFFICIENTNET
    # ============================

    base_model = get_efficientnet_base(
        model
    )

    # ============================
    # FIND LAST CONVOLUTION
    # ============================

    target_layer = get_last_conv_layer(
        base_model
    )

    print(
        "Grad-CAM layer:",
        target_layer.name
    )

    # ============================
    # IMPORTANT:
    # GET TARGET ACTIVATION AND
    # BASE OUTPUT FROM SAME GRAPH
    # ============================

    grad_model = tf.keras.Model(
        inputs=base_model.input,
        outputs=[
            target_layer.output,
            base_model.output
        ]
    )

    # ============================
    # GRADIENT TAPE
    # ============================

    with tf.GradientTape() as tape:

        conv_outputs, base_output = grad_model(
            img_array,
            training=False
        )

        # ============================
        # RUN REMAINING CLASSIFIER
        # ============================

        x = base_output

        base_position = model.layers.index(
            base_model
        )

        classifier_layers = model.layers[
            base_position + 1:
        ]

        for layer in classifier_layers:

            try:
                x = layer(
                    x,
                    training=False
                )

            except TypeError:
                x = layer(x)

        predictions = x

        if pred_index is None:

            pred_index = tf.argmax(
                predictions[0]
            )

        class_output = predictions[
            0,
            pred_index
        ]

    # ============================
    # CALCULATE GRADIENTS
    # ============================

    grads = tape.gradient(
        class_output,
        conv_outputs
    )

    if grads is None:

        raise ValueError(
            "Gradients are still None. "
            "The target layer is not connected "
            "to the prediction graph."
        )

    # ============================
    # GLOBAL AVERAGE POOLING
    # ============================

    pooled_grads = tf.reduce_mean(
        grads,
        axis=(1, 2)
    )

    # Remove batch dimension
    conv_outputs = conv_outputs[0]

    pooled_grads = pooled_grads[0]

    # ============================
    # WEIGHT FEATURE MAPS
    # ============================

    heatmap = tf.reduce_sum(
        conv_outputs * pooled_grads,
        axis=-1
    )

    # ============================
    # RELU
    # ============================

    heatmap = tf.maximum(
        heatmap,
        0
    )

    # ============================
    # NORMALIZE
    # ============================

    max_value = tf.reduce_max(
        heatmap
    )

    heatmap = tf.where(
        max_value > 0,
        heatmap / max_value,
        heatmap
    )

    heatmap = heatmap.numpy()

    return (
        heatmap,
        original_image,
        int(pred_index),
        predictions.numpy()[0]
    )


def create_gradcam_overlay(
    original_image,
    heatmap,
    alpha=0.40
):

    original_image = np.asarray(
        original_image
    )

    # ============================
    # CONVERT IMAGE
    # ============================

    if original_image.dtype != np.uint8:

        if original_image.max() <= 1.0:

            original_image = (
                original_image * 255
            ).astype(
                np.uint8
            )

        else:

            original_image = np.clip(
                original_image,
                0,
                255
            ).astype(
                np.uint8
            )

    # ============================
    # RESIZE HEATMAP
    # ============================

    heatmap = cv2.resize(
        heatmap,
        (
            original_image.shape[1],
            original_image.shape[0]
        )
    )

    # ============================
    # CONVERT HEATMAP
    # ============================

    heatmap_uint8 = np.uint8(
        255 * heatmap
    )

    heatmap_color = cv2.applyColorMap(
        heatmap_uint8,
        cv2.COLORMAP_JET
    )

    heatmap_color = cv2.cvtColor(
        heatmap_color,
        cv2.COLOR_BGR2RGB
    )

    # ============================
    # OVERLAY
    # ============================

    overlay = cv2.addWeighted(
        original_image,
        1 - alpha,
        heatmap_color,
        alpha,
        0
    )

    return overlay