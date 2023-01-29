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
        self.stop_listening : r = r.listen_in_background(m,self.listen)
        
        # 안내메시지
        self.speak(text='무엇을 도와드릴까요?')
                        
        # 프로그램 무한 반복
        while True:
            time.sleep(0.1)            
        
    def listen(self,recognizer,audio)-> None:
        """ 음성인식 (STT) """
        try:
            text = recognizer.recognize_google(audio,language='ko')
            print(f'[User] : {text}')
            
            # answer 메소드 호출
            self.answer(input_text=text)

        except sr.UnknownValueError:
            print('인식 실패')   # 음성 인식 실패한 경우

        except sr.RequestError as rq_err: # # API Key 오류 또는 네트워크 단절 등 ..   
            print(f'요청 실패 : {rq_err}')
    
    def answer(self,input_text:str)-> None: 
        """ 대답 """
        answer_text : str = '' # 인공지능 대답        
        if '안녕' in input_text:
            answer_text = '안녕하세요 저는 인공지능입니다.'
        elif '날씨' in input_text:
            answer_text = '오늘의 서울 기온은 추울 것 같아요!'
        elif '고마워' in input_text:
            answer_text = '별 말씀을요!'
        elif '종료' in input_text:
            # 더 이상 듣지 않음
            answer_text = '다음에 또 만나요'
            self.stop_listening(wait_for_stop=False)
        else:
            answer_text = '잘 모르겠어요 ..'

        # 인공지능 speak
        self.speak(text=answer_text)
        
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
        
        # voide.mp3 파일 삭제
        self.remove_mp3(file_name=file_name)
            
    def play_sound(self,file_name:str):
        """ MP3 Play """
        playsound(file_name)    
    
    def remove_mp3(self,file_name:str):
        if os.path.exists(file_name):
            os.remove(file_name)
        
def main()-> None:
    # Create AISpeaker Instance
    ai_speaker : AISpeaker = AISpeaker()
    
    ai_speaker.run()
if __name__ == '__main__':
    main()