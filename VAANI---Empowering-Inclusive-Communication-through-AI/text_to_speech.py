from gtts import gTTS
import os
import tempfile

def text_to_speech(text, language='en', emotion=None, voice_type=None, pitch=None, speed=None):
    # Mapping of language codes to their corresponding gTTS language names
    language_map = {
        "en": "en",
        "hi": "hi",
        "gu": "gu",
        "kn": "kn",
        "ml": "ml",
        "mr": "mr",
        "ta": "ta",
        "te": "te"
    }

    # Get the corresponding gTTS language name
    gtts_language = language_map.get(language, "hi")

    # Emotion mapping to gTTS parameters
    emotion_map = {
        "neutral": None,
        "happy": "happy",
        "sad": "sad",
        "angry": "angry",
        "surprised": "surprised"
    }

    # Set emotion parameter for gTTS
    gtts_emotion = emotion_map.get(emotion, None)

    # Create gTTS object
    tts = gTTS(text, lang=gtts_language, tld='com', slow=False, lang_check=True)

    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        temp_file_name = temp_file.name
        tts.save(temp_file_name)

    with open(temp_file_name, 'rb') as audio_file:
        audio_bytes = audio_file.read()

    os.unlink(temp_file_name)

    return audio_bytes