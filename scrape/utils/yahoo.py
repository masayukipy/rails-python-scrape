from utils.base import Base


class Yahoo(Base):
    def __init__(self) -> None:
        self.url = "https://www.yahoo.com/"
    
    def run(self, word):
        self.driver = self.get_drive()
        self.soup = self.get_soup()
        print(self.soup)
