# Personalized Learning through Cognitive State Analysis: A Context-Aware AI Companion

This application provides real-time cognitive state analysis using a webcam to personalize the learning experience. It analyzes facial expressions, eye movements, and head posture to identify the learner's cognitive state and provides adaptive feedback to improve engagement and learning effectiveness.

## Setup Instructions

1. Clone this repository.

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment.

**Windows**

```bash
.\venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Click **Start Monitoring** to begin the cognitive state analysis.

4. Allow camera access when prompted.

5. The system continuously analyzes the learner's behavior and displays the detected cognitive state along with personalized feedback.

## The System Analyzes

* Facial expressions
* Eye movements and attention
* Head posture
* Face detection
* Learning engagement
* Cognitive state

## Features

* Real-time cognitive state detection
* Webcam-based facial analysis
* Personalized learning feedback
* Learner engagement monitoring
* Context-aware AI assistance
* Interactive web interface
* Live performance visualization
* Lightweight and easy-to-use application

## Technology Stack

* Backend: Flask
* Computer Vision: OpenCV
* Face Detection: Haar Cascade Classifier
* Programming Language: Python
* Frontend: HTML, CSS, JavaScript
* Real-time Processing: OpenCV Video Capture

## Working Process

1. The user starts the learning session.
2. The webcam captures live video frames.
3. The system detects the user's face using OpenCV.
4. Facial features and head movements are analyzed.
5. The learner's cognitive state is identified.
6. Personalized feedback is generated in real time.
7. The process repeats continuously throughout the learning session.

## Project Structure

```
├── app.py
├── webcam.py
├── requirements.txt
├── haarcascade_frontalface_default.xml
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   └── index.html
└── README.md
```

## Future Enhancements

* Deep learning-based emotion recognition
* Eye gaze tracking
* Blink and fatigue detection
* Attention score prediction
* Adaptive content recommendation
* Student performance analytics dashboard
* Learning history and progress tracking
* Multi-user support

## Note

* Ensure your webcam is connected and accessible.
* Install all required Python packages before running the application.
* Allow browser camera permissions for real-time monitoring.
* The application performs best under adequate lighting conditions.
* This project is intended for educational and research purposes.
