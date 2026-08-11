import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(1)

CONFIDENCE_THRESHOLD = 0.5
WANTED_CLASSES = None #Set this to {0} for detecting people only / None set as default

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    
    for box in results[0].boxes:
        
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]

        if conf < CONFIDENCE_THRESHOLD:
            continue
        if WANTED_CLASSES is not None and cls_id not in WANTED_CLASSES:
            continue

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()