# 🎙️ AI Voice Assistant with Voice Authentication

> A Python-based AI Voice Assistant that authenticates users using **voice biometrics** before executing voice commands. This project combines **speaker recognition**, **speech recognition**, and **text-to-speech** to provide a secure and personalized voice assistant experience.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge\&logo=tensorflow)
![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)


<p align="center">
<img src="demo.gif" width="900">
</p>

---

# 📖 Overview

Traditional voice assistants respond to anyone who speaks. This project adds an extra layer of security by verifying the speaker's identity before executing commands.

The system first records the user's voice, extracts audio features, authenticates the speaker using a trained machine learning model, and only then launches the voice assistant.

---

# ✨ Features

* 🎤 Voice Authentication
* 🤖 AI Voice Assistant
* 🔐 Speaker Verification
* 🗣 Speech-to-Text
* 🔊 Text-to-Speech
* 📂 Personalized Voice Profiles
* ⚡ Fast Authentication
* 🧠 Machine Learning Based Speaker Recognition
* 🎯 High Authentication Accuracy
* 💻 Simple Python Implementation

---

# 🛠️ Tech Stack

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Programming Language          |
| TensorFlow / Keras | Speaker Recognition Model     |
| Librosa            | Audio Feature Extraction      |
| NumPy              | Numerical Computing           |
| SpeechRecognition  | Speech-to-Text                |
| pyttsx3            | Text-to-Speech                |
| Scikit-Learn       | Machine Learning Utilities    |
| OS & Pickle        | File Handling & Model Storage |

---

# 🏗️ Project Architecture

```text
                 🎤 Microphone
                       │
                       ▼
              Record User Voice
                       │
                       ▼
           Audio Preprocessing
                       │
                       ▼
            MFCC Feature Extraction
                       │
                       ▼
          Speaker Authentication
               │              │
               │              │
         ❌ Unauthorized   ✅ Authorized
                               │
                               ▼
                     Launch Voice Assistant
                               │
                               ▼
                    Execute Voice Commands
```

---

# ⚙️ Workflow

```text
User Registration
        │
        ▼
Collect Voice Samples
        │
        ▼
Extract MFCC Features
        │
        ▼
Train Speaker Recognition Model
        │
        ▼
Save Trained Model
        │
        ▼
User Speaks
        │
        ▼
Authenticate Voice
        │
        ▼
Authentication Successful?
        │
   ┌────┴─────┐
   │          │
  No         Yes
   │          │
Access      Launch
Denied      Assistant
```

---

# 📁 Project Structure

```text
AI-Voice-Assistant-with-voice-authentication/
│
├── dataset/
├── models/
├── recordings/
├── voice_samples/
│
├── assistant.py
├── authentication.py
├── train_model.py
├── utils.py
├── requirements.txt
└── README.md
```

> **Update the folder names above if your repository structure is different.**

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/Pruthvik1111/AI-Voice-Assistant-with-voice-authentication.git
```

```bash
cd AI-Voice-Assistant-with-voice-authentication
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python assistant.py
```

---

# 💻 Usage

### Step 1

Register a new user's voice samples.

### Step 2

Train the speaker recognition model.

### Step 3

Launch the voice assistant.

### Step 4

Speak into the microphone.

### Step 5

If the authenticated voice matches a registered user, the assistant becomes active.

Otherwise, access is denied.

---

# 📊 Sample Output

```text
🎤 Listening...

Recording Complete.

Extracting MFCC Features...

Authenticating User...

Confidence Score : 98.42%

Authentication Successful ✅

Hello Pruthvik!

How can I help you today?
```

---


# 📈 Future Improvements

* 🌐 Cloud Deployment
* 🎙️ Wake Word Detection
* 👤 Multi-user Authentication
* 🧠 Deep Learning Speaker Recognition
* 📱 Mobile Application
* 🖥️ Modern GUI using CustomTkinter
* 🔒 Encryption for Voice Profiles
* 🤖 LLM Integration (OpenAI/Gemini)
* ☁️ Database Support
* 📊 Authentication Dashboard

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Pruthvik Shetty**

GitHub: https://github.com/Pruthvik1111

LinkedIn: *Add your LinkedIn profile here*

---

# ⭐ If you found this project useful...

Please consider giving it a ⭐ on GitHub. It helps the project reach more developers and motivates future improvements.

<p align="center">
⭐ Star this repository if you liked it! ⭐
</p>
