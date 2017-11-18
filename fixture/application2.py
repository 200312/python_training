from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session2 import SessionHelper2
from fixture.group2 import GroupHelper2


class Application2:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session2 = SessionHelper2(self)
        self.group2 = GroupHelper2(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

