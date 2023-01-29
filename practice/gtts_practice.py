# TTS (Text To Speech)
# STT (Speech To Text)
from gtts import gTTS
from playsound import playsound

def set_text(source_txt:str)-> str:
    # 파일에서 불러와서 처리    
    with open(source_txt,'r',encoding='UTF-8') as fp:
        return fp.read()

def set_file()-> str:
    return 'sample.mp3'

def set_gTTS(text:str,file_name:str)-> None:
    tts_en : gTTS = gTTS(text=text,lang='ko')
    tts_en.save(savefile=file_name) 

def run_mp3(file_name:str): 
    playsound(file_name)
    
def main()-> None:
    # Source Text File
    source_txt : str = 'sample.txt'
    
    # Text
    text : str = set_text(source_txt=source_txt)
        
    # file name
    file_name : str = set_file()
    
    # gTTS
    set_gTTS(text=text,file_name=file_name)
    
    # run .mp3
    run_mp3(file_name=file_name)

if __name__ == '__main__':
    main()