# string concatenation (aka how to put stings together)
# suppose we want to create a string that says "subscribe to ____"
from sample_madlibs import hp, code, zombie, hungergames
import random

youtuber = ""   # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}.format(youtuber))
# print (f"subscribe to {youtuber}"}

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}!  It makes me so excited all the time because " \
         f"I love to {verb1}.  Stay hydrated and {verb2} like you are {famous_person}!"
print(f"{madlib}")

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()