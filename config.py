"""
Configuration file for AI Voice Assistant
Store your API keys and settings here
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============== API KEYS ==============
# OpenAI API Key (Get from: https://platform.openai.com/api-keys)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")

# ============== ASSISTANT SETTINGS ==============
ASSISTANT_NAME = "Jarvis"  # Change to your preferred name
WAKE_WORD = "hey jarvis"   # Wake word to activate assistant
VOICE_RATE = 150          # Speech rate (words per minute)
VOICE_VOLUME = 1.0        # Volume (0.0 to 1.0)

# ============== VOICE SETTINGS ==============
# Voice gender: 0 = Male, 1 = Female (may vary by system)
VOICE_GENDER = 0

# ============== PATHS ==============
CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
NOTEPAD_PATH = "notepad.exe"
CALCULATOR_PATH = "calc.exe"
WHATSAPP_WEB = "https://web.whatsapp.com"
YOUTUBE_URL = "https://www.youtube.com"

# ============== COMMAND SETTINGS ==============
TIMEOUT = 5  # Seconds to wait for command
PHRASE_TIME_LIMIT = 5  # Max seconds for a single phrase

# ============== AI SETTINGS ==============
AI_MODEL = "gpt-3.5-turbo"  # OpenAI model to use
MAX_TOKENS = 150  # Maximum response length
TEMPERATURE = 0.7  # Creativity (0.0 to 1.0)

# ============== DEBUGGING ==============
DEBUG_MODE = True  # Set to False in production
LOG_FILE = "logs/assistant.log"