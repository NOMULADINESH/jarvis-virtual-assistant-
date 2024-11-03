import requests
import random
import jokes
import speech_recognition as sr
import webbrowser
import pyttsx3
import music_liberies

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    joke = random.choice(jokes)
    speak(joke)

def get_weather(city):
    api_key = "ca8041f766714fe59c9670d934237873"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']
        return f"The current temperature in {city} is {temperature}°C with {weather_description}."
    else:
        return "Sorry, I couldn't get the weather information."

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open git hub" in c.lower():
        webbrowser.open("https://git hub.com")    

    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin hub.com")    

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")    

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chat gpt hub.com")    

    elif "open black box" in c.lower():
        webbrowser.open("https://black box ai.com")    

    elif "open internshala" in c.lower():
        webbrowser.open("https://internshala.com")    

    elif "open notion" in c.lower():
        webbrowser.open("https://notion.com")    

    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")  

    elif c.lower().startswith("play"):
        songs=c.lower().split(" ")[1]
        link=music_liberies.music[songs]  
        webbrowser.open(link) 

    elif "tell me a joke" in command:
       tell_joke()

    elif "today headlines" in command:
        city = command.split("in")[-1].strip()  # Extract city name
        weather_info = get_weather(city)
        speak(weather_info)


      


if __name__=="__main__":
    speak("initializing jarvis...")
    while True:
        # listen for the wakeup word jarvis

        r=sr.Recognizer()

        print("recognizing...")
        try:
           with sr.Microphone() as source:
              print("listining...")
              audio=r.listen(source,timeout=2,phrase_time_limit=1)
              word=r.recognize_google(audio)
              if(word.lower()=="jarvis"):
                speak("ya")
                #listen for command
           with sr.Microphone() as source:
              print("jarvis activated...")
              audio=r.listen(source)
              command=r.recognize_google(audio)

              processcommand(command)


        except Exception as e:
            print(f"error {e}")    



