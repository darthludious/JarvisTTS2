import speech_recognition as sr
import pyttsx3
import time
import requests
from pathlib import Path
import tempfile
import wave
import pyaudio
import numpy as np
from collections import deque
from threading import Thread, Event
import audioop
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TTSProvider:
    def __init__(self):
        # Initialize fallback TTS engine
        self.fallback_engine = pyttsx3.init()
        voices = self.fallback_engine.getProperty('voices')
        for voice in voices:
            if "male" in voice.name.lower():
                self.fallback_engine.setProperty('voice', voice.id)
                break
        self.fallback_engine.setProperty('rate', 150)
        self.fallback_engine.setProperty('volume', 0.9)

        # TTS API configuration
        self.use_api = False  # Set to True when API is configured
        self.api_url = os.getenv('TTS_API_URL', '')  # URL for your TTS API
        self.api_key = os.getenv('TTS_API_KEY', '')  # API key if required

    def speak(self, text):
        if self.use_api and self.api_url:
            try:
                # Placeholder for API call - modify according to your chosen API
                response = requests.post(
                    self.api_url,
                    headers={
                        'Authorization': f'Bearer {self.api_key}',
                        'Content-Type': 'application/json'
                    },
                    json={'text': text}
                )
                
                if response.status_code == 200:
                    # Handle audio playback from API response
                    # This will need to be implemented based on the API response format
                    pass
                else:
                    # Fallback to pyttsx3 if API call fails
                    self._fallback_speak(text)
            except Exception as e:
                print(f"TTS API error: {e}")
                self._fallback_speak(text)
        else:
            self._fallback_speak(text)

    def _fallback_speak(self, text):
        """Fallback to pyttsx3 when API is not available"""
        self.fallback_engine.say(text)
        self.fallback_engine.runAndWait()

# Rest of the code remains unchanged
