# 🕳️ Pothole Detection using YOLOv11

This project implements a custom YOLOv11 model to detect potholes in road images. It uses Ultralytics' YOLO training and inference pipelines along with a labeled dataset for accurate object detection in real-world conditions.

---

## 📁 Dataset Description

The dataset used in this project is hosted on **Roboflow**:

**Dataset URL:** `https://universe.roboflow.com/marwanabdellah/potholes-detection-yolov11`

It contains annotated images with the following class:

| Class     | Description                            |
|-----------|----------------------------------------|
| `pothole` | Labeled region representing a pothole  |

---

## 📊 Project Pipeline

### **1. Data Preparation**
- Dataset downloaded from Roboflow in YOLO format.
- Split into train/val/test.
- `data.yaml` configured with class info and paths.

### **2. Model Configuration**
- Used **Ultralytics YOLOv8 framework**.
- Initialized with pretrained weights (`yolov8m.pt`).
- Customized for single-class detection.

### **3. Training Process**
- Trained using:
  - `imgsz = 640`
  - `epochs = 50`
  - `batch = 16`
- Used `best.pt` from `runs/detect/train*/weights/`.

### **4. Inference**
- Loaded the trained model with:
  ```python
  model = YOLO("path/to/best.pt")
  ```
- Inferred on test images using:
  ```python
  results = model("path/to/image.jpg")
  ```

### **5. Visualization**
- Used `result.plot()` to overlay detections.
- Saved or displayed using PIL.

---

## 🚀 How to Run

### **Requirements**
- Python ≥ 3.10
- ultralytics
- roboflow
- pillow
- matplotlib

### **Install Requirements**
```bash
pip install ultralytics roboflow pillow matplotlib
```

### **Running the Script**
```python
from ultralytics import YOLO
model = YOLO("runs/detect/train/weights/best.pt")
results = model("test.jpg")
results[0].show()
```

