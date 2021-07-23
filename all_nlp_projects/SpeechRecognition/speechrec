import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import smtplib

responseAgain=''
r=sr.Recognizer()
speechapi=pyttsx3.init('sapi5')
voices=speechapi.getProperty('voices')

speechapi.setProperty('voice',voices[1].id)


def speak(audio):
    speechapi.say(audio)
    speechapi.runAndWait()



def wishing():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Goodmorning!")

    elif hour>=12 and hour<18:
        speak("Good Noon!")
    else:
        speak("Good Evening!")
   
    speak("A little voice Assistant at your service,Mam!How May I Help you?")
def  takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold=1
        r.energy_threshold=3000
        audio=r.listen(source)
        query=""
    try:
        print("Recognizing")
        query=r.recognize_google(audio,)
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-mail-id','your-password')
    server.sendmail('your-mail-id',to, content)
    server.close()
def mailprocess():
               speak("Please mention the mailname of Reciever")
               id='@gmail.com'
               mailname=takeCommand()
               mailn=''.join(mailname.lower().split())
               to=mailn+id
               print("Email id:",to)
               speak("Please check if the email is correct.")
               resp=takeCommand()
               if 'yes' in resp:
                   
                   speak("What do you want send as message?")
                   content=takeCommand()
                   speak("are you sure you want to send this msg?")
                   ans=takeCommand()
                   if  'yes' in ans:
                       sendEmail(to,content)
                       print("Email has been sent sucessfully.")
                       speak("Email has been sent successfully.")
                   else:
                       speak("Your email was not being sent.Please try again.")  
               else:
                   speak("Uh oh!No worries.Please Try again.")
                   mailprocess()
    
    
    
    
    
if __name__== "__main__":
 while True:
        wishing()
        while True:
               query= takeCommand().lower()
               if 'wikipedia' in query:
                   
                       speak("Let me Know what do you wanna search")
                       url='https://en.wikipedia.org/wiki/'
                       with sr.Microphone() as source:
                            print("Listening...")
                            audio=r.listen(source,timeout=3)
                            get=''
                        
                       try:
                            get=r.recognize_google(audio)
                            print(get)
                            speak("Okay,Gotcha.Here is the result.")
                            wb.get().open_new(url+get)
                            
                       except sr.UnknownValueError:
                             print('error')
                        
                       except sr.RequestError as e:
                            print('failed'.format(e))
                       break
                   
                  
                    
               elif 'time' in query:
                  strTime=datetime.datetime.now().strftime("%H:%M:%S")
                  speak(f"Mam the time is {strTime}")
                  break
                   
               elif 'really bored' in query:
                  speak('Lets play some songs then!')
                  music_folder="D:\\Songs"
                  songs=os.listdir(music_folder)
                  os.startfile(os.path.join(music_folder,songs[0]))
                  break
               elif 'mail' in query:
                  try:
                   mailprocess()
                      
                  except Exception():
                       print(Exception)
                  break
        speak("Any more service mam?")
        responseAgain=takeCommand()
        if responseAgain !='yes':
          speak("Thankyou Hope you must have got help Have a nice day ahead!")
          break 
