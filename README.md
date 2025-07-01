# 📦 Object Direction Counter (YOLOv8 + Tracking)

A lightweight real-time object tracking and counting system using **YOLOv8** and OpenCV. The system detects an object and only increments or decrements the count if it moves **left to right** or **right to left**, respectively. It avoids duplicate counts by assigning unique **tracking IDs** to each object.

---

## 🎯 Features

- ✅ Real-time object detection using YOLOv8
- ✅ Assigns and tracks unique object IDs
- ✅ Counts object only once per pass (avoids duplicate count)
- ✅ Counts increment if object moves **left → right**
- ✅ Counts decrement if object moves **right → left**
- ✅ Overwrites count in `track_log.csv` every frame with timestamp
- ✅ Adjustable frame size: 1280×1280

---

## 🛠 Tech Stack

- Python 3.10
- OpenCV
- Ultralytics YOLOv8
- Custom logic for direction-based counting

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/object-direction-counter.git
   cd object-direction-counter
   ```

2. **Set up virtual environment (optional but recommended)**
   ```bash
   python -m venv shrinkenv
   shrinkenv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program**
   ```bash
   python main.py
   ```

---

## 📂 File Structure
```
├── main.py              # Main execution script
├──capture.py            # Capture images for training model
├──trainmode.py          # train model
├──shrink_detect         # trained model files
├── utils.py             # Helper functions for direction and logging
├── track_log.csv        # Output file with timestamp and current count
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
```

---

## 📝 Sample Output
```
ID 4 moved right. Count: 1
ID 4 moved left. Count: 0
```

---

## 📌 Notes
- Model used: `yolov8n.pt` (can be replaced with your trained weights)
- Make sure your webcam is accessible by OpenCV

---

## 📧 Contact
If you're a recruiter or looking for collaboration, feel free to connect:

**Name**: Ayush Kumar  
**Email**: [ayushrajpoot2004@gmail.com]  
**LinkedIn**: [https://www.linkedin.com/in/ayush-kumar-473a37370/]  
**GitHub**: [https://github.com/ayush11223366]

---

> 🚀 This project is part of my submission for a computer vision internship and ongoing work for Sparkathon 2025.
