from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import time
import os

class AISpeaker:    
    def run(self)-> None:
        # Create Recognizer Instance
        r : sr.Recognizer = sr.Recognizer()

        # Create MicroPhone Instance
        m : sr.Microphone() = sr.Microphone()
        
        # 백그라운드로 계속 열어둠
        stop_listening : r = r.listen_in_background(m,self.listen)
        
        # 안내메시지
        self.speak(text='무엇을 도와드릴까요?')
                
        # 더 이상 듣지 않음
        stop_listening(wait_for_stop=False)
        
        # 프로그램 무한 반복
        while True:
            time.sleep(0.1)
            
        
    def listen(self,recognizer,audio)-> None:
        """ 음성인식 (STT) """
        pass
    
    def answer(self,input_text:str)-> None: 
        """ 대답 """
        pass
    
    def speak(self,text:str)-> None:
        # 인공지능 출력문
        print(f'[인공지능] : {text}')
        
        """ 소리내어 읽기 (TTS) """
        file_name : str = 'voide.mp3'
        
        # Create tts instance
        tts : gTTS = gTTS(text=text,lang='ko')
        
        # Save
        tts.save(file_name)
        
        # Play Mp3
        self.play_sound(file_name=file_name)
            
    def play_sound(self,file_name:str):
        """ MP3 Play """
        playsound(file_name)
        
def main()-> None:
    # Create AISpeaker Instance
    ai_speaker : AISpeaker = AISpeaker()
    
    ai_speaker.run()
if __name__ == '__main__':
    main()