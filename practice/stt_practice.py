import speech_recognition as sr

def set_speech()-> None:
    # Create Recognizer Instance    
    r : sr.Recognizer = sr.Recognizer()

    # Set MicroPhone
    # audio : sr.AudioData = set_micro_phone(r=r)
    
    # Set Audio File
    audio : sr.AudioFile = set_audio_file(r=r)
    
    try:
        # 구글 API 로 인식 (하루 50회)
        # 영어 문장
        # text = r.recognize_google(audio_data=audio,language='en-US')
        
        # 한글 문장
        text = r.recognize_google(audio_data=audio,language='ko')
        print(text)
    except sr.UnknownValueError:
        print('인식 실패')   # 음성 인식 실패한 경우
    except sr.RequestError as rq_err: # # API Key 오류 또는 네트워크 단절 등 ..   
        print(f'요청 실패 : {rq_err}')
    
def set_micro_phone(r:sr.Recognizer)-> sr.AudioData:
    """ 마이크로부터 음성 듣기"""
    with sr.Microphone() as source:
        print('듣고 있어요')
        audio : sr.AudioData = r.listen(source=source)
        return audio

def set_audio_file(r:sr.Recognizer)-> sr.AudioFile:
    """ 파일로부터 음성 불러오기 (.wav , .aiff , .flac) """
    with sr.AudioFile('sample.wav') as source:
        audio : sr.AudioFile  = r.record(source=source)
        return audio 

def main():
    set_speech()

if __name__ == '__main__':
    main()