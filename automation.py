"""
Automation Module: Handles system automation tasks
"""

import pyautogui
import webbrowser
import os
import subprocess
import time
from config import *

class Automation:
    def __init__(self):
        """Initialize automation module"""
        # Set PyAutoGUI safety settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
    
    def open_application(self, app_name):
        """
        Open an application
        Args:
            app_name (str): Name of application to open
        Returns:
            str: Status message
        """
        apps = {
            'chrome': CHROME_PATH,
            'browser': CHROME_PATH,
            'notepad': NOTEPAD_PATH,
            'calculator': CALCULATOR_PATH,
            'calc': CALCULATOR_PATH,
        }
        
        app_name = app_name.lower()
        
        if app_name in apps:
            try:
                os.startfile(apps[app_name])
                return f"Opening {app_name}"
            except Exception as e:
                return f"Failed to open {app_name}: {e}"
        else:
            # Try to open as system command
            try:
                os.system(f"start {app_name}")
                return f"Opening {app_name}"
            except:
                return f"Application {app_name} not found"
    
    def open_website(self, url):
        """
        Open a website in default browser
        Args:
            url (str): Website URL
        Returns:
            str: Status message
        """
        try:
            if not url.startswith('http'):
                url = 'https://' + url
            
            webbrowser.open(url)
            return f"Opening {url}"
        except Exception as e:
            return f"Failed to open website: {e}"
    
    def search_google(self, query):
        """
        Search on Google
        Args:
            query (str): Search query
        Returns:
            str: Status message
        """
        try:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            return f"Searching for {query}"
        except Exception as e:
            return f"Failed to search: {e}"
    
    def search_youtube(self, query):
        """
        Search on YouTube
        Args:
            query (str): Search query
        Returns:
            str: Status message
        """
        try:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            return f"Searching YouTube for {query}"
        except Exception as e:
            return f"Failed to search YouTube: {e}"
    
    def type_text(self, text):
        """
        Type text using keyboard automation
        Args:
            text (str): Text to type
        Returns:
            str: Status message
        """
        try:
            time.sleep(2)  # Give user time to focus on target window
            pyautogui.write(text, interval=0.05)
            return f"Typed: {text}"
        except Exception as e:
            return f"Failed to type: {e}"
    
    def press_key(self, key):
        """
        Press a keyboard key
        Args:
            key (str): Key to press (e.g., 'enter', 'space')
        Returns:
            str: Status message
        """
        try:
            pyautogui.press(key)
            return f"Pressed {key} key"
        except Exception as e:
            return f"Failed to press key: {e}"
    
    def take_screenshot(self):
        """
        Take a screenshot
        Returns:
            str: Status message
        """
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            
            return f"Screenshot saved as {filename}"
        except Exception as e:
            return f"Failed to take screenshot: {e}"
    
    def minimize_all_windows(self):
        """
        Minimize all windows (Show desktop)
        Returns:
            str: Status message
        """
        try:
            pyautogui.hotkey('win', 'd')
            return "Minimized all windows"
        except Exception as e:
            return f"Failed to minimize windows: {e}"
    
    def lock_computer(self):
        """
        Lock the computer
        Returns:
            str: Status message
        """
        try:
            os.system("rundll32.exe user32.dll,LockWorkStation")
            return "Locking computer"
        except Exception as e:
            return f"Failed to lock computer: {e}"
    
    def shutdown_computer(self, minutes=1):
        """
        Shutdown computer after specified minutes
        Args:
            minutes (int): Minutes to wait before shutdown
        Returns:
            str: Status message
        """
        try:
            seconds = minutes * 60
            os.system(f"shutdown /s /t {seconds}")
            return f"Computer will shutdown in {minutes} minute(s)"
        except Exception as e:
            return f"Failed to schedule shutdown: {e}"
    
    def cancel_shutdown(self):
        """
        Cancel scheduled shutdown
        Returns:
            str: Status message
        """
        try:
            os.system("shutdown /a")
            return "Shutdown cancelled"
        except Exception as e:
            return f"Failed to cancel shutdown: {e}"