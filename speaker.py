from src.stt import set_speech
from src.tts import set_file,set_gTTS,set_text,run_mp3
import time
import os

class AISpeaker:
    def __init__(self,file_name:str) -> None:
        self.file_name : str
        
    def listen(self):
        """ 음성인식 (STT) """
        text : str = set_speech()
        return text

def main():
    # MP3 File Name
    file_name : str = set_file(file_name='sample.mp3')

    # Create AISpeaker Instance
    ai_speaker : AISpeaker = AISpeaker()
    
if __name__ == '__main__':
    main()