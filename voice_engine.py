"""
Voice Engine: Handles speech recognition and text-to-speech
"""

import speech_recognition as sr  # type: ignore
import pyttsx3
import logging
from config import *

class VoiceEngine:
    def __init__(self):
        """Initialize speech recognition and text-to-speech engines"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
        # Configure TTS engine
        self.setup_voice()
        
        # Setup logging
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        if DEBUG_MODE:
            print("✅ Voice Engine initialized")
    
    def setup_voice(self):
        """Configure text-to-speech settings"""
        voices = self.engine.getProperty('voices')
        
        # Set voice (male/female)
        if VOICE_GENDER < len(voices):
            self.engine.setProperty('voice', voices[VOICE_GENDER].id)
        
        # Set speech rate and volume
        self.engine.setProperty('rate', VOICE_RATE)
        self.engine.setProperty('volume', VOICE_VOLUME)
    
    def speak(self, text):
        """
        Convert text to speech
        Args:
            text (str): Text to speak
        """
        print(f"🗣️ {ASSISTANT_NAME}: {text}")
        logging.info(f"Speaking: {text}")
        
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """
        Listen to microphone and convert speech to text
        Returns:
            str: Recognized text or empty string if failed
        """
        with sr.Microphone() as source:
            print("🎤 Listening...")
            
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )
                
                print("🔄 Recognizing...")
                
                # Convert speech to text using Google Speech Recognition
                command = self.recognizer.recognize_google(audio)
                
                print(f"👤 You said: {command}")
                logging.info(f"User command: {command}")
                
                return command.lower()
                
            except sr.WaitTimeoutError:
                if DEBUG_MODE:
                    print("⏱️ Listening timeout")
                return ""
            
            except sr.UnknownValueError:
                if DEBUG_MODE:
                    print("❓ Could not understand audio")
                return ""
            
            except sr.RequestError as e:
                print(f"❌ Speech recognition error: {e}")
                logging.error(f"Speech recognition error: {e}")
                return ""
            
            except Exception as e:
                print(f"❌ Error: {e}")
                logging.error(f"Unexpected error: {e}")
                return ""
    
    def listen_for_wake_word(self):
        """
        Listen for wake word to activate assistant
        Returns:
            bool: True if wake word detected
        """
        print(f"💤 Say '{WAKE_WORD}' to activate...")
        command = self.listen()
        
        if WAKE_WORD in command:
            self.speak("Yes, I'm listening")
            return True
        
        return False