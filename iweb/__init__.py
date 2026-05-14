from .etf import iweb_etf
from .investment import iweb_investment
from .mutual_fund import iweb_mutual_fund
from utils import clean_spreadsheet, get_xlsx_filepath, setup_driver, delay


def iweb_runner() -> None:
    out = get_xlsx_filepath("iweb.xlsx")
    clean_spreadsheet(out)

    driver = setup_driver(True)
    iweb_etf(driver, out)
    driver.quit()

    delay(10, 30)

    driver = setup_driver(True)
    iweb_investment(driver, out)
    driver.quit()

    delay(10, 30)

    driver = setup_driver(True)
    iweb_mutual_fund(driver, out)
    driver.quit()
