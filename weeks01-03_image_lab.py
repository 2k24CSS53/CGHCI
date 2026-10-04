import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def inspect_image(image_path: str) -> dict:
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    height, width, channels = img.shape
    pixel_count = width * height
    estimated_bytes = pixel_count * channels

    return {
        "width": width,
        "height": height,
        "channels": channels,
        "shape": [height, width, channels],
        "pixel_count": pixel_count,
        "estimated_bytes": estimated_bytes,
        "color_order": "BGR",
    }


def create_pixel_views(image_path: str, output_dir: str) -> dict:
    os.makedirs(output_dir, exist_ok=True)
    img_bgr = cv2.imread(image_path)

    b, g, r = cv2.split(img_bgr)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    downsampled = cv2.resize(gray, (w // 2, h // 2))

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(r, cmap="Reds")
    plt.title("Red")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(g, cmap="Greens")
    plt.title("Green")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(b, cmap="Blues")
    plt.title("Blue")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(downsampled, cmap="gray")
    plt.title("Downsampled")
    plt.axis("off")

    plt.tight_layout()
    output_path = os.path.join(output_dir, "pixel_views.png")
    plt.savefig(output_path)
    plt.close()

    return {"output": output_path}


def create_adjustments(image_path: str, output_dir: str) -> dict:
    os.makedirs(output_dir, exist_ok=True)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    brightness = cv2.convertScaleAbs(img, alpha=1, beta=50)
    contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(output_dir, "brightness.png"), brightness)
    cv2.imwrite(os.path.join(output_dir, "contrast.png"), contrast)
    cv2.imwrite(os.path.join(output_dir, "threshold.png"), thresh)

    return {"status": "adjustments done"}


def create_blur_and_edges(image_path: str, output_dir: str) -> dict:
    os.makedirs(output_dir, exist_ok=True)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.blur(gray, (5, 5))

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    sobel = cv2.magnitude(sobelx, sobely)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Gray")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(blurred, cmap="gray")
    plt.title("Blur")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(sobel, cmap="gray")
    plt.title("Edges")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "blur_edges.png"))
    plt.close()

    return {"status": "blur & edges done"}


def run_lab(image_path: str, output_dir: str):
    inspect_image(image_path)
    create_pixel_views(image_path, output_dir)
    create_adjustments(image_path, output_dir)
    create_blur_and_edges(image_path, output_dir)


def main():
    image_path = os.path.join("images", "original.jpg")
    output_dir = "outputs"

    run_lab(image_path, output_dir)
    print("Lab execution completed successfully.")


if __name__ == "__main__":
    main()