# Webcam Object Detector

Real-time object detection using YOLOv8 and OpenCV. Just point your webcam at the world and watch it recognize people, chairs, phones, cups, and 76 other everyday objects, live, in a window on your screen.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9%2B-5C3EE8?logo=opencv&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What it does

This project captures live video from your webcam and runs each frame through **YOLOv8n**, a pretrained object detection model, drawing bounding boxes and labels around anything it recognizes in real time. No internet required after the initial model download.

## Features

- Real-time detection straight from your webcam
- 80 object classes out of the box (COCO dataset: people, vehicles, animals, household items, and more)
- Adjustable confidence threshold to filter out uncertain guesses
- Optional class filtering: detect only the objects you care about
- Built to be understood, not just run: the code is written in progressive stages rather than one dense script

## How it works

Rather than one black-box script, this project is built in a series of phases, each adding one concept on top of the last:

| Phase | What it adds |
|---|---|
| **1. Webcam capture** | Get a live video window with zero ML using just OpenCV |
| **2. Static inference** | Run YOLOv8 on a single image, inspect the raw output |
| **3. Live detection** | Combine the two: run the model on every webcam frame |
| **4. Manual drawing** | Replaced the built-in `.plot()` shortcut with custom box-drawing code |
| **5. Filtering** | Add confidence thresholds and class filters on top |

If you're reading through the code, start at `webcam.py` and work your way through the project structure below.

## Equipment

- Python 3.10+
- A webcam (built-in or external)
- ~10MB free disk space for the model weights
- M2 Macbook Air 8gb (runs smoothly)

## Installation

```bash
git clone https://github.com/grumpy-jerry/webcam-object-detector.git
cd webcam-object-detector
pip3 install -r requirements.txt
```

No virtual environment required as this installs directly to your system Python. (If you'd rather isolate it, `python3 -m venv venv && source venv/bin/activate` before the `pip3 install` works too.)

## Usage

Run any stage directly:

```bash
python3 thresholds_and_filtering.py
```

A window opens showing your webcam feed with live bounding boxes. Press **`q`** with the video window focused to quit cleanly.

The first run downloads `yolov8n.pt` (~6MB) automatically.

### Adjusting detection

Open the script and tweak these two lines near the top:

```python
CONFIDENCE_THRESHOLD = 0.5   # raise this to reduce false positives
WANTED_CLASSES = None        # e.g. {0} to detect only "person"
```

Class indices come from the COCO dataset, meaning index `0` is `person`, `2` is `car`, `16` is `dog`, and so on. The full list is available via `model.names` in Python, or in the [Ultralytics COCO class reference](https://docs.ultralytics.com/datasets/detect/coco/).

## Project structure

```
webcam-object-detector/
├── webcam.py                        # Webcam capture only, no ML
├── static_image.py                  # YOLOv8 on a single still image
├── live_detection.py                # Live detection using .plot()
├── manual_boxes.py                  # Manual box-drawing, no shortcuts
├── thresholds_and_filtering.py      # Confidence threshold + class filtering
└── README.md
```

## Built with

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) : object detection model
- [OpenCV](https://opencv.org/) : webcam capture and display

## Next steps / ideas

- Fine-tune YOLOv8n on a custom dataset to detect objects outside the standard 80 COCO classes
- Add object counting per frame
- Trigger an action (sound, notification, log entry) when a specific class is detected
- Swap in a larger model (`yolov8s.pt`, `yolov8m.pt`, etc.) for higher accuracy at the cost of speed
