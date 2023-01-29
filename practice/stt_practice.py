import speech_recognition as sr

# Create Recognizer Instance
r : sr.Recognizer = sr.Recognizer()

# 마이크를 통해서 들려오는 음성 저장
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source=source)

try:
    # 구글 API 로 인식 (하루 50회)
    # 영어 문장
    text = r.recognize_google(audio_data=audio,language='en-US')
    print(text)
except sr.UnknownValueError:
    print('인식 실패')   # 음성 인식 실패한 경우
except sr.RequestError as rq_err: # # API Key 오류 또는 네트워크 단절 등 ..   
    print(f'요청 실패 : {rq_err}')