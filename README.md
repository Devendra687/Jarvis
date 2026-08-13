# 🤖 Jarvis — Personal AI Voice Assistant

A personal voice assistant built with **Python**. Jarvis listens for the wake word **"Jarvis"**, understands voice commands, performs useful system and browser actions, and uses **Gemini AI** to handle general questions.

> 🚧 **Jarvis is an actively developing learning project.** New features, better automation, and AI/ML capabilities will be added over time.

---

## ✨ Features

* 🎤 **Voice Activation** — Activate Jarvis using the wake word `"Jarvis"`
* 🔊 **Text-to-Speech** — Jarvis responds using `pyttsx3`
* 🧠 **Gemini AI** — Handles general questions and conversations
* 🌐 **Website Launcher** — Open Google, YouTube, Instagram, Snapchat, etc.
* 🔎 **Voice-Controlled YouTube Search** — Search YouTube using voice commands
* 🎵 **Music Commands** — Play songs using a local music library
* 🖥️ **Desktop App Launcher** — Open installed applications using `AppOpener`
* 📸 **Screenshot Support** — Take screenshots with automatically generated timestamps
* 🐍 **Virtual Environment** — Project uses a Python virtual environment for dependency management

---

## 🛠️ Technologies & Libraries

* **Python**
* **SpeechRecognition** — Voice input and speech recognition
* **PyAudio** — Microphone/audio support
* **pyttsx3** — Text-to-speech
* **Google GenAI** — Gemini AI integration
* **AppOpener** — Desktop application launching
* **PyAutoGUI** — Screenshot functionality
* **webbrowser** — Browser automation
* **datetime** — Timestamp generation

For the complete list of dependencies, see `requirements.txt`.

---

## 📁 Project Structure

```text
Jarvis/
├── jarvis.py
├── musicliab.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env              # Local API keys — never commit this
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Devendra687/Jarvis.git
cd Jarvis
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

If a newly added package is missing from `requirements.txt`, install it and update the dependency file:

```powershell
python -m pip install <package-name>
python -m pip freeze > requirements.txt
```

### 5. Configure the Gemini API Key

Keep your API keys **out of GitHub**.

Store your API key locally in `.env` and make sure `.env` is included in `.gitignore`.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

> Make sure your Python code is configured to read the API key from your environment before running Jarvis.

### 6. Run Jarvis

```powershell
python jarvis.py
```

Then say:

```text
Jarvis
```

Jarvis will listen for your command.

---

## 🎙️ Example Commands

```text
Jarvis
```

```text
open calculator
```

```text
open youtube
```

```text
search Python tutorial
```

```text
take a screenshot
```

```text
play <song name>
```

Commands that are not handled by Jarvis's local command system are passed to Gemini AI.

---

## 🔐 Security

**Never commit sensitive information to GitHub.**

Make sure the following are ignored:

```gitignore
.env
.venv/
__pycache__/
.vscode/
```

Never put your actual API key directly inside `jarvis.py` or `README.md`.

---

## 🧠 How Jarvis Works

The current command flow is based on a simple command-routing system:

```text
Voice Input
     ↓
Wake Word Detection
     ↓
Command Recognition
     ↓
Command Router
     ↓
┌──────────────┬──────────────┬──────────────┐
│   Browser    │   AppOpener  │   Screenshot │
│   / Music    │              │              │
└──────────────┴──────────────┴──────────────┘
                    ↓
                 Gemini AI
                    ↓
                Response
```

This architecture will be improved as Jarvis becomes more intelligent and modular.

---

## 🔮 Future Plans

* 🌦️ Weather information
* 🌐 Better web search integration
* 🧠 Improved AI-powered command understanding
* 🗣️ More natural voice conversations
* 💾 Memory system for remembering useful information
* 🖥️ More universal desktop controls
* 🎵 Improved music search and playback
* 📂 File and folder management through voice
* 📧 Email and notification integration
* 🏠 Smart device control
* 🤖 Intelligent task automation
* 🧩 Modular tool-based architecture
* 🧠 AI/ML-powered intent detection
* 🔗 Integration with more APIs and services

---

## 🎯 Long-Term Goal

The long-term goal is to turn Jarvis into a capable **personal AI assistant** that can understand natural language, identify the user's intent, choose the appropriate tool, perform tasks on the system, access useful information from the web, and eventually use a modular **AI/ML architecture** for smarter decision-making and automation.

---

## 📌 Project Status

**Status: 🚧 In Development**

Jarvis is currently being developed as both a personal AI assistant and a learning project. The project will gradually evolve from a simple rule-based voice assistant into a more intelligent and modular AI system.
