import cv2
import time

# Load Haar Cascade (SAFE PATH)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# -------- NEW VARIABLES --------
distraction_count = 0
MAX_ALLOWED_DISTRACTIONS = 3

face_detected_time = 0
start_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(60, 60)
    )

    face_count = len(faces)

    # -------- MODIFIED ATTENTION LOGIC --------
    if face_count > 0:
        attention_status = "Attentive"
        status_color = (0, 255, 0)

        distraction_count = 0  # reset distractions

        if start_time is None:
            start_time = time.time()
        face_detected_time = int(time.time() - start_time)

    else:
        distraction_count += 1

        if distraction_count > MAX_ALLOWED_DISTRACTIONS:
            attention_status = "Distracted"
            status_color = (0, 0, 255)
            start_time = None
            face_detected_time = 0
        else:
            attention_status = "Attentive"
            status_color = (0, 255, 0)

    # Draw face rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display info
    cv2.putText(frame, f"Status: {attention_status}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)

    cv2.putText(frame, f"Faces Detected: {face_count}",
                (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.putText(frame, f"Distraction Count: {distraction_count}",
                (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.putText(frame, f"Face Time: {face_detected_time}s",
                (10, 135), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # For Flask integration later
    print(attention_status)

    cv2.imshow("Cognitive State Detection - Press Q to Exit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
