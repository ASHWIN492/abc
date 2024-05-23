import streamlit as st
from PIL import Image
import tempfile
import os
import image_processing
import pdf_processing
import text_to_speech

def text_to_speech_page():
    st.title("Text-to-Speech with Emotion and Voice Customization")
    # Text input section
    text_input = st.text_area("Enter Text", height=200)
    # Language selection
    language = st.selectbox("Select Language", ["en", "hi", "gu", "kn", "ml", "mr", "ta", "te"])
    # Emotion selection
    emotion = st.selectbox("Select Emotion", ["neutral", "happy", "sad", "angry", "surprised"])
    # Voice type selection
    voice_type = st.selectbox("Select Voice Type", ["male", "female"])
    # Pitch selection
    pitch = st.slider("Select Pitch", min_value=0.5, max_value=2.0, step=0.1)
    # Speed selection
    speed = st.slider("Select Speed", min_value=50, max_value=300, step=10)

    if text_input:
        if st.button("Convert Text to Speech"):
            with st.spinner('Converting text to speech...'):
                audio_bytes = text_to_speech.text_to_speech(text_input, language, emotion, voice_type, pitch, speed)
            st.success("Text conversion completed!")
            st.audio(audio_bytes, format='audio/mp3')

def pdf_to_speech_page():
    st.title("PDF to Speech Conversion")
    # File upload section
    file = st.file_uploader("Upload PDF", type=['pdf'])

    if file:
        if file.type == 'application/pdf':
            with st.spinner('Extracting text...'):
                text = pdf_processing.extract_text_from_pdf(file)
            if text.startswith("Error:"):
                st.error(text)
            else:
                st.write("Extracted Text:")
                st.write(text)
                # Language selection
                language = st.selectbox("Select Language", ["en", "hi", "gu", "kn", "ml", "mr", "ta", "te"])
                # Emotion selection
                emotion = st.selectbox("Select Emotion", ["neutral", "happy", "sad", "angry", "surprised"])
                # Voice type selection
                voice_type = st.selectbox("Select Voice Type", ["male", "female"])
                # Pitch selection
                pitch = st.slider("Select Pitch", min_value=0.5, max_value=2.0, step=0.1)
                # Speed selection
                speed = st.slider("Select Speed", min_value=50, max_value=300, step=10)

                if st.button("Convert PDF to Speech"):
                    with st.spinner('Converting PDF to speech...'):
                        audio_bytes = text_to_speech.text_to_speech(text, language, emotion, voice_type, pitch, speed)
                    st.success("PDF conversion completed!")
                    st.audio(audio_bytes, format='audio/mp3')

def image_processing_page():
    st.title("Image Processing")
    uploaded_image = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Process Image"):
            prediction = image_processing.process_image(image)
            st.write("Image Prediction:", prediction)

def main():
    pages = {
        "Text to Speech": text_to_speech_page,
        "PDF to Speech": pdf_to_speech_page,
        "Image Processing": image_processing_page
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    pages[selection]()

if __name__ == '__main__':
    main()