from gtts import gTTS
from playsound import playsound
import os

def set_text(source_txt:str)-> str:
    # 파일에서 불러와서 처리
    with open(source_txt,'r',encoding='UTF-8') as fp:
        return fp.read()

def set_file(file_name:str)-> str:
    os.path.abspath('mp3')
    if not os.path.exists('mp3'):
        os.mkdir('mp3')
    return os.path.join('mp3',file_name)

def set_gTTS(text:str,file_name:str)-> None:
    tts_ko : gTTS = gTTS(text=text,lang='ko')
    tts_ko.save(file_name)

def run_mp3(file_name:str):
    playsound(file_name)