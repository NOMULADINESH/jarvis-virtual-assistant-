import requests
import music_library
import speech_recognition as sr
import webbrowser
import pyttsx3
import openai  # Correct OpenAI API import

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    openai.api_key = "<Your Key Here>"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

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

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")  

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")    

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")    

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chat.openai.com")    

    elif "open black box" in c.lower():
        webbrowser.open("https://blackbox.com")    

    elif "open internshala" in c.lower():
        webbrowser.open("https://internshala.com")    

    elif "open notion" in c.lower():
        webbrowser.open("https://notion.so")    

    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")  

    elif c.lower().startswith("play"):
        songs = c.lower().split(" ")[1]
        if songs in music_library.music:  # Fix for checking if song exists in the dictionary
            link = music_library.music[songs]  
            webbrowser.open(link) 
        else:
            speak(f"Sorry, I couldn't find {songs}.")

    elif "today headlines" in c.lower():
        city = c.split("in")[-1].strip()  # Extract city name
        weather_info = get_weather(city)
        speak(weather_info)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes")
                    
            with sr.Microphone() as source:
                print("Jarvis activated...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processcommand(command)

        except Exception as e:
            print(f"Error: {e}")
