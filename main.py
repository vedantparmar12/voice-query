import asyncio
import os
from speech_to_text import speech_to_text
from llm_processing import generate_response
from text_to_speech import text_to_speech

async def voice_query_pipeline(audio_file, output_file):
    print(f"Attempting to process audio file: {audio_file}")
    print(f"File exists: {os.path.exists(audio_file)}")
    print(f"File size: {os.path.getsize(audio_file) if os.path.exists(audio_file) else 'N/A'}")
    
    # Step 1: Speech-to-Text
    transcribed_text = speech_to_text(audio_file)
    print(f"Transcribed text: {transcribed_text}")
    
    # Step 2: LLM Processing
    llm_response = generate_response(transcribed_text)
    print(f"LLM response: {llm_response}")
    
    # Step 3: Text-to-Speech
    await text_to_speech(llm_response, output_file)

def find_wav_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.wav')]

async def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script directory: {current_dir}")
    
    wav_files = find_wav_files(current_dir)
    
    if not wav_files:
        print("Error: No .wav files found in the current directory.")
        print(f"Current directory: {current_dir}")
        print("Please place a .wav file in this directory and run the script again.")
        return

    print(f"Found the following .wav files: {wav_files}")
    audio_file = os.path.join(current_dir, wav_files[0])  # Use the first .wav file found
    output_file = os.path.join(current_dir, "output_response.mp3")
    
    print(f"Using audio file: {audio_file}")
    await voice_query_pipeline(audio_file, output_file)

if __name__ == "__main__":
    asyncio.run(main())