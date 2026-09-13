from ultralytics import YOLO

# Load model weights
model = YOLO("best.pt")

model.predict(
    source="test_videos/helmet.mp4",  
    save=True,
    show=True,
    conf=0.25
)