# 🕳️ Pothole Detection with YOLOv11

A YOLOv11-based object detection project for identifying **potholes** in road images, integrated with **Ultralytics**, **Roboflow**, and annotated datasets.

---

## 🧠 Overview

This project trains and evaluates a YOLOv11 model on a custom dataset of potholes. It uses Roboflow for dataset preparation and the Ultralytics YOLOv8 (YOLOv11-compatible) pipeline for training and inference.

---

## 📁 Project Structure

```
potholes_detection_yolov11/
├── dataset/
│ ├── train/
│ ├── valid/
│ ├── test/
│ ├── data.yaml
├── runs/
│ └── detect/
│     └── train11/
│         └── weights/
│             └── best.pt
│     └── train15/
│         └── weights/
│             └── best.pt
├── medium_inference.py
├── large_inference.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧪 Key Features

- ✅ Single-class object detection (Pothole)
- 📦 Dataset labeled and exported via **Roboflow** in YOLO format
- 🧠 Custom training using **Ultralytics YOLO**
- 📈 Real-time inference support on images, folders, and videos
- 💾 Save and visualize predictions programmatically (no cv2 needed)

---

## 🛠 Installation

### 1. Clone the Repository

```
git clone https://github.com/MarwanAbdellah/Potholes_detection_YOLOv11.git
cd Potholes_detection_YOLOv11
```

### 2. Create and Activate a Virtual Environment

```
python -m venv venv
```

- **Windows**: `venv\Scripts\activate`  
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Requirements

```
pip install -r requirements.txt
```

---

## 🚀 Running Inference

```
from ultralytics import YOLO
from PIL import Image

# Load trained model
model = YOLO("runs/detect/train11/weights/best.pt")

# Run inference
results = model("path/to/image.jpg")

# Show annotated results
img = Image.fromarray(results[0].plot())
img.show()

# Optionally save
img.save("predicted.jpg")
```

---

## 📊 Dataset Source

Dataset hosted via **Roboflow**:

**URL:** `https://universe.roboflow.com/marwanabdellah/potholes-detection-yolov11`

Class annotations:

| Class     | Description                            |
|-----------|----------------------------------------|
| `pothole` | Detected road surface damage or pothole |

---

## 📦 Requirements

```
ultralytics
roboflow
pillow
matplotlib
```

Install using:

```
pip install -r requirements.txt
```

---

## 📌 .gitignore Suggestions

```
__pycache__/
.venv/
*.pt
runs/
*.jpg
*.log
```

---

## 📬 Contact

**Marwan Abdellah**  
📧 [marawan.abdellah0@gmail.com](mailto:marawan.abdellah0@gmail.com)  
🔗 GitHub: [@MarwanAbdellah](https://github.com/MarwanAbdellah)
```
