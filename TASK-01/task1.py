from ultralytics import YOLO
model = YOLO('yolov8n-seg.pt')#other models also exist
model.predict(source='https://ultralytics.com/images/bus.jpg', save=True, save_dir='output')
