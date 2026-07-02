# 🚗 AI Driver Monitoring System (DMS)

> A flagship AI-powered Driver Monitoring System that uses Computer Vision, Facial Landmark Detection, and Deep Learning to detect driver fatigue, distraction, and unsafe driving behavior in real time.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Mesh-orange)
![YOLO](https://img.shields.io/badge/YOLOv8-Planned-red)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

This project is a modular **Driver Monitoring System (DMS)** inspired by modern automotive safety systems.

It continuously monitors the driver's face to estimate fatigue and attention using computer vision and AI techniques.

The long-term goal is to build a production-style Driver Monitoring System similar in concept to those used in modern vehicles.

---

# ✨ Current Features

- ✅ Real-time camera capture
- ✅ MediaPipe Face Mesh
- ✅ Eye landmark extraction
- ✅ Eye Aspect Ratio (EAR)
- ✅ Blink detection
- ✅ Eye closure timer
- ✅ Driver state detection
- ✅ Full facial mesh rendering
- ✅ Modular project architecture

---

# 🚀 Planned Features

### 🖥 Premium Dashboard

- Automotive HUD
- FPS counter
- Current time
- Driver status
- Attention meter
- Fatigue meter
- Animated widgets
- Professional UI

---

### 🧠 AI Driver Intelligence

- Head Pose Estimation
- Yawn Detection (MAR)
- Composite Risk Score
- DriverBrain Decision Engine

---

### 👁 Driver Monitoring

- Blink Detection
- Eye Closure Detection
- Distraction Detection
- Driver Attention Monitoring

---

### 📱 Object Detection

- Phone Detection (YOLOv8)
- Phone Near Face Detection

---

### 📊 Analytics

- SQLite Database
- Session Reports
- Event Timeline
- Blink Statistics
- EAR Graph
- Driver Safety Report

---

### 🔊 Alert System

- Audio Alarm
- Warning Banner
- Flashing HUD
- Fatigue Alerts

---

### 🔌 Embedded Integration

- MQTT
- ESP32
- OLED Display
- Buzzer
- LED
- Vibration Motor

---

# 🏗 Project Structure

```
AI-Driver-Drowsiness-Monitoring/

├── main.py

├── src/

│   ├── camera.py
│   ├── face_mesh.py
│   ├── constants.py

│   ├── core/
│   │     └── driver_state.py

│   ├── detectors/
│   │     ├── blink_detector.py
│   │     ├── eye_detector.py
│   │     ├── drowsiness_detector.py
│   │     └── head_pose_detector.py

│   ├── dashboard/
│   │     ├── dashboard.py
│   │     ├── theme.py
│   │     ├── widgets.py
│   │     ├── panels.py
│   │     ├── animations.py
│   │     └── hud.py

│   └── utils/

├── tests/

└── README.md
```

---

# 🛠 Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

Future:

- YOLOv8
- SQLite
- MQTT
- ESP32
- FastAPI
- React Dashboard

---

# 🎯 System Pipeline

```
Camera
   │
   ▼
Face Mesh
   │
   ├── Blink Detection
   ├── Eye Closure
   ├── Head Pose
   ├── Yawn Detection
   └── Phone Detection
            │
            ▼
      DriverBrain
            │
            ▼
 Composite Risk Score
            │
            ▼
 Dashboard + Alarm
            │
            ▼
 SQLite + ESP32
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/Shaun-max-code/AI-Driver-Drowsiness-Monitoring.git

cd AI-Driver-Drowsiness-Monitoring
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# 📈 Development Roadmap

## Phase 1

- [x] Face Mesh
- [x] Blink Detection
- [x] EAR
- [x] Driver State
- [x] Modular Architecture

## Phase 2

- [ ] Premium Dashboard
- [ ] Head Pose Estimation
- [ ] Yawn Detection
- [ ] DriverBrain

## Phase 3

- [ ] SQLite Logging
- [ ] Session Reports
- [ ] Timeline
- [ ] Statistics

## Phase 4

- [ ] YOLO Phone Detection
- [ ] Performance Optimization

## Phase 5

- [ ] ESP32 Integration
- [ ] MQTT
- [ ] Embedded Alert System

---

# 👨‍💻 Author

**Shaun Mathew**

Electronics & Communication Engineer

GitHub:
https://github.com/Shaun-max-code

LinkedIn:
https://www.linkedin.com/in/shaun-mathew-709ba5247

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.