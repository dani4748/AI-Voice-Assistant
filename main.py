"""
AI Voice Assistant - Main Entry Point
Created by: [mu]
"""

import os
from voice_engine import VoiceEngine
from command_processor import CommandProcessor
from config import *

def create_directories():
    """Create necessary directories if they don't exist"""
    directories = ['logs', 'data']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if DEBUG_MODE:
                print(f"✅ Created directory: {directory}")

def main():
    """Main function to run the voice assistant"""
    # Create necessary directories
    create_directories()
    
    # Initialize components
    voice = VoiceEngine()
    processor = CommandProcessor()
    
    # Welcome message
    print("=" * 50)
    print(f"   🤖 {ASSISTANT_NAME} - AI Voice Assistant")
    print("=" * 50)
    
    voice.speak(f"Hello! I am {ASSISTANT_NAME}, your AI voice assistant. How can I help you today?")
    
    # Main loop
    while True:
        try:
            # Listen for wake word (optional - comment out for always-on mode)
            # if not voice.listen_for_wake_word():
            #     continue
            
            # Listen for command
            command = voice.listen()
            
            if command:
                # Process command
                should_continue = processor.process(command)
                
                if not should_continue:
                    break
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Interrupted by user")
            voice.speak("Goodbye!")
            break
        
        except Exception as e:
            print(f"❌ Error: {e}")
            if DEBUG_MODE:
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    main()