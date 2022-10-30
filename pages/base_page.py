class BasePage():
    def __init__(self, browser, url):
        self.broswer = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)