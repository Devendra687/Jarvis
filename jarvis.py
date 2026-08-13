import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliab
from google import genai
from AppOpener import open
import pyautogui
from datetime import datetime

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(text)


def aiprocess(command):
    client = genai.Client(
        api_key=""
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=[
            "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant. Keep answers short and helpful.",
            command,
        ],
    )

    return response.text




def processcommand(c):

    # for yt search
    if c.lower().startswith("search"):
        query = c.lower().replace("search", " ").strip()
        url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
        webbrowser.open(url)
    # for screenshot
    elif "take a screenshot" in c.lower():
        name = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
        pyautogui.screenshot(name)
        speak("Screenshot taken sir")
        # open websites
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open snap" in c.lower():
        webbrowser.open("https://snapchat.com")
        # app opening
    elif c.lower().startswith("open"):
        app = c.lower().replace("open", " ").strip()
        open(app)
        # for music
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", " ").strip()
        if song in musicliab.music:
            link = musicliab.music[song]
            print("Opening:", link)
            webbrowser.open(link)
        else:
            speak("Song not found")
    else:
        # let open ai handel the request
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "jarvis"
        r = sr.Recognizer()

        print("recoginzing....")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Say something!")
                r = recognizer
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio).lower().strip()
            print("Heard:", word)
            if word.lower() == "jarvis":
                speak("yess boss")
                # listen for command
                with sr.Microphone() as source:
                    print(word)
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processcommand(command)
        except sr.UnknownValueError:
            print("😕 Could not understand.")

        except sr.WaitTimeoutError:
            print("⌛ Listening timed out.")

        except sr.RequestError:
            print("🌐 Internet problem.")

        except Exception as e:
            print("Error:", e)
