import pyttsx3
import wikipedia


def search_wikipedia():
    try:
        voice = pyttsx3.init()
        search_query = input("Searching wikipedia/google: ")
        result = wikipedia.summary(search_query)
        print(result)
        voice.say(result)
        voice.runAndWait()
    except wikipedia.exceptions.DisambiguationError as e:
        print("Please provide a more specific search query.")
    except wikipedia.exceptions.PageError as e:
        print("The page you requested does not exist.")
    except Exception as e:
        print("An error occurred while searching Wikipedia.")


search_wikipedia()
