import numpy as np
import cv2
from ultralytics import YOLO
import random

# Mở file coco.txt
with open("D:\\FPT\\Kì học\\fall2024\\DPL302m\\yolo\\utils\\coco.txt", "r") as my_file:
    class_list = my_file.read().splitlines()

# Tạo màu ngẫu nhiên cho các lớp
detection_colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(class_list))]

# Tải mô hình YOLOv8
model = YOLO("weights/yolov7.pt")

# Mở video
cap = cv2.VideoCapture("D:\\FPT\\Kì học\\fall2024\\DPL302m\\yolo\\video\\nguoi.mp4")
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    
    # Lưu frame để dự đoán
    cv2.imwrite("D:\\FPT\\Kì học\\fall2024\\DPL302m\\yolo\\picture\\nguoi_lao_dong.jpg", frame)

    # Dự đoán trên hình ảnh
    detect_params = model.predict(source="D:\\FPT\\Kì học\\fall2024\\DPL302m\\yolo\\picture\\nguoi_lao_dong.jpg", conf=0.45, save=False)[0]

    # Kiểm tra nếu có phát hiện
    if detect_params.boxes:
        for box in detect_params.boxes:
            # Vẽ hình chữ nhật xung quanh phát hiện
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Tọa độ hộp
            class_id = int(box.cls)  # ID lớp
            confidence = box.conf.item()  # Chuyển đổi tensor thành số thực
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), detection_colors[class_id], 3)
            # Hiển thị tên lớp và độ tin cậy
            cv2.putText(frame, f"{class_list[class_id]} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    
    # Hiển thị frame
    cv2.imshow('ObjectDetection', frame)

    # Dừng khi nhấn 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng capture
cap.release()
cv2.destroyAllWindows()
