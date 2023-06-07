# imports:
from __future__ import print_function
from pydub import AudioSegment
from pydub.playback import play
import pywhatkit as kit  # pip install pywhatkit
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
import yagmail  # pip install yagmail
import wolframalpha  # pip install wolframalpha
from datetime import datetime  # built into python
import imaplib  # built into python
import traceback  # built into python
import email  # pip install
from pyttsx3 import *
from newspaper import fulltext
import newspaper
from functools import lru_cache
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import threading
import time as t
import language_tool_python
import nltk
from nltk.corpus import stopwords
import requests
from adafruit_servokit import ServoKit
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import os
import subprocess
def move(channel, inc, speed, angle):
    angle = angle+1
    i = 0
    i = int(kit.servo[channel].angle) + 1
    while not i == angle:
        kit.servo[channel].angle=i
        sleep(speed)
        i = i+inc
        print(i)
def stand():
    kit.servo[0].angle=90
    kit.servo[1].angle=90
    kit.servo[2].angle=90
    kit.servo[3].angle=130
    kit.servo[4].angle=90
    kit.servo[5].angle=130
    kit.servo[10].angle=70
    kit.servo[11].angle=90
    kit.servo[12].angle=10
    kit.servo[13].angle=90
    kit.servo[14].angle=90
    kit.servo[15].angle=90
def wave():
    kit.servo[2].angle=180
    sleep(1)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=90
    sleep(0.5)
    kit.servo[2].angle=90
def step1():
    move(12, 1, 0.025, 30)
    move(5, 1, 0.005, 145)
    move(4, 1, 0.005, 135)
    move(12, -0.5, 0.025, 10)
def step2():
    move(4, -1, 0.0001,90)
    move(5, -1, 0.0001, 130)
    move(3, 0.5, 0.01, 150)
    move(11, -1, 0, 55)
    move(10, -1, 0, 40)
    move(3, -0.5, 0.01, 130)

def step3():
    move(11, 1, 0.0001, 90)
    move(10, 1, 0.0001,70)
    move(12, 0.5, 0.01, 30)
    move(4, 1, 0, 130)
    move(5, 1, 0, 155)
    move(12, -1, 0.01, 10)
def i_know():
    speak("I know!")
    kit.servo[2].angle=180
    sleep(0.3)
    kit.servo[1].angle=45
    sleep(1)
    kit.servo[1].angle=90
    sleep(0.3)
    kit.servo[2].angle=90
def ok():
    kit.servo[0].angle=135
    sleep(1)
    kit.servo[0].angle=90
def shake():
    kit.servo[0].angle=135
    sleep(1)
    kit.servo[0].angle=90


API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
headers = {"Authorization": "Bearer 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"}
from gradio_client import Client

client = Client("https://billbojangeles2000-bart-large-cnn-samsum.hf.space/")
def balls(payload):
    result = client.predict(
        payload,  # str  in 'Input' Textbox component
        api_name="/predict"
    )
    return result
output = balls("tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.")
print(output)

def countdown(query):
    global my_timer
    URL = "https://www.google.co.in/search?q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time4timer = soup.find(jsname="VQs5Rb").text.replace("h", " Hour ").replace("m", " minute ").replace("s", " seconds ").split()
    time4timer.pop(5)
    time4timer.pop(4)
    if "00" in time4timer[0]:
        time4timer.pop(0)
        time4timer.pop(0)
        if "00" in time4timer[0]:
            time4timer.pop(0)
            time4timer.pop(0)
    queryy = str(time4timer).replace("[", "").replace("'", "").replace(",", "").replace("]", "")
    #print(queryy)
    URL = "https://www.google.co.in/search?q=" + "Convert " + queryy + " to seconds"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time = soup.find(id="NotFQb")
    #print(time)
    timer = str(time)
    #print(timer)
    timey = timer.split(" ")
    time4timer = int(timey[9].replace('"', "").replace("/", "").replace(">", "").replace("value=", ""))
    my_timer = time4timer
    #print(time4timer)
    #countdown_thread = threading.Thread(target=countdown, args=(query))
    #countdown_thread.start()
    while time4timer > 1:
        time4timer -= 1
        t.sleep(1)
    speak("beep, beep, your timer has rung")
