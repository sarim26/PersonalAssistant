from os import replace
import speech_recognition as sr
import pyttsx3
import wolframalpha
import webbrowser as wb
import datetime
import requests
import json
import random

#Code for RTB, Road To Brilliance, a personal assistant/AI made by Sarim. Mark 2.

engine = pyttsx3.init('sapi5')
engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
r = sr.Recognizer()

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

def greeting():
    hr=datetime.datetime.now().hour
    if hr >= 5 and hr <12:
        list = ["Good Morning, lazy! May this day be full of productivity…from someone else! Obviously, not you!",
        "Good Morning! Parting from your best friend can be difficult… but I am sure you will go back to bed, in no time!",
        "As the day begins, remember that I am your friend. you're welcome!",
        "Good Morning to a friend who starts each day by asking important questions: Should I get up at ten or eleven? Is there pizza left over from last night? Have a good day, deep thinker!",
        "Your morning should begin with a message from a friend who really cares about you…but that's not happening, today! Take care, I guess!",
        "Good Morning to someone I would like to consider to be a friend. Don't get too excited. I stated that I would like to.",
        "Good Morning to someone who sets, when the sun rises, and rises, when the sun sets! Pretty sure you've got that backwards, sir. Have a nice nap!",
        "Sir, someday you will be a morning person! But i doubt that it's going to happen any time soon.",
        "Good Morning to a friend, who outdoes everyone… in sleeping! You excel at that!",
        "Let me Finish my Coffee First and nobody gets hurt. Have a Good Morning!",
        "Let me Finish my Coffee First and nobody gets hurt. Have a Good Morning!"]
        message= random.choice(list)
        print(message + "How may I help you?")
        speak(message + "How may I help you?")
        instruction()
    elif hr >= 12 and hr < 18:
        ga= ["Good afternoon to you sir . Or should i say, good morning?", "A very good afternoon to you, sir ." , "Good afternoon, sir "]
        gafinale= random.choice(ga)
        print(gafinale + "How may I assist you?")
        speak(gafinale + ", How may I assist you?")
        instruction()
    else:
        gn= ["Good evening sir. I presume it's time for you to start working on relevant stuff.", "Good evening, sir."]
        gnfinal= random.choice(gn)
        print(gnfinal + " "+ "How may I be of assistance")
        speak(gnfinal +" "+ "How may I be of assistance")
        instruction()




def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = r.listen(source)
        statement = r.recognize_google(audio_data, language='en-in')
        statement = statement.lower()
        return statement






def wantsomemore():
    speak("Would you like for me to do anything else, sir?")
    instruction()



def instruction():
    statement = listen()
    if "search the internet" in statement or "search the web" in statement:
        statement = statement.replace("search the web for", "")
        app_id ='TWY23A-XEGUYPYJ5E'
        client = wolframalpha.Client(app_id)
        res = client.query(statement)
        answer = next(res.results).text
        speak(answer)
        print(answer)
        wantsomemore()

    elif 'who are you' in statement :
        speak("I am RTB, Mark 3. A personal assistant made by Master Sarim for non-commercial use. The RTB in my name is an acronym for road to brilliance. I hope to help you out in any way possible.")
        wantsomemore()

    elif statement=="nothing" or "no" in statement:
        speak("RTB shutting down. Until next time, sir.")
        print("RTB shutting down.")
        exit()

    elif "calculate" in statement or "calculation" in statement :
        app_id ='TWY23A-XEGUYPYJ5E'
        client = wolframalpha.Client(app_id)
        statement = statement.replace("calculate" or "calculation" or "what is" or "what's", "")
        print(statement)
        res = client.query(statement)
        answer = next(res.results).text
        speak(answer)
        print(answer)
        wantsomemore()

    elif "join french" in statement:
        wb.open_new_tab("https://meet.google.com/nwa-bypz-tcg?pli=1&authuser=1")
        speak("You have joined french, sir. Heta ma'am is waiting.")
        wantsomemore()


    elif "join common" in statement:
        wb.open_new_tab("https://meet.google.com/cue-qifo-qzx?authuser=1")
        speak("You have joined the common url, sir. Click on Join Now if you wish to join the meeting.")
        wantsomemore()

    elif "open classroom" in statement:
        wb.open_new_tab("https://classroom.google.com/u/1/c/MzQ3NDc3NzY5NjE5")
        speak("Google classroom for your school is now open, sir.")
        wantsomemore()

    elif "join JD" in statement:
        wb.open_new_tab("https://us02web.zoom.us/j/9235590223?pwd=SWVxUnJLQzV2aHk2V0JIRUkvV3MyZz09")
        speak("The link to your Jd's class is open now. Allow it to open zoom if you wish to join the meeting, sir.")
        wantsomemore()
    elif "join math" in statement:
        wb.open_new_tab("https://meet.google.com/pcf-xnzv-qjw?pli=1&authuser=1")
        speak("You have joined math. Ankit sir is waiting, sir.")
        wantsomemore()

    elif "weather" in statement:
            api_key="8116deb220337a70e7ecab4e9f25b391"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=listen()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_temperature = round(current_temperature - 273)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celcius unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celcius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                wantsomemore()

    elif "join bst" in statement or "join business studies" in statement:
        wb.open_new_tab("https://meet.google.com/zch-zkdu-evq?pli=1&authuser=1")
        speak("You have joined BST. Mansi ma'am is waiting. I hope you did your homework, sir.")


    elif "time" in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime} , sir")
        wantsomemore()

    elif statement == "" or " "== statement:
        speak("I'm sorry, I do not understand. Did you say")
        print("Pardon, did you say" , statement)
        speak(statement)
        wantsomemore()

    else :
        speak("I'm sorry, I do not understand. Did you say")
        print("Pardon, did you say" , statement)
        speak(statement)
        wantsomemore()

greeting()
