import codecs

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

    def get_soup(self, url):
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
