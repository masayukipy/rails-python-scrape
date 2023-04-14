import re
from datetime import datetime
from calendar import monthrange
import random
import codecs
import sqlite3
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Base:
    
    def __init__(self) -> None:
        pass

    def save_file(self, path_name: str, text: str):
        try:
            f = codecs.open(path_name, mode="wb", encoding="utf-8")
            f.write(text)
            f.close()
            return True
        except: # noqa
            return False

    def run(self, url):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')       
        options.add_argument("--window-size=800,5000")
        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        driver.get(url)
        _soup = BeautifulSoup(driver.page_source, features="html.parser")
        driver.close()
        return _soup

    def random_date(self, year, month):

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

        days_in_month = monthrange(year, month)[1]

        day = random.randint(1, days_in_month)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        random_date = datetime(year, month, day, hour, minute, second)
        return random_date
        

    def get_word(self):
        root_path = re.findall("(.+)\\\\scrape", str(Path().resolve()))[0]
        db_path = f"{root_path}/db/development.sqlite3"
        print(db_path)
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        # cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # print(cur.fetchall())
        query = f"SELECT * FROM rundates WHERE date < '{datetime.now()}';"
        resp = cur.execute(query)
        id_word_id_list = [[x[0], x[1]] for x in resp]

        update_id_list = [x[0] for x in id_word_id_list]
        id_list = set([x[1] for x in id_word_id_list])

        con.close()
       

        # return
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        if not id_list:
            return []

        query2 = "SELECT * FROM keywords WHERE "
        
        for id in id_list:
            query2 += f"id = {id} OR "

        query2 = query2[:-4]

        resp2 = cur.execute(query2)
        word_list = [x[1] for x in resp2]

        con.close()

        
        # update
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        update_query = ""
        for x in update_id_list:
            update_query += f"UPDATE rundates SET date = '{self.random_date(cur_year, cur_month)}' WHERE id = {x};"
        con.executescript(update_query)

        con.close()

        return word_list
