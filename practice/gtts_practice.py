# TTS (Text To Speech)
# STT (Speech To Text)
from gtts import gTTS
from playsound import playsound


def set_text()-> str:
    # 영어문장
    # return 'Can I Help You?'
    # 한글문장
    return '파이썬을 배우면 이런 것도 할 수 있어요'

def set_file()-> str:
    return 'sample.mp3'

def set_gTTS(text:str,file_name:str)-> None:
    tts_en : gTTS = gTTS(text=text,lang='ko')
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