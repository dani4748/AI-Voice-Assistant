# 🤖 AI Voice Assistant

A powerful AI-powered voice assistant that can control your computer, answer questions, and automate tasks using voice commands.

## ✨ Features

- 🎤 **Voice Recognition** - Hands-free voice control
- 🗣️ **Text-to-Speech** - Natural voice responses
- 🤖 **AI Integration** - Powered by OpenAI GPT for intelligent conversations
- 💻 **Application Control** - Open apps, websites with voice commands
- 🔍 **Web Search** - Search Google, YouTube instantly
- ⌨️ **Automation** - Type text, take screenshots, control system
- 📱 **WhatsApp Integration** - Send messages via voice
- 📚 **Wikipedia Search** - Get instant information
- 🔒 **System Controls** - Lock computer, shutdown, minimize windows

## 🎯 Voice Commands Examples

| Command | Action |
|---------|--------|
| "What time is it?" | Tells current time |
| "Open Chrome" | Opens Google Chrome |
| "Search for Python tutorials" | Searches on Google |
| "Play Despacito" | Plays on YouTube |
| "Type hello world" | Types text |
| "Take screenshot" | Captures screen |
| "Lock computer" | Locks PC |
| "What is artificial intelligence?" | AI explains |
| "Tell me a joke" | AI tells joke |
| "Wikipedia Python programming" | Searches Wikipedia |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Windows OS
- Microphone
- Internet connection

### Step 1: Install Python
Download from: https://www.python.org/downloads/

### Step 2: Clone/Download Project
```bash
cd "C:\all programs\M Danish\AI-Voice-Assistant"
Step 3: Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Step 4: Install Dependencies
pip install speechrecognition pyttsx3 pyautogui pywhatkit wikipedia openai python-dotenv requests pillow pipwin
pipwin install pyaudio
Step 5: Get OpenAI API Key
Go to: https://platform.openai.com/signup
Create free account
Navigate to API Keys section
Create new API key
Copy the key
Step 6: Configure API Key
Create .env file and add:
OPENAI_API_KEY=your-api-key-here
Step 7: Run the Assistant
python main.py
⚙️ Configuration
Edit config.py to customize:
Assistant name (default: "Jarvis")
Wake word (default: "hey jarvis")
Voice settings (rate, volume, gender)
Application paths
AI model settings
📁 Project Structure
AI-Voice-Assistant/
│
├── main.py                 # Main entry point
├── voice_engine.py         # Speech recognition & TTS
├── command_processor.py    # Command processing logic
├── ai_brain.py            # AI integration (OpenAI)
├── automation.py          # System automation tasks
├── config.py              # Configuration settings
├── .env                   # API keys (DO NOT SHARE!)
├── requirements.txt       # Dependencies
│
├── logs/                  # Activity logs
└── data/                  # User data
🛠️ Troubleshooting
Microphone Not Working
Check microphone permissions in Windows Settings
Test microphone in Sound settings
Restart the application
PyAudio Installation Error
pip install pipwin
pipwin install pyaudio
OpenAI API Errors
Verify API key is correct in .env
Check you have credits in OpenAI account
Ensure internet connection is stable
Import Errors
pip install --upgrade pip
pip install -r requirements.txt
📝 Usage Tips
Speak Clearly - Enunciate commands for better recognition
Wait for Response - Let assistant finish speaking before next command
Use Natural Language - Speak naturally, no need for exact phrases
Internet Required - Most features need internet connection
Microphone Quality - Better microphone = better recognition
🔐 Security Notes
Never share your .env file - Contains sensitive API keys
API costs - OpenAI charges after free tier, monitor usage
Microphone privacy - Assistant only listens when running
🎓 Learning Resources
Python: https://www.python.org/
OpenAI API: https://platform.openai.com/docs
Speech Recognition: https://pypi.org/project/SpeechRecognition/
PyAutoGUI: https://pyautogui.readthedocs.io/
🤝 Contributing
This is a personal/educational project. Feel free to fork and modify!
📜 License
Free to use for personal and educational purposes.
👨‍💻 Created By
Muhammad Danish
Project: AI Voice Assistant
Date: March 2026
Purpose: Learning & Internship Portfolio
🙏 Acknowledgments
OpenAI for GPT API
Python Speech Recognition library
pyttsx3 for text-to-speech
All open-source contributors
📞 Support
If you encounter issues:
Check the Troubleshooting section
Review logs in logs/assistant.log
Verify all dependencies are installed
Ensure API key is configured correctly
🔄 Version History
v1.0 (March 2026) - Initial release
Basic voice recognition
Text-to-speech
AI integration
System automation
Web search
Wikipedia integration
🚀 Future Enhancements
[ ] Mobile app version (Android)
[ ] Smart home integration
[ ] Calendar management
[ ] Email automation
[ ] Custom voice training
[ ] Multi-language support
[ ] Offline mode
[ ] Voice cloning
Made with ❤️ for learning and innovation
---

# 🚀 COMPLETE NEXT STEPS GUIDE

## **STEP 1: Wait for Installation to Complete** ⏳

Current status: Packages are installing (10/58 complete)

**What to do:**
- ✅ Wait for terminal to show "Successfully installed..."
- ✅ Don't close the terminal
- ✅ Be patient (3-5 more minutes)

---

## **STEP 2: Install PyAudio** 🎤

After the main installation completes:

```powershell
pipwin install pyaudio
Expected output:
Downloading pyaudio...
Installing pyaudio...
Successfully installed pyaudio