from playsound import playsound
from io import BytesIO
from gtts import gTTS
import tempfile

def tts_file(text, lang='en', slow=False):
    with tempfile.TemporaryFile() as temp_handler:
        engine = gTTS(text=text, lang=lang, slow=slow)
        engine.save(temp_handler.name)
        playsound(temp_handler.name)

def tts_direct(text, lang='en', slow=False):
    io = BytesIO()    
    engine = gTTS(text=text, lang=lang, slow=slow)
    engine.write_to_fp(io)
