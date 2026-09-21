import time
from flask import Flask, render_template, jsonify
import cv2

app = Flask(__name__)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

# PARAMETERS
OBSERVATION_TIME = 20  # seconds
DISTRACTION_THRESHOLD = 3  # max allowed distractions
FACE_MISSING_TIME = 3  # seconds

start_time = time.time()
last_face_seen = time.time()
distraction_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    global last_face_seen, distraction_count

    ret, frame = cap.read()
    if not ret:
        return jsonify({"status": "Attentive"})

    current_time = time.time()

    # Observation phase
    if current_time - start_time < OBSERVATION_TIME:
        remaining = int(OBSERVATION_TIME - (current_time - start_time))
        return jsonify({"status": "Observing", "remaining": remaining})

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3, minSize=(80, 80))

    if len(faces) > 0:
        last_face_seen = current_time
        return jsonify({"status": "Attentive"})

    # Face missing
    if current_time - last_face_seen > FACE_MISSING_TIME:
        distraction_count += 1
        last_face_seen = current_time

        if distraction_count >= DISTRACTION_THRESHOLD:
            return jsonify({"status": "Distracted"})

    return jsonify({"status": "Attentive"})

if __name__ == "__main__":
    app.run(debug=True)
