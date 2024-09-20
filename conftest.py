import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # Configure ChromeOptions to run headless and with no sandbox for CI environment
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # This make Chromium reachable
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems
    chrome_options.add_argument("start-maximized")  # Starts Chrome maximized to avoid resolution issues
    chrome_options.add_argument(
        "disable-infobars")  # Disables the "Chrome is being controlled by automated test software" infobar
    chrome_options.add_argument("--disable-extensions")  # Disables existing extensions
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
