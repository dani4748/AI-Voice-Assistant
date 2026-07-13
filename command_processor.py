"""
Command Processor: Process and execute user commands
"""

import datetime
import wikipedia
import pywhatkit
from voice_engine import VoiceEngine
from automation import Automation
from ai_brain import AIBrain
from config import *

class CommandProcessor:
    def __init__(self):
        """Initialize command processor"""
        self.voice = VoiceEngine()
        self.auto = Automation()
        self.ai = AIBrain()
        
        if DEBUG_MODE:
            print("✅ Command Processor initialized")
    
    def process(self, command):
        """
        Process and execute user command
        Args:
            command (str): User's voice command
        Returns:
            bool: True to continue, False to exit
        """
        command = command.lower()
        
        # ========== EXIT COMMANDS ==========
        if any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
            self.voice.speak("Goodbye! Have a great day!")
            return False
        
        # ========== TIME & DATE ==========
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.voice.speak(f"The time is {current_time}")
        
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.voice.speak(f"Today is {current_date}")
        
        # ========== OPEN APPLICATIONS ==========
        elif 'open' in command:
            app_name = command.replace('open', '').strip()
            
            # Special cases
            if 'whatsapp' in app_name:
                result = self.auto.open_website(WHATSAPP_WEB)
            elif 'youtube' in app_name:
                result = self.auto.open_website(YOUTUBE_URL)
            else:
                result = self.auto.open_application(app_name)
            
            self.voice.speak(result)
        
        # ========== SEARCH ==========
        elif 'search' in command:
            query = command.replace('search', '').replace('for', '').strip()
            
            if 'youtube' in command:
                result = self.auto.search_youtube(query)
            else:
                result = self.auto.search_google(query)
            
            self.voice.speak(result)
        
        # ========== TYPE TEXT ==========
        elif 'type' in command:
            text = command.replace('type', '').strip()
            self.voice.speak("Typing in 2 seconds. Click on the target window")
            result = self.auto.type_text(text)
            self.voice.speak(result)
        
        # ========== SCREENSHOT ==========
        elif 'screenshot' in command or 'capture screen' in command:
            result = self.auto.take_screenshot()
            self.voice.speak(result)
        
        # ========== MINIMIZE WINDOWS ==========
        elif 'minimize' in command or 'show desktop' in command:
            result = self.auto.minimize_all_windows()
            self.voice.speak(result)
        
        # ========== LOCK COMPUTER ==========
        elif 'lock' in command:
            result = self.auto.lock_computer()
            self.voice.speak(result)
        
        # ========== SHUTDOWN ==========
        elif 'shutdown' in command:
            self.voice.speak("Are you sure you want to shutdown?")
            confirm = self.voice.listen()
            
            if 'yes' in confirm or 'sure' in confirm:
                result = self.auto.shutdown_computer(1)
                self.voice.speak(result)
            else:
                self.voice.speak("Shutdown cancelled")
        
        # ========== WIKIPEDIA ==========
        elif 'wikipedia' in command or 'wiki' in command:
            query = command.replace('wikipedia', '').replace('wiki', '').strip()
            
            try:
                self.voice.speak("Searching Wikipedia...")
                result = wikipedia.summary(query, sentences=2)
                self.voice.speak(result)
            except:
                self.voice.speak("Could not find information on Wikipedia")
        
        # ========== PLAY MUSIC/VIDEO ==========
        elif 'play' in command:
            query = command.replace('play', '').strip()
            self.voice.speak(f"Playing {query} on YouTube")
            pywhatkit.playonyt(query)
        
        # ========== WHATSAPP MESSAGE ==========
        elif 'whatsapp' in command and 'message' in command:
            self.voice.speak("Please say the phone number")
            phone = self.voice.listen()
            
            self.voice.speak("What message should I send?")
            message = self.voice.listen()
            
            try:
                # Get current time + 2 minutes
                now = datetime.datetime.now()
                hour = now.hour
                minute = now.minute + 2
                
                if minute >= 60:
                    minute -= 60
                    hour += 1
                
                pywhatkit.sendwhatmsg(f"+{phone}", message, hour, minute)
                self.voice.speak("Message will be sent in 2 minutes")
            except:
                self.voice.speak("Failed to send WhatsApp message")
        
        # ========== WHO ARE YOU ==========
        elif 'who are you' in command or 'what are you' in command:
            self.voice.speak(f"I am {ASSISTANT_NAME}, your AI voice assistant. I can help you with various tasks like opening applications, searching the web, and answering questions.")
        
        # ========== CLEAR HISTORY ==========
        elif 'clear history' in command or 'forget' in command:
            result = self.ai.clear_history()
            self.voice.speak(result)
        
        # ========== AI CHAT (DEFAULT) ==========
        else:
            # Use AI for everything else
            response = self.ai.get_response(command)
            self.voice.speak(response)
        
        return True