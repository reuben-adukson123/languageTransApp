import streamlit as st
from googletrans import Translator
from gtts import gTTS
import base64
import os

# Main App Logic
st.title("Language Translator with Auto Play Pronunciation")

# Text input from user
text_to_translate = st.text_area("Enter text to translate:")

# Language input
target_language = st.text_input("Enter target language (e.g., 'fr' for French, 'es' for Spanish):")

if st.button("Translate"):
    # Translate the text
    translator = Translator()
    translation = translator.translate(text_to_translate, dest=target_language)
    
    st.write(f"Translated Text: {translation.text}")

    # Generate and save audio pronunciation
    tts = gTTS(translation.text, lang=target_language)
    audio_file = "translated_audio.mp3"
    tts.save(audio_file)

    # Convert audio file to base64 to embed it in HTML for autoplay
    audio_bytes = open(audio_file, "rb").read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

    # Embed HTML with autoplay for the audio file
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

    # Optionally, remove the file after playing
    os.remove(audio_file)
