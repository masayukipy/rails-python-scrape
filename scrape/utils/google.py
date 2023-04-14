import time

from utils.base import Base


class Google(Base):
    def __init__(self) -> None:
        self.url = "https://www.google.co.jp/"

    def run(self, word):
        # self.soup = self.get_soup(self.url)
        # self.save_file("html/a.html", str(self.soup))
        # print(self.soup)
        self.driver = self.get_drive()
        self.driver.execute_script(f"document.querySelector('textarea').value = '{word}'")
        time.sleep(1)
        self.driver.execute_script(f"document.querySelector('input').click()")
        time.sleep(5)
        self.soup = self.get_soup()
        
        self.driver.close()
        return self.soup
