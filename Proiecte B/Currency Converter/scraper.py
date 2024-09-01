from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
import json 


class CurrencyScraper:

    def configureDriver(self):
        self.executablePath = 'F:/Website Drivers/chromedriver-win64/chromedriver.exe'
        self.service = Service(executable_path=self.executablePath)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-search-engine-choice-screen')
        self.options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-logging')
        self.options.add_argument('--log-level=3')
        self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')

    def __init__(self) -> None:
        with open('currency_data.json', 'w') as js:
            json.dump({}, js)
        self.configureDriver()
        self.driver:Chrome = webdriver.Chrome(service=self.service, options=self.options)

    def scrapeCurrencies(self):
        self.driver.get('https://www.cursbnr.ro/')

        # Wait for Accept Button

        waitForAcceptButton = WebDriverWait(self.driver, 10)
        waitForAcceptButton.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="onesignal-slidedown-cancel-button"]')))
        acceptButton = self.driver.find_element(By.XPATH, '//button[@id="onesignal-slidedown-cancel-button"]')
        acceptButton.click()

        # Wait for Consimtamant Button

        waitForAcceptButton.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')))
        acceptButton = self.driver.find_element(By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')
        acceptButton.click()

        # Collect all the tr currency tags
        currencies:list[WebElement] = self.driver.find_elements(By.XPATH, '//table[@class="table table-striped table-lg"]/tbody/tr')

        # Extract the name, symbol and value of the currency
        for currency in currencies:
            symbol = currency.find_element(By.XPATH, 'td[1]').text
            name = currency.find_element(By.XPATH, 'td[2]/a').text
            value = currency.find_element(By.XPATH, 'td[3]').text
            currencyData = {
                'symbol': symbol, 
                'value' : value
            }

            # Update the json with the current currency 
            with open('currency_data.json', 'r') as js:
                data = json.load(js)
                data.setdefault(f'{name}', currencyData)

            with open('currency_data.json', 'w') as js:
                json.dump(data, js)
            
        with open('currency_data.json', 'r') as js:
            data = json.load(js)
            data.setdefault(f'Leu romanesc', {'symbol':'RON', 'value':'1.00'})
        
        with open('currency_data.json', 'w') as js:
            json.dump(data, js)


if __name__ == '__main__':
    scraper = CurrencyScraper()
    scraper.scrapeCurrencies()