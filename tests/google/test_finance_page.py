import pytest
from pages.google.finance_page import GoogleFinancePage

@pytest.mark.usefixtures("setup")
class TestGoogleFinancePage:
    def test_page_loads(self):
        finance_page = GoogleFinancePage(self.driver)
        finance_page.navigate()
        expected_title = "Google Finance"
        assert  expected_title in finance_page.title, f"Google Finance page title does not contain {expected_title}"

