# 🦖 Chrome Dino Game Automation

A Python automation bot that plays the **Google Chrome Dino Game** automatically using **Computer Vision** and **Keyboard Automation**. The bot continuously monitors the game screen, detects upcoming obstacles in real time, and performs perfectly timed jumps to achieve high scores without any human interaction.

This project demonstrates the practical use of **OpenCV**, **PyAutoGUI**, and image processing techniques for building a real-time game automation system. It is an excellent beginner-to-intermediate computer vision project and showcases how AI-inspired automation can interact with graphical applications.

---

## 📌 Features

- 🎯 Automatically detects obstacles in the Chrome Dino Game.
- ⚡ Performs real-time jumps with minimal delay.
- 👀 Uses Computer Vision for obstacle recognition.
- ⌨️ Simulates keyboard inputs automatically.
- 🚀 Fast and lightweight Python implementation.
- 📈 Capable of achieving very high scores without manual gameplay.
- 🛠️ Easy to customize detection area and jump timing.
- 💻 Beginner-friendly project with clean and understandable code.

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV (cv2)
- PyAutoGUI
- NumPy
- Keyboard Library

---

## 📂 Project Structure

```
Chrome-Dyno-game-automation/
│
├── images/                 # Sample screenshots or templates
├── main.py                 # Main automation script
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── assets/                 # Optional project images/GIFs
```

---

## ⚙️ How It Works

1. Open the Chrome Dino Game.
2. Start the Python script.
3. The program continuously captures a predefined region of the screen.
4. Using OpenCV, it analyzes the captured frames for incoming obstacles.
5. Once an obstacle is detected within the danger zone, the script automatically presses the **Spacebar** to make the dinosaur jump.
6. This process repeats continuously, allowing the bot to play the game automatically.

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Chrome-Dyno-game-automation.git
```

### Navigate to the project folder

```bash
cd Chrome-Dyno-game-automation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install manually:

```bash
pip install opencv-python pyautogui numpy keyboard
```

---

## ▶️ Usage

1. Open **Google Chrome**.
2. Disconnect your internet or visit:

```
chrome://dino
```

3. Start the game.
4. Run the automation script:

```bash
python main.py
```

5. Sit back and watch the bot play automatically.

---

## 🧠 Detection Logic

The automation follows a simple real-time workflow:

```
Capture Screen
        │
        ▼
Convert to Grayscale
        │
        ▼
Detect Obstacle Pixels
        │
        ▼
Obstacle Found?
   │           │
  No          Yes
   │           │
 Continue   Press Space
   │           │
   └────Repeat────┘
```

---

## 📸 Demo

You can add screenshots or GIFs here.

Example:

```
assets/demo.gif
```

or

```markdown
![Demo](assets/demo.gif)
```

---

## 🔧 Customization

You can easily modify:

- Detection region
- Jump threshold
- Screen resolution
- Detection sensitivity
- Game speed optimization

This makes the project compatible with different monitor sizes and resolutions.

---

## 💡 Future Improvements

- 🦅 Detect flying birds
- ⚡ Automatic ducking
- 🎮 Adaptive AI based on game speed
- 🤖 Machine Learning obstacle prediction
- 📊 Score tracking
- 🎥 Live detection visualization
- 🖥️ GUI for easy configuration

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Computer Vision basics
- Screen capture techniques
- Image processing using OpenCV
- Keyboard automation
- Real-time object detection
- Python automation
- Game bot development
- Performance optimization

---

## 📋 Requirements

- Python 3.8+
- Windows 10/11 (Recommended)
- Google Chrome
- Chrome Dino Game

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It motivates further development and helps others discover the project.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nakul Rajurkar**

B.Tech – Artificial Intelligence & Data Science

Feel free to connect and explore more of my projects!

---

### ⭐ If you like this project, don't forget to star the repository!
