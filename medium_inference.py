from PIL import Image

from ultralytics import YOLO

def medium_inference(img_path: str):
    # Loading the weights for the YOLO model
    model = YOLO("runs/detect/train11/weights/best.pt")

    # Run inference
    results = model(img_path)

    # Visualize the results
    for i, r in enumerate(results):
        # Plot results image
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

        return im_rgb

if __name__ == "__main__":
    medium_inference(r"potholes-detect-1\valid\images\64_jpg.rf.f3d271c6ca9f5a631e2b721040becdb5.jpg")