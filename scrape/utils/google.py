from utils.base import Base


class Google(Base):
    def __init__(self) -> None:
        self.url = "https://www.google.co.jp/"

    def run(self):
        self.soup = self.get_soup(self.url)
        self.save_file("html/a.html", str(self.soup))
        print(self.soup)