@lru_cache(100)
def recipie(query):
    URL = "site:spendwithpennies.com " + query
    for i in search(URL, tld="com", num=1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
            }
        page = requests.get(str(i), headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ingredients = soup.find("div", class_="wprm-recipe-ingredient-group").text
        speak_ingredients = ingredients.split("¢")
        recipie = soup.find("div", class_="wprm-recipe-instruction-group").text
        speak_recipie = recipie.split(".")
        print(ingredients)
        print(recipie)
        i = 0
        while i < len(speak_ingredients):
            i = i + 1
            speak("Here is the ingredents you will need. If you want when, just ask!")
            Next = take_command()
            while not "Bob" in Next:
                Next = take_command()
            speak(speak_ingredients[i])
        i = 0
        while i < len(speak_recipie):
            i = i + 1
            speak("Here is the recipe. Once you've completed a step, ask me and I'l go to the next one")
            Next = take_command()
            while not "Bob" in Next:
                Next = take_command()
            speak(speak_ingredients[i])
        speak("congrat's, you've made it!")
@lru_cache(100)
def stock_price(query):
   try:
        user_query = query

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if datetime.now().strftime('%I:%M %p') > '9:30' and datetime.now().strftime('%I:%M %p') < '4:00':
            stockprice = soup.find("span", jsname='vWLAgc').text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="rfaVEf").text
            UOD = soup.find("span",jsname="qRSVye").text
            #print(UOD)
            if UOD > "0":
                speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent)
            else:
                speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)


            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent + " from last friday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)
        else:
            stockprice = soup.find("span", jsname="wurNO").text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="sam3Lb").text
            UOD = soup.find("span", jsname="TmYleb").text
            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from last friday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from last friday")
            else:
                if "+" in UOD:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from yesterday")
                else:
                    speak("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from yesterday")
   except Exception:
        speak("Im sorry, I could not get the price for that stock")
