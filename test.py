import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5/runs/train/aurebesh/weights/best.mlmodel')

image = 'images/train/1a6e3418-a843-4707-8591-a65c79a97303.jpg'

results = model(image)

print(results)
