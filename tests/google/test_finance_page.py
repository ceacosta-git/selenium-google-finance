import pytest

from pages.google.finance_page import GoogleFinancePage


@pytest.fixture(scope="class")
def in_google_finance_page(setup):
    print("called in_google_finance_page")
    driver = setup
    finance_page = GoogleFinancePage(driver)
    finance_page.navigate()
    yield finance_page


@pytest.mark.usefixtures("setup", "in_google_finance_page")
class TestGoogleFinancePage:

    @staticmethod
    def get_expected_stock_symbols():
        return ["NFLX", "MSFT", "TSLA"]

    def test_page_loads(self, in_google_finance_page):
        finance_page = in_google_finance_page
        expected_title = "Google Finance"
        assert expected_title in finance_page.title, f"Google Finance page title does not contain {expected_title}"

    def test_retrieve_smart_watchlist_stock_symbols(self, in_google_finance_page):
        finance_page = in_google_finance_page

        expected_smart_watchlist_section = 'You may be interested in'

        assert expected_smart_watchlist_section in finance_page.smart_watchlist_section.text, \
            f"Unable to find section: {expected_smart_watchlist_section}"

        assert finance_page.smart_watchlist_stock_symbols != [], \
            "Unable to retrieve stock symbols from smart watchlist."

    @pytest.mark.parametrize("expected_stock", get_expected_stock_symbols())
    def test_stock_is_in_smart_watchlist(self, expected_stock, in_google_finance_page):
        finance_page = in_google_finance_page

        assert expected_stock in finance_page.smart_watchlist_stock_symbols, \
            f"Unable to find stock symbol {expected_stock} in smart watchlist."

    @pytest.mark.print_differences
    def test_print_stock_symbols_not_in_expected(self, in_google_finance_page):
        finance_page = in_google_finance_page

        actual_stocks = set(finance_page.smart_watchlist_stock_symbols)
        expected_stocks = set(TestGoogleFinancePage.get_expected_stock_symbols())

        stocks_not_in_expected = actual_stocks.difference(expected_stocks)
        print(f"Listed stocks not in given test data: {stocks_not_in_expected}")
        assert stocks_not_in_expected is not None, "Unable to print stocks not in given test data"

    @pytest.mark.print_differences
    def test_print_expected_stock_symbols_not_in_smart_watchlist(self, in_google_finance_page):
        finance_page = in_google_finance_page

        actual_stocks = set(finance_page.smart_watchlist_stock_symbols)
        expected_stocks = set(TestGoogleFinancePage.get_expected_stock_symbols())
        stocks_not_in_watchlist = None
        stocks_not_in_watchlist = expected_stocks.difference(actual_stocks)
        print(f"Expected stocks not in smart watchlist: {stocks_not_in_watchlist}")
        assert stocks_not_in_watchlist is not None, "Unable to print stocks not in smart watchlist"