@lru_cache(100)
def spelling(query):
    try:
        user_query = query.replace("search up", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        spelling = soup.find(class_='MiCl6d').get_text().replace("·", ",   ")
        s1 = spelling.replace(",   ", "")
        speak(s1 + " is spelled " + spelling)
        print((s1 + " is spelled " + spelling))
        print(s1 + " is spelled " + s1)
    except Exception:  # and result == "" or Exception and result == "":
        speak("Im sorry, I could not find how to spell your word")


def search_query(query):
    try:
        CANS = []
        user_query = query.replace("search up", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        answer = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
        CANS.append(answer)
        print("1")
    except Exception:  # and result == "" or Exception and result == "":
        CANS.append("")

    try:

        result = soup.find(class_='di3YZe').get_text()
        CANS.append(result)
        print("2")
    except Exception:
        CANS.append("")  # and result == "" or Exception and result == "":
    try:
        #
        result = soup.find(class_='kno-rdesc').get_text()
        CANS.append(result)
        print("3")
    except Exception:
        CANS.append("")

    try:
        result = soup.find(class_='BbbuR uc9Qxb uE1RRc').get_text()
        CANS.append(result)
    except Exception:
        CANS.append("")
    text = ' '.join(CANS)
    summary = balls(text)
    speak(summary)
@lru_cache(100)
def read_email(key, value):
    try:
        imapClient = imaplib.IMAP4_SSL(SMTP_SERVER)
        print("\nLogging in...")

        imapClient.login(FROM_EMAIL, FROM_PWD)
        print("\nLog-in successfull!")

        imapClient.select("inbox")
        print("\nReading mailboxes...")

        if (key == None or value == None):
            type, searchResult = imapClient.search(None, "UNSEEN")
            print("\nTotal search emails count:" + str(len(searchResult[0])))

        elif (key != None and value != None):
            type, searchResult = imapClient.search(None, "(" + key + " " + value + ")")
            print("\nTotal search emails count:" + str(len(searchResult[0])))

        for resultCount in searchResult[0].split():
            typ, messages = imapClient.fetch(resultCount, "(RFC822)")

            for message in messages:
                if isinstance(message, tuple):
                    msg = email.message_from_bytes(message[1])
                    email_to_id = msg["to"]
                    email_from_id = msg["from"]
                    email_cc_id = msg["cc"]
                    email_bcc_id = msg["bcc"]
                    email_subject = msg["subject"]
                    email_body = msg["body"]
                    print("\nTo: " + str(email_to_id))
                    print("\nFrom: " + str(email_from_id))
                    print("\nSubject: " + str(email_subject))
                    print("\nBody: " + "".join([part.get_payload() for part in msg.walk()][1]).replace("\r","").replace("\n"," "))
                    speak("\nTo: " + str(email_to_id))
                    speak("\nFrom: " + str(email_from_id))
                    speak("\nSubject: " + str(email_subject))
                    speak(
                        "\nBody: " + "".join([part.get_payload() for part in msg.walk()][1]).replace("\r", "").replace(
                            "\n", " "))

                break

    except Exception as e:
        print("\nException handled: " + str(e))
        print("\nException details:")
        traceback.print_tb(e.__traceback__)
# Take command function
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("recognising")
        start_time = datetime.now()
        query = r.recognize_google(audio)
        #query = r.recognize_wit(audio, "OSTS5W57Q2YWAYJQHOI6CUQDTW37FICQ")
        end_time = datetime.now()
        print(end_time - start_time)
        print("user said: " + query + "\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
@lru_cache(100)
def send_whatsapp_message(qeury):
    if "dad" in query:
        speak("Whats the message")
        message = take_command()
        speak("Sending message...")
        kit.sendwhatmsg_instantly("+19783056153", message)
        print("Message sent successfully!")
    speak("Who should I text?")
    receiver = take_command()
    if "Dad" in receiver or "dad" in receiver:
        speak("Whats the message")
        message = take_command()
        speak("Sending message...")
        kit.sendwhatmsg_instantly("+19783056153", message)
        print("Message sent successfully!")
@lru_cache(100)
def play_song(song):
    song = song.replace('play', '')
    speak('playing ' + song)
    kit.playonyt(song)
@lru_cache(100)
def wikipedia_search(wiki_query):
    speak("searching in wikipedia..")
    query = wiki_query.replace("tell me about", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to Wikipedia")
    print(results)
    speak(results)
@lru_cache(100)
def time():
    time = datetime.now().strftime('%I:%M %p')
    speak('Current time is ' + time)
    print('Current time is ' + time)
@lru_cache(100)
def joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)
@lru_cache(100)
def remember():
    speak("What should I remember")
    print("What should I remember")
    rememberMessage = take_command()
    speak("you said me to remember : " + rememberMessage)
    print("you said me to remember : " + rememberMessage)
    remember = open('data.txt', 'w')
    remember.write(rememberMessage)
    remember.close()
@lru_cache(100)
def recall_remember():
    remember = open('data.txt', 'r')
    speak("you said me to remember that : " + remember.read())
    print("you said me to remember that : " + remember.read())
@lru_cache(100)
def weather(query):
    URL = 'https://www.google.co.in/search?q=' + str(query.replace(" ", "+")) + "/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    s1 = soup.find(class_='wob_loc q8U8x').get_text()
    s2 = soup.find(class_='wob_dcp').get_text()
    s3 = soup.find(class_='wob_t q8U8x').get_text()
    speak("In " + s1 + ", its " + s2 + " and its " + s3 + " Degree's fahrenheit")
    print("In " + s1 + ", its " + s2 + " and its " + s3 + " Degree's fahrenheit")
@lru_cache(100)
def send_email():
    speak("Who should I send the message to?")
    to_email = take_command()
    if "dad" in to_email or "Dad" in to_email:
        yag = yagmail.SMTP("thestockdude10@gmail.com", "pqnoalssfcodnous")
        speak("What do you want the subject to be?")
        content_subject = take_command()
        speak("What is the message?")
        content = take_command()
        yag.send('bipulkarki@gmail.com', content_subject, content)
        speak("Email sent sucessfully")
    else:
        speak("Im sorry, I cant sent that email")
@lru_cache(100)
def read_news():
    MSNBC_paper = newspaper.build('https://www.msnbc.com/')
    for article in MSNBC_paper.articles:
        articleurl = article.url
        html = requests.get(articleurl).text
        text = fulltext(html)
        text = text.replace("'", "")
        speak("Here is the latest news")
        print("Here is the latest news")
        print(text)
        speak("Would you like me to read it?")
        print("Would you like me to read it?")
        yN = take_command()
        if "yes" or 'Yes' in yN:
            speak(text)
        else:
            speak("Ok, no problem")
@lru_cache(100)
def math(query):
    try:
        user_query = query.replace("math", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        answer = soup.find(class_='XH1CIc').get_text() + soup.find(class_='fB3vD').get_text()
        speak(answer)
        print(answer)
    except Exception:  # and result == "" or Exception and result == "":
        speak("Sorry, I dont have a answer to that math question")
@lru_cache(100)
def definition(query):
        query = query.replace("tell me the definition", "")
        query = query.replace("max", "")
        query = ("definition of " + query)
        client = wolframalpha.Client("32R5H7-G5KG3RU4YQ")
        res = client.query(query)
        output = next(res.results).text
        speak("Here's the definition of " + query)
        print("Here's the definition of " + query)
        print(output)
        speak(output)
@lru_cache(100)
def speak(text):
    voice = "slt"  # Replace with the desired voice identifier
    subprocess.run(["flite", "-voice", voice, "-t", text])
print("initialising QUANDALE DINGLE'S GOOFY AHH MECHANICS")
global my_timer
FROM_EMAIL = "thestockdude10@gmail.com"
FROM_PWD = "pqnoalssfcodnous"
SMTP_SERVER = "imap.gmail.com"
tool = language_tool_python.LanguageToolPublicAPI('en')
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}
kit = ServoKit(channels=16)
if __name__ == "__main__":
    stand()
    wave()
    speak("Hello. My name is SIR, pleased to meet you")
    speak("Please shake my hand")
    shake()
    speak("How may I help you?")
    
    global my_timer
    while True:
        query = take_command().lower()
        if 'walter' in query:
            query = query.replace("walter", "")
            if "walk" in query:
                speak("Ok! But just to let you know, I may fall, so hold my hand!")
                step2()
                step3()
                step2()
                step3()
                step2()
                step3()
                step2()
                step3()
                step2()
                step3()
            if "set a timer" in query:
                ok()
                speak("ok")
                countdown_thread = threading.Thread(target=countdown, args=[query])
                countdown_thread.start()
                speak("Your timer has been set!")
            elif 'play' in query:
                ok()
                speak("ok")
                play_song(query)
            elif ' time ' in query or " time " in query:
                ok()
                speak("ok")
                i_know()
                time()
            elif 'joke' in query:
                ok()
                speak("ok")
                i_know()
                joke()
            elif 'search up' in query:
                ok()
                speak("ok")
                i_know()
                search_query(query)
            elif 'remember something' in query:
                ok()
                speak("ok")
                i_know()
                remember()
            elif 'do you remember anything' in query:
                ok()
                speak("ok")
                i_know()
                recall_remember()

            elif "weather" in query:
                if not "search up" in query:
                    ok()
                    speak("ok")
                    i_know()
                    weather(query)

            elif "email" in query:
                if not 'read' in query:
                    if 'send' in query:
                        ok()
                        speak("ok")
                        i_know()
                        send_email()
            elif "who are you" in query:
                    # if "Max" in query:
                    
                    speak(
                        "I am SIR, an robot made my Sansar Karki. I use manny github repositaries such as Gladiator07/JARVIS, RahulSharma4329's AI-Assistant-Helena, and manny python libraries such as speech reognition, pyttsx3, datetime, wikipedia, pyjokes, pywhatkit, webbrowser, requests and ya-gmail. These libraries allow me to do manny things.")
                    
            elif "hello" in query or "Hello" in query:
                    # if "Max" in query:
                    speak("Hello")
                    wave()
                    speak("How are you doing?")

            elif "questions about you" in query:
                    # if "Max" in query:
                    speak("Ok!")
                    ok()
                    speak("I love questions. What are the questions?")
            elif "what can you do" in query:
                    # if "Max" in query:
                    speak(
                        "I can tell you the weather, tell you the news, search somthing up for you, remember stuff, tell you a joke, search something on wikipedia, send a email, play a song on youtube, tell you the time, and more. I will become even smarter as I am coded with even more updates!")
                    print(
                        "I can tell you the weather, tell you the news, search somthing up for you, remember stuff, tell you a joke, search something on wikipedia, send a email, play a song on youtube, tell you the time, and more. I will become even smarter as I am coded with even more updates!")
            elif "you are very smart" in query:
                    # if "Max" in query:
                    speak("thanks, I like compliments. Humans do too.")
                    print("thanks, I like compliments. Humans do too.")
            elif "pause" in query:
                    # if "Max" in query:
                speak("Ok, pausing")
                time.sleep(10)
            elif "news" in query:
                ok()
                speak("ok")
                read_news()

            elif "math" in query:
                    if not "search up" in query:
                        ok("ok")
                        math(query)
            elif "tell me the definition of" in query:
                ok()
                speak("ok")
                i_know()
                definition(query)
            elif "read" in query:
                if "email" in query:
                    if not 'send' in query:
                        ok()
                        speak("ok")
                        read_email("3", None)
            elif "text" in query:
                ok()
                speak("ok")
                send_whatsapp_message(query)
            #elif "direction" in query:
            #        speak("What is the origin")
            #        origin = take_command().replace("its", "")
            #        speak("What is the destination")
            #        destination = take_command().replace("its", "")
            #        directions(origin, destination)
            if "spell" in query:
                if not "search up" in query:
                        ok()
                        speak("ok")
                        i_know()
                        spelling(query)
            if "stock" in query or "shares" in query or "price in query" in query:
                if not "search up" in query:
                    ok()
                    speak("ok")
                    i_know
                    stock_price(query)
            if "recipe" in query:
                    ok()
                    speak("ok")
                    recipie(query)
            if 'bye' in query:
                    # if "Max" in query:
                    wave()
                    speak(
                        "happy to help, bye bye! And as always, stay true GOOFY AAAAAAHHHHHH UNCLE PRODUCTIONS QUANDALE DINGLEGE CACA PRINGLES DINGDONG")
                    print(
                        "happy to help, bye bye! And as always, stay true GOOFY AAAAAAHHHHHH UNCLE PRODUCTIONS QUANDALE DINGELEGE CACA PRINGLES DINGDONG")
                    exit()