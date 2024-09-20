import pytest

from pages.google.finance_page import GoogleFinancePage


@pytest.mark.usefixtures("setup")
class TestGoogleFinancePage:
    def test_page_loads(self):
        finance_page = GoogleFinancePage(self.driver)
        finance_page.navigate()
        expected_title = "Google Finance"
        assert expected_title in finance_page.title, f"Google Finance page title does not contain {expected_title}"

    def test_retrieve_smart_watchlist_stock_symbols(self):
        finance_page = GoogleFinancePage(self.driver)
        finance_page.navigate()

        expected_smart_watchlist_section = 'You may be interested in'

        assert expected_smart_watchlist_section in finance_page.smart_watchlist_section.text, \
            f"Unable to find section: {expected_smart_watchlist_section}"

        assert finance_page.smart_watchlist_stock_symbols != [], \
            "Unable to retrieve stock symbols from smart watchlist."

