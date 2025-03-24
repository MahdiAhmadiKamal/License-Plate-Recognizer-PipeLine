import cv2
from ultralytics import YOLO
# from deep_text_recognition_benchmark.dtrb import DTRB

image = cv2.imread("io\input\IMG_5157.JPG")
# Load a model
plate_detector = YOLO("weights\yolov8-detector\yolov8s-license-plate-detector.pt")
result = plate_detector.predict(image)
result = result[0]

for i in range(len(result.boxes.xyxy)):
    if result.boxes.conf[i] > 0.5:
        bbox = result.boxes.xyxy[i]
        print(bbox)
        bbox = bbox.cpu().detach().numpy().astype(int)
        print(bbox)
        plate_image = image[bbox[1]:bbox[3], bbox[0]:bbox[2]].copy()
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 4)

cv2.imwrite("io\output\image_result.jpg", image)
cv2.imwrite("io\output\plate_image_result.jpg", plate_image)

# plate_recognizer = DTRB("weights/dtrb-recognizer/dtrb-TPS-ResNet-BiLSTM-Attn-license-plate-recognizer.pth")
# plate_recognizer.predict("io\input-plates")