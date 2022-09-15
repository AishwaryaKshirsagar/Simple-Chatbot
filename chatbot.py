import speech_recognition as sr # to recognise voice
import pyttsx3 # to convert speech to text
import datetime # to get the current date
import wikipedia

listener = sr.Recognizer() 
engine = pyttsx3.init() # initialize
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # to get the type of voice we want(here female voice).

def talk(text): # function for answering the questions
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source: # getting our voice as source
        print('listening...')
        voice = listener.listen(source) # getting the voice in a variable
        command = listener.recognize_google(voice) # getting the voice stored in a variable in text format
        command = command.lower()
        print('You: '+ command)
        return command

def run_alexa():
    command = take_command()
    if 'hello' in command:
        talk('hello! I am Alexa')
        print('hello! I am Alexa!')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        now = 'Current time is: '+ time
        talk(now)
        print(now)

    elif 'your name' in command:
        status = "My name is Alexa"
        talk(status)
        print(status)
    
    elif 'who is' in command: # information about a person
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2, auto_suggest=False)
        print(info)
        talk(info)
    
    elif 'what is' in command: # general information 
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 2, auto_suggest=False)
        print(info)
        talk(info)
    
    elif 'bye' in command:
        talk('Good Bye! Have a nice day.')
        print('Good Bye! Have a nice day.')
    
    else:
        print('Please say the command again!')

run_alexa() # call the function
