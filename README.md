# Real-Time License Plate Detection and OCR using TensorFlow Lite, PaddleOCR, and Raspberry Pi

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-111111?style=for-the-badge)]
[![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-FF6F00?style=for-the-badge\&logo=tensorflow\&logoColor=white)](https://www.tensorflow.org/lite)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)](https://opencv.org/)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-0052CC?style=for-the-badge)](https://github.com/PaddlePaddle/PaddleOCR)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)](https://numpy.org/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=for-the-badge\&logo=raspberrypi\&logoColor=white)](https://www.raspberrypi.com/)

---

# Overview

A real-time License Plate Detection and Recognition system built using:

* YOLOv8
* TensorFlow Lite
* PaddleOCR
* OpenCV
* Raspberry Pi Camera
* Computer Vision

This project trains a **custom YOLOv8 model on Indian License Plate datasets** and converts the trained model into **TensorFlow Lite (.tflite)** format for lightweight CPU inference.

The deployed system captures frames using Raspberry Pi Camera, detects vehicle license plates, performs perspective correction, and extracts text using PaddleOCR.

The complete pipeline is optimized for **Raspberry Pi 4 (64-bit)** and edge AI deployment.

<table>
<tr>
<td align="center">
<img src="assets/raspberry_pi_4.jpg" width="450" height="600">
</td>

<td align="center">
<img src="assets/multiple_car_detection.png" width="450">
</td>
</tr>
</table>

<p align="center">
Live deployment on Raspberry Pi 4
</p>
---

# Features

✔ Custom YOLOv8 Training on Indian License Plate Dataset

✔ TensorFlow Lite Conversion

✔ Real-Time License Plate Detection

✔ PaddleOCR Text Recognition

✔ Perspective Transformation

✔ License Plate Rectification

✔ OCR Text Extraction

✔ Confidence Filtering

✔ Non-Maximum Suppression (NMS)

✔ Raspberry Pi Camera Integration

✔ CPU Optimized Execution

✔ Lightweight Edge Deployment

---

# Folder Structure

```text
RaspberryPi-LicensePlate-Recognition/
│
├── assets/
│   ├── model_training_results.png
│   ├── multiple_car_detection.png
│   ├── raspberry_pi_4.jfif
│   ├── raspberry_pi_4.jpg
│   └── raspberry_pi_detection.jpg
│
├── model_training/
│    ├── models/
│           ├── best_float32.tflite
│           └── best.pt
│    ├── License_Plate_Recognition.ipynb
│    ├── License_Plate_Recognition.py
│    ├── License_Plate_TFLite_Conversion.ipynb
│    └── License_Plate_TFLite_Conversion.
│
├── models/
│   └── best_float32.tflite
│
├── outputs/
│   ├── frames/
│   ├── video_reader.py
│   ├── video_merger.py
│   ├── original.mp4
│   ├── output.mp4
│   └── README.md
│
├── src/
│   └── main.py
│
├── requirements.txt
├── description.md
└── README.md
```

---

# System Architecture

```text
Raspberry Pi Camera
        ↓
Frame Capture
        ↓
Preprocessing
        ↓
YOLOv8 Detection
        ↓
TensorFlow Lite Inference
        ↓
Bounding Box Extraction
        ↓
NMS Filtering
        ↓
Perspective Transform
        ↓
PaddleOCR
        ↓
License Plate Text
        ↓
Visualization
```

---

# Technologies Used

* Python
* YOLOv8
* TensorFlow Lite
* PaddleOCR
* PaddlePaddle
* OpenCV
* NumPy
* Raspberry Pi Camera (Picamera2)
* Edge AI

---

# Project Workflow

## Phase 1 — Dataset Preparation

Prepare Indian License Plate dataset.

Process:

* Annotation
* Label Formatting
* Dataset Split

Output:

* Training Dataset
* Validation Dataset

---

## Phase 2 — YOLOv8 Model Training

Train custom YOLOv8 model.

Outputs:

* License Plate Detection
* Bounding Box Regression
* Confidence Estimation

Output:

```text
best.pt
```

---

## Phase 3 — TensorFlow Lite Conversion

Convert trained YOLOv8 model into TensorFlow Lite.

Purpose:

* Faster Inference
* CPU Optimization
* Raspberry Pi Deployment

Output:

```text
best_float32.tflite
```

---

## Phase 4 — Live Camera Acquisition

Capture frames using Raspberry Pi Camera.

Output:

```text
RGB Frames
```

---

## Phase 5 — Detection

Run TensorFlow Lite inference.

Outputs:

* Center X
* Center Y
* Width
* Height
* Confidence

---

## Phase 6 — Post Processing

Apply:

* Confidence Threshold
* Bounding Box Conversion
* NMS

Result:

```text
Final Plate Regions
```

---

## Phase 7 — Perspective Correction

Apply:

* Contour Detection
* Rectangle Extraction
* Perspective Transform

Output:

```text
Straightened Plate
```

---

## Phase 8 — OCR

Run PaddleOCR.

Extract:

* Characters
* Numbers
* Full License Plate Text

---

## Phase 9 — Visualization

Display:

* Bounding Box
* Confidence Score
* OCR Output

---

# Project Outputs

## Raspberry Pi Deployment Setup

<table>
<tr>
<td align="center">
<img src="assets/raspberry_pi_4.jfif" width="450">
</td>

<td align="center">
<img src="assets/raspberry_pi_4.jpg" width="450">
</td>
</tr>
</table>

<p align="center">
Live deployment on Raspberry Pi 4
</p>

---

## Real-Time License Plate Detection

<table>
<tr>

<td align="center">
<img src="assets/multiple_car_detection.png" width="450">
<p>Linux / Windows Output</p>
</td>

<td align="center">
<img src="assets/raspberry_pi_detection.jpg" width="450">
<p>Raspberry Pi Output</p>
</td>

</tr>
</table>

<p align="center">
Detected plates with confidence score and OCR text
</p>

---

# Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/RaspberryPi-LicensePlate-Recognition.git
```

Create environment

```bash
python -m venv cv_env
```

Activate

Linux:

```bash
source cv_env/bin/activate
```

Windows:

```bash
cv_env\Scripts\activate
```

Install

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# Controls

| Key | Action |
| --- | ------ |
| Q   | Quit   |

---

# Concepts Used

* YOLOv8 Object Detection
* Transfer Learning
* TensorFlow Lite Optimization
* OCR
* Perspective Transform
* Non Maximum Suppression
* Computer Vision
* Edge AI

---

# Applications

* Smart Parking
* Vehicle Monitoring
* Toll Automation
* Vehicle Entry Systems
* Security Systems

---

# Future Improvements

* Multi-Line OCR
* Vehicle Tracking
* Database Integration
* Web Dashboard
* Coral Edge TPU
* Automatic Gate Systems

---

# Author

Abhivridh

B.Tech Computer Science Engineering

College of Engineering Trivandrum

⭐ Star this repository if you found it useful.
