import whisper
from config import WHISPER_MODEL_SIZE
import os

model = None

def load_model():
    global model
    if model is None:
        print(f"Loading Whisper model with size: {WHISPER_MODEL_SIZE}")
        model = whisper.load_model(WHISPER_MODEL_SIZE)
        print("Model loaded successfully")

def speech_to_text(audio_file):
    try:
        print(f"Attempting to transcribe file: {audio_file}")
        print(f"File exists (inside function): {os.path.exists(audio_file)}")
        print(f"File size (inside function): {os.path.getsize(audio_file) if os.path.exists(audio_file) else 'N/A'}")
        
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"The audio file {audio_file} does not exist.")
        
        load_model()
        print("Starting transcription")
        
        # Try using an absolute path
        abs_audio_file = os.path.abspath(audio_file)
        print(f"Absolute path: {abs_audio_file}")
        
        result = model.transcribe(abs_audio_file)
        print("Transcription completed")
        return result["text"]
    except Exception as e:
        error_message = f"Error in speech recognition: {str(e)}"
        print(error_message)
        print(f"Current working directory: {os.getcwd()}")
        return error_message