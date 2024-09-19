from seleniumpagefactory.Pagefactory import PageFactory

class GoogleFinancePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()
    @property
    def url(self):
        return "https://www.google.com/finance"
    @property
    def title(self):
        return self.driver.title

    def navigate(self):
        self.driver.get(self.url)
