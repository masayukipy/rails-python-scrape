import time

from utils.google import Google
from utils.yahoo import Yahoo
from utils.base import Base
import threading


def run_google(word):
    print(word, "google")
    google_result = Google().run(word)

def run_yahoo(word):
    print(word, "yahoo")
    yahoo_result = Yahoo().run(word)
    

while True:
    word_list = Base().get_word()
    # word_list = [1,2,3,4,5,6,7,8,9,9,2]
    print(word_list)
    break
    google_yahoo_thread = []
    for word in word_list:
        google_yahoo_thread.append(threading.Thread(target = run_google, args=(word,)))
        google_yahoo_thread.append(threading.Thread(target = run_yahoo, args=(word,)))

    for th in google_yahoo_thread:
        th.start()

    for th in google_yahoo_thread:
        th.join()
        
        
# Google().run("Python Scrapping")
# Yahoo().run("Ruby on Rails")

