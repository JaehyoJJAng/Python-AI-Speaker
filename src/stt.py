import speech_recognition as sr

def set_speech()-> str:
    # Create Recognizer Instance    
    r : sr.Recognizer = sr.Recognizer()

    # Set MicroPhone
    audio : sr.AudioData = set_micro_phone(r=r)
    
    try:    
        text = str(r.recognize_google(audio_data=audio,language='ko'))
        return text
    except sr.UnknownValueError:
        print('음성인식 실패')
    except sr.RequestError as req_err:
        print(f'음성요청 실패 : {req_err}')
        
def set_micro_phone(r:sr.Recognizer)-> sr.AudioData:
    """ 마이크로부터 음성 듣기"""
    with sr.Microphone() as source:
        print('듣고 있어요')
        audio : sr.AudioData = r.listen(source=source)
        return audio
