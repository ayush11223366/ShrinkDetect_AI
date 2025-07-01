import os
import time
import cv2
import threading

save_interval = 2  # seconds
folder = "images"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

last_saved = time.time()

def save_image(image, filename):
    cv2.imwrite(filename, image)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show FPS (optional)
    cv2.imshow("Camera Feed", frame)

    current_time = time.time()
    if current_time - last_saved >= save_interval:
        filename = os.path.join(folder, f"{int(current_time)}.jpg")
        # Start saving image in a new thread
        threading.Thread(target=save_image, args=(frame.copy(), filename)).start()
        last_saved = current_time

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
