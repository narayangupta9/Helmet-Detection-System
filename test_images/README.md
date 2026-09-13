# Real-Time Helmet Detection System

A deep learning computer vision system built using YOLOv8 to detect motorcycle riders with and without helmets.

## Classes Detected
- `With Helmet`
- `Without Helmet`

## Project Structure
- `predict.py`: Inference script for detection on video feeds.
- `best.pt`: Fine-tuned YOLOv8 model weights.
- `test_videos/`: Sample input videos.
- `test_images/`: Sample input images.
- `output/`: Processed prediction results.

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt