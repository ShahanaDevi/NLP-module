from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the converted audio to a file
    tts.save("output.mp3")
    # Play the generated audio file
    os.system("start output.mp3")

if __name__ == "__main__":
    # Example text to convert to speech
    text = "Hello, this is a AI machine learning based E-learning platform."

    # Perform text-to-speech conversion
    text_to_speech(text)
