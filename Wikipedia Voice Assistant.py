import pyttsx3
import wikipedia

voice = pyttsx3.init()
search_query = input("Searching wikipedia/google: ")
result = wikipedia.summary(search_query)
print(result)
print(result)
voice.say(result)
voice.runAndWait()
