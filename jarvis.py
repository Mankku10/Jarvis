import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('   hello mayank sir , I am your buddy , how can i help you  ')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('\nrecognition')
        query = r.recognition_google(audio , language='en-in')
        print(f'user said : {query}')
    except Exception as e:
        print('say again please')
        return "none"
    return query

def sendMail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email-id' , 'your-password')
    server.sendmail('your-e-mail-id' ,to ,content)
    server.close()



if __name__ == '__main__':
    wish()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("please wait , seaching in wikipedia")
            query = query.replace("wikipedia" , "")
            speak("accoding to wikipedia")
            results = wikipedia.summary(query , sentence=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play song' in query:
            music_dir = (addressed the dir of song)
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H%M%S")
            speak(f"sir , the is {strtime}")

        elif 'open game' in query:
            path = (adressed the path)
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("whats should i say")
                content = takecommand()
                to = 'receiver email id'
                sendMail(to, content)
                speak('your email has been send')

            except Exception as e:
                print(e)
                speak('sorry mayank sir your email does not send')

        elif 'exit' in query:
            exit()



