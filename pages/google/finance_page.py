from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from seleniumpagefactory.Pagefactory import PageFactory


class GoogleFinancePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def url(self) -> str:
        return "https://www.google.com/finance"

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def smart_watchlist_section(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, "section[aria-labelledby='smart-watchlist-title']")

    @property
    def smart_watchlist_stocks_links(self) -> [WebElement]:
        return self.smart_watchlist_section.find_elements(By.CSS_SELECTOR, "a[href*='/quote/']")

    @property
    def smart_watchlist_stock_symbols(self) -> [str]:
        stocks_links = self.smart_watchlist_stocks_links
        stocks = []
        for stock_link in stocks_links:
            # stock_link pattern is: stock_symbol stock_fullname price ...
            stocks.append(stock_link.text.split()[0])

        return stocks

    def navigate(self):
        self.driver.get(self.url)
