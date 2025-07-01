# main.py
import cv2
from ultralytics import YOLO
from utils import check_direction, update_log
import time

# Load YOLOv8 model
model = YOLO("shrink_detect/yolov8-highres/weights/best.pt")
  # Replace with your trained model path

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

# Store tracking positions
track_history = {}
counted_ids = set()
object_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True, conf=0.5, iou=0.5, verbose=False)[0]

    if results.boxes.id is not None:
        for box in results.boxes:
            id = int(box.id.item())
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Track direction
            direction, updated = check_direction(id, cx, track_history, counted_ids)
            if updated:
                if direction == "right":
                    object_count += 1
                elif direction == "left" and object_count > 0:
                    object_count -= 1
                print(f"ID {id} moved {direction}. Count: {object_count}")

    # Show count on frame
    cv2.putText(frame, f'Count: {object_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    cv2.imshow("Object Tracker", frame)

    # Save data every frame
    update_log(object_count)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
