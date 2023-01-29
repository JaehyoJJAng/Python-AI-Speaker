# TTS (Text To Speech)
# STT (Speech To Text)
from gtts import gTTS
from playsound import playsound


def set_text()-> str:
    return 'Can I Help You?'

def set_file()-> str:
    return 'sample.mp3'

def set_gTTS(text:str,file_name:str)-> None:
    tts_en : gTTS = gTTS(text=text,lang='en')
    tts_en.save(savefile=file_name) 

def run_mp3(file_name:str):
    playsound(file_name)
    
def main()-> None:
    # Text
    text : str = set_text()
    
    # file name
    file_name : str = set_file()
    
    # gTTS
    set_gTTS(text=text,file_name=file_name)
    
    # run .mp3
    run_mp3(file_name=file_name)

if __name__ == '__main__':
    main()