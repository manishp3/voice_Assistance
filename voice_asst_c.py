import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os

def sp_text():
    recg=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        recg.adjust_for_ambient_noise(source)
        
        audio=recg.listen(source)
        try:
            print("Recegnizing...")
            data=recg.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print(" Not Understand")
# sp_text()
def sptotxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

sptotxt("Hello manish")

#ayathi comment do
if __name__=='__main__':

    # if sp_text().lower()=="hay manish":
    while True:
        data1=sp_text().lower()
        if "you name :" in data1:
            name="my name is manish"
            sptotxt(name)
        elif "how old are you?" in data1:
            age= "I am two year old"
            sptotxt(age)    
        elif 'time' in data1:
            time=datetime.datetime.now().strftime("%I%m%p")
            sptotxt(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'web' in data1:
            webbrowser.open("https://www.github.com/")
        elif 'play song' in data1:
            address="C:\Users\Manish Patadiya\Music"
            listsong=os.listdir(address)
            print(listsong)
            os.startfile(os.path.join(address,listsong[2]))
        elif "exit" in data1:
            sptotxt("thank you")
            break
        time.sleep(5)
        
    # else:
    #     print("Thaks😃")