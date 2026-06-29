# Indian License Plate Detection Model Training and TensorFlow Lite Conversion

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-111111?style=for-the-badge)]
[![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-FF6F00?style=for-the-badge\&logo=tensorflow\&logoColor=white)](https://www.tensorflow.org/lite)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-5A3FFF?style=for-the-badge)]
[![Roboflow](https://img.shields.io/badge/Roboflow-6706CE?style=for-the-badge)]
[![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge\&logo=googlecolab\&logoColor=white)]

---

# Overview

This project focuses on training a custom **YOLOv8 object detection model** for detecting **Indian Vehicle License Plates** and converting the trained model into **TensorFlow Lite (.tflite)** format for lightweight deployment.

The entire training pipeline was implemented using **Google Colab GPU**, dataset management was handled using **Roboflow**, and final deployment optimization was performed using **TensorFlow Lite conversion**.

The exported model is designed for:

* Raspberry Pi Deployment
* Edge AI Applications
* Real-Time Inference
* CPU-Only Execution

---

# Features

✔ Custom YOLOv8 Training
✔ Indian License Plate Dataset
✔ Roboflow Dataset Integration
✔ GPU Accelerated Training
✔ TensorFlow Lite Export
✔ Model Evaluation
✔ Automatic Metric Generation
✔ Lightweight Deployment
✔ Edge AI Optimization

---

# Dataset

Dataset Source:

* Roboflow

Dataset Type:

* Object Detection

Target Class:

```text
License Plate
```

Dataset Preparation Included:

* Annotation
* Train / Validation / Test Split
* YOLOv8 Label Conversion

---

# Training Pipeline

```text
Roboflow Dataset
        ↓
Dataset Download
        ↓
YOLOv8 Training
        ↓
Validation
        ↓
Performance Evaluation
        ↓
Best Weight Selection
        ↓
TensorFlow Lite Conversion
        ↓
Deployment
```

---

# Technologies Used

* Python
* YOLOv8
* Ultralytics
* Roboflow
* TensorFlow
* TensorFlow Lite
* PyTorch
* Google Colab

---

# Project Workflow

## Phase 1 — Dataset Acquisition

Download dataset from Roboflow.

Output:

```text
Indian-License-Plate-1/
```

---

## Phase 2 — GPU Environment Setup

Verify GPU availability.

Outputs:

* CUDA Status
* GPU Name

Example:

```text
GPU available: True
GPU name: Tesla T4
```

---

## Phase 3 — YOLOv8 Training

Load pretrained model.

```python
model = YOLO("yolov8n.pt")
```

Train model.

Parameters:

* Epochs → 50
* Image Size → 640
* Batch Size → 16
* Early Stopping → 10

Output:

```text
runs/detect/license_plate_detector/
```

Generated:

* best.pt
* last.pt
* results.png

---

## Phase 4 — Model Evaluation

Evaluate:

* Train
* Validation
* Test

Metrics:

* mAP@50
* mAP@50–95
* Precision
* Recall

Output:

```text
Evaluation Scores
```

---

## Phase 5 — TensorFlow Lite Conversion

Load trained model.

```python
trained_model = YOLO("best.pt")
```

Convert:

```python
trained_model.export(
    format="tflite",
    imgsz=640
)
```

Output:

```text
best_saved_model/
best_float32.tflite
```

---

# Folder Structure

```text
LicensePlateModelTraining/
│
├── License Plate Recognition.ipynb
├── License Plate TFLite Conversion.ipynb
│
├── dataset/
│   └── Indian-License-Plate-1/
│
├── runs/
│   └── detect/
│
├── models/
│   ├── best.pt
│   └── best_float32.tflite
│
├── assets/
│
└── README.md
```

---

# Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/license-plate-model-training.git
```

Install dependencies

```bash
pip install ultralytics
pip install tensorflow
pip install roboflow
pip install torch
```

---

# Running Training

Run notebook:

```text
License Plate Recognition.ipynb
```

Train:

```python
model.train(
epochs=50,
imgsz=640,
batch=16
)
```

---

# Export TensorFlow Lite

Run:

```text
License Plate TFLite Conversion.ipynb
```

Output:

```text
best_float32.tflite
```

---

# Outputs

Generated Files:

```text
best.pt
best_float32.tflite
results.png
```

---

# Concepts Used

* Object Detection
* Transfer Learning
* Bounding Box Regression
* TensorFlow Lite Optimization
* Edge AI
* Model Export
* Evaluation Metrics

---

# Applications

* Smart Parking
* Toll Systems
* Vehicle Analytics
* Automatic Entry Systems
* Traffic Monitoring

---

# Future Improvements

* Larger Dataset
* Quantized TFLite Models
* YOLOv11 Migration
* Edge TPU Deployment
* Multi-Country License Plates

---

# Author

Abhivridh

B.Tech Computer Science Engineering

College of Engineering Trivandrum

⭐ Star this repository if you found it useful.
