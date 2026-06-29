# Outputs

This folder contains utilities and generated outputs used for testing and evaluating the License Plate Recognition pipeline on prerecorded videos.

The pipeline processes an input video frame-by-frame, performs:

1. License Plate Detection (TensorFlow Lite)
2. Perspective Correction
3. Optical Character Recognition (PaddleOCR)
4. Bounding Box + Text Rendering
5. Frame Export
6. Video Reconstruction

---
## Images - Real-Time License Plate Detection and OCR

<table>
<tr>

<td align="center">
        <img src="../assets/multiple_car_detection.png" width="450">
        <p align=center>Output Processed in Linux/Windows Computer</p>
</td>

<td align="center">
        <img src="../assets/raspberry_pi_detection.jpg" width="450">
        <p align=center>Raspberry Pi 4 Output</p>
</td>

</tr>
</table>

<p align="center">
Detected license plate with confidence score and extracted OCR text
</p>

---

## Folder Structure

```text
outputs/
│
├── original.mp4
├── video_reader.py
├── video_merger.py
├── output.mp4
├── frames/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   ├── frame_0003.jpg
│   └── ...
│
└── README.md
```

---

## Files Description

### original.mp4

Input video used for testing.

The system reads this video frame-by-frame and performs license plate detection and OCR.

---

### video_reader.py

Processes the input video.

### Workflow

```text
Input Video
     ↓
Read Frame
     ↓
Resize + Normalize
     ↓
TensorFlow Lite Detection
     ↓
Perspective Transform
     ↓
PaddleOCR
     ↓
Draw Bounding Box
     ↓
Save Frame
```

Output:

```text
frames/
```

Contains processed frames.

Run:

```bash
python video_reader.py
```

---

### frames/

Stores processed image frames.

Naming format:

```text
frame_0001.jpg
frame_0002.jpg
frame_0003.jpg
...
```

Each frame contains:

- Detected license plate
- Confidence score
- Extracted text
- Bounding boxes

---

### video_merger.py

Combines generated frames back into an MP4 video.

### Workflow

```text
Read Frames
     ↓
Sort Frames
     ↓
Create VideoWriter
     ↓
Write Frames
     ↓
Generate MP4
```

Run:

```bash
python video_merger.py
```

Output:

```text
output.mp4
```

---

## Processing Pipeline

```text
original.mp4
     ↓
video_reader.py
     ↓
frames/
     ↓
video_merger.py
     ↓
output.mp4
```

---

## Notes

- Frames are processed sequentially.
- OCR runs only when detection confidence exceeds threshold.
- Frame numbering uses zero padding for correct ordering.
- Output video uses MP4 encoding.

---

## Example Usage

Generate frames:

```bash
python video_reader.py
```

Merge frames:

```bash
python video_merger.py
```

Final output:

```text
output.mp4
```
