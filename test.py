import pyttsx3
# Keep pip install for pyttsx3
import speech_recognition as sr
# Keep pip install for SpeechRecognition
import datetime
import wikipedia
# Keep pip install for wikipedia
import webbrowser
import os
import smtplib

# Use espeak for text-to-speech on Kali
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    os.system(f"espeak -s 10 '{text}'")  # Adjust speed with -s option (optional)



def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")

  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")

  else:
    speak("Good Evening!")

  speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
  # It takes microphone input from the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

  except Exception as e:
    print(e)
    print("Say that again please...")
    return "None"
  return query


def sendEmail(to, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login('youremail@gmail.com', 'your-password')
  server.sendmail('youremail@gmail.com', to, content)
  server.close()

if __name__ == "__main__":
  wishMe()
  while True:
    # if 1:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=2)
      speak("According to Wikipedia")
      print(results)
      speak(results)

    elif 'open youtube' in query:
      webbrowser.open("youtube.com")

    elif 'open google' in query:
      webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
      webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
      music_dir = '/path/to/your/music/folder'  # Replace with your music directory
      for filename in os.listdir(music_dir):
        if filename.endswith(".mp3"):  # Modify for your music format
          os.system(f"vlc {os.path.join(music_dir, filename)} &")  # Play in background
          break

    
