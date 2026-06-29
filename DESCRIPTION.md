# Environment Setup and Dependency Installation

This document contains the exact environment configuration and installation steps used for this project.

---

# Hardware

Device:
Raspberry Pi 4 (64-bit)

Camera:
Raspberry Pi Camera Module

OS:
Raspberry Pi OS (64-bit)

---

# Python Environment

Python Version:

```text
Python 3.13
```

Create environment:

```bash
python -m venv cv_env
```

Activate:

```bash
source cv_env/bin/activate
```

Deactivate:

```bash
deactivate
```

---

# System Package Installation

Update packages:

```bash
sudo apt update
```

Install Camera Library:

```bash
sudo apt install python3-picamera2 -y
```

---

# Python Dependency Installation

Install dependencies:

```bash
pip install \
numpy==2.3.5 \
opencv-python==4.10.0.84 \
tensorflow==2.20.0 \
paddlepaddle==3.2.0 \
paddleocr==3.2.0
```

Verify installation:

```bash
python -c "import tensorflow"
```

```bash
python -c "from paddleocr import PaddleOCR"
```

```bash
python -c "from picamera2 import Picamera2"
```

---

# Runtime Stability Configuration

To avoid segmentation faults while running PaddleOCR and TensorFlow together:

```python
import os

os.environ["OMP_NUM_THREADS"]="1"
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["MKL_NUM_THREADS"]="1"

os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"
```

Initialize OCR:

```python
ocr=PaddleOCR(
lang='en',
use_doc_orientation_classify=False,
use_doc_unwarping=False,
use_textline_orientation=False,
cpu_threads=1
)
```

Initialize TFLite:

```python
tf.lite.Interpreter(
model_path=model_path,
num_threads=1
)
```

---

# Execution

Run:

```bash
python main.py
```

Quit:

```text
Press Q
```

---

# Notes

- Entire pipeline runs on CPU
- GPU is disabled
- PaddleOCR medium English model used
- TensorFlow Lite XNNPACK enabled
- Thread count limited for stability
- Designed for Raspberry Pi deployment
