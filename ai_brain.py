"""
AI Brain: Handles intelligent responses using OpenAI
"""

import openai
from config import *
import logging

class AIBrain:
    def __init__(self):
        """Initialize AI brain with OpenAI"""
        openai.api_key = OPENAI_API_KEY
        self.conversation_history = []
        
        # System prompt to define assistant behavior
        self.system_prompt = {
            "role": "system",
            "content": f"""You are {ASSISTANT_NAME}, a helpful voice assistant. 
            Give brief, concise answers suitable for speech. 
            Keep responses under 3 sentences unless asked for more detail.
            Be friendly and helpful."""
        }
        
        if DEBUG_MODE:
            print("✅ AI Brain initialized")
    
    def get_response(self, user_input):
        """
        Get AI response for user input
        Args:
            user_input (str): User's question or command
        Returns:
            str: AI generated response
        """
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Keep only last 10 messages to avoid token limit
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            
            # Create messages list with system prompt
            messages = [self.system_prompt] + self.conversation_history
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model=AI_MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content.strip()
            
            # Add AI response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_response
            })
            
            logging.info(f"AI Response: {ai_response}")
            return ai_response
            
        except openai.error.AuthenticationError:
            return "OpenAI API key is invalid. Please check your config.py file."
        
        except openai.error.RateLimitError:
            return "API rate limit exceeded. Please try again later."
        
        except openai.error.APIConnectionError:
            return "Cannot connect to OpenAI. Please check your internet connection."
        
        except Exception as e:
            logging.error(f"AI Error: {e}")
            return "I encountered an error processing your request."
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        return "Conversation history cleared"