from ultralytics import YOLO
import numpy

# load a pretrained YOLOv8n model
model = YOLO("yolov8m.pt", "v8")

# predict on an image
detection_output = model.predict(source="D:\\FPT\\Kì học\\fall2024\\DPL302m\\yolo\\picture\\nguoi_lao_dong.jpg", conf=0.25, save=True)

# Display tensor array
print(detection_output)

# Display numpy array
print(detection_output[0].numpy())
