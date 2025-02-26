# import requests

# # URL của mô hình YOLOv7
# url = 'https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt'

# # Tải file về máy
# response = requests.get(url)

# # Lưu file
# with open('yolov7.pt', 'wb') as f:
#     f.write(response.content)

# print("Tải xong mô hình YOLOv7!")

import torch
import cv2
import time

# Đường dẫn tới mô hình và video
model_path = 'yolov7.pt'  # Thay thế đường dẫn này bằng nơi bạn lưu mô hình
video_path = r'xe.mp4'  # Đường dẫn đến video đầu vào
output_path = 'output_video.mp4'  # Đường dẫn đến video đầu ra


# Load mô hình YOLOv7
model = torch.hub.load('WongKinYiu/yolov7', 'custom', path=model_path, source='github')

# Thiết lập VideoCapture cho video đầu vào
cap = cv2.VideoCapture(video_path)

# Lấy thông tin từ video (frame rate, size)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Thiết lập VideoWriter để lưu video đầu ra
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Chạy YOLOv7 trên từng frame của video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    start_time = time.time()

    # Chạy mô hình YOLOv7 trên từng frame
    results = model(frame)

    # Vẽ khung bao quanh đối tượng phát hiện lên frame
    results.render()

    # Tính toán và in ra FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    print(f"FPS: {fps:.2f}")

    # Ghi lại frame với khung bao quanh vào video đầu ra
    out.write(frame)

    # Hiển thị kết quả (nếu muốn)
    cv2.imshow('YOLOv7 Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
out.release()
cv2.destroyAllWindows()

print("Hoàn thành phát hiện đối tượng trong video!")
