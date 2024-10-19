import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY') or 'YOUR_GOOGLE_MAPS_API_KEY_HERE'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'YOUR_OPENAI_API_KEY_HERE'
