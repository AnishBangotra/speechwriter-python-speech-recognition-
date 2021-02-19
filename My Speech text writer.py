import speech_recognition as sr
from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError
import pyautogui
import time
from plyer import notification
import webbrowser as wb
process=True
def notifyme(title,message):
     notification.notify(
    title=title,
    message=message,
    app_icon="C:\\Users\\Anish\\Downloads\\audiowaveform_audio_3104.ico",#https://iconarchive.com/show/firefox-os-icons-by-vcferreira/clock-icon.html
    timeout=10
   )

print('Im listening to you!')
message_typed_count=0
def typewriter():
    global process
    global message_typed_count
    while process:
        try:
            re=sr.Recognizer()
            with sr.Microphone() as source:
                audio=re.listen(source)
            pyautogui.typewrite(re.recognize_google(audio))
            pyautogui.press('enter')
            time.sleep(0)
            print('Typed')
            message_typed_count+=1
            if message_typed_count==10:
                process=False
                notifyme('Speech Recognition Notifier Here',"You reached the limit of your voice type writing.!")
        except UnknownValueError:
                print('Sorry Can you speek again!')
typewriter()

def recording_file():
    with open('new_audio.wav', 'wb')as file:
        file.write(source.get_wav_data())
    try:
        recognized=recognizer.recognize_google(source)
        print(recognized)
    except RequestError as exe:
        print(exe)
    except UnknownValueError:
        print('Unable to recognize')

def listen():
    recog=Recognizer()
    mic=Microphone
    with mic:
        recog.adjust_for_ambient_noise(mic)
    print('Talk')
    audio_stopper=recog.listen_in_background(mic,recording_file)

def web_search():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r2.listen(source)
    if 'python' in r1.recognize_google(audio):
        r1=sr.Recognizer()
        url='https://www.youtube.com/'
        with sr.Microphone() as source:
            audio=r1.listen(source)
            try:
                get=r1.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))
