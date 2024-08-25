from gtts import gTTS
from pygame import mixer
import os
import stat

def convertToMp3(sentence:str, output_directory:str, size:int) -> None:
    tts = gTTS(sentence, lang='en', slow=False, lang_check=True)
    tts.save(f'{output_directory}/sentence{size}.mp3')

def play(sentence:str) -> None:
    if len(sentence) == 0:
        return None
    if os.path.exists('F:/Python/TextToSpeech/buffer.mp3'):
        os.remove('F:/Python/TextToSpeech/buffer.mp3')
    mixer.init()
    tts = gTTS(sentence, lang = 'en', slow = False, lang_check = True)
    tts.save('F:/Python/TextToSpeech/buffer.mp3')
    os.chmod('F:/Python/TextToSpeech/buffer.mp3', stat.S_IRWXO | stat.S_IRWXG | stat.S_IRWXU)
    mixer.music.load('F:/Python/TextToSpeech/buffer.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.stop()
    mixer.music.unload()
