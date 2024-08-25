import edge_tts

async def text_to_speech(text, output_file, voice="en-US-JennyNeural", pitch="+0Hz", rate="+0%"):
    try:
        communicate = edge_tts.Communicate(text, voice, pitch=pitch, rate=rate)
        await communicate.save(output_file)
        print(f"Text-to-speech output saved to {output_file}")
    except Exception as e:
        print(f"Error in text-to-speech conversion: {str(e)}")