from ultralytics import YOLO # type: ignore
# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov9m.pt")

# Train the model using the 'yolov9m.pt' dataset for 3 epochs
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.train(data="data.yaml", epochs=20, imgsz=512, device='cpu')
#amp giúp giảm kích thước dữ liệu mà GPU phải xử lý,
#cho phép bạn xử lý các tập dữ liệu lớn hơn và giảm bớt bộ nhớ sử dụng trên GPU.