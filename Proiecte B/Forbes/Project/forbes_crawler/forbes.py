import logging.config
import logging.handlers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .constants import executablePath, bufferJsonPath, billJsonPath
import forbes_crawler.constants as constants 
from database.database import Manager 
import json 
import logging

class Crawler:

    __slots__ = ('driver', 'service', 'options', 'bill_urls', 'information', 'logger', 'bl')

    def loadLoggingConfiguration(self):
        with open('F:\\Python\\Forbes\\Project\\config.json', 'r') as f:
            config = json.load(f)
        logging.config.dictConfig(config)

    def configure(self):

        global ips 

        self.service = Service(executable_path=executablePath)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-search-engine-choice-screen')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--headless=new')
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-logging')
        self.options.add_argument('--log-level=3')

        self.loadLoggingConfiguration()

    def __init__(self):

        self.configure()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get('https://www.forbes.com/billionaires/')

        self.information = {}
        self.bill_urls, self.bl = [], []
        self.logger = logging.getLogger(__name__)
    
    
    def start_requests(self):

        # Wait for acces button

        self.logger.info('Waiting for the acces button to appear on the screen')

        wait = WebDriverWait(driver=self.driver, timeout=20)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Accept All"]')))
        acceptButton = self.driver.find_element(By.XPATH, '//button[@aria-label="Accept All"]')
        acceptButton.click()

        self.logger.info('Clicked the accept button')

        # Wait for the billionaires information

        constants.loading = 5

        self.logger.info('Waiting for the billionaires information to render')

        wait = WebDriverWait(driver=self.driver, timeout=20)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="Table_personName__Bus2E"]')))
        bills:list[WebElement] = self.driver.find_elements(By.XPATH, '//div[@class="Table_personName__Bus2E"]')
        bills:list[str] = [bill.text for bill in bills]

        self.logger.info('Collected all the billionaire links')

        for (id, bill) in enumerate(bills):
            if '&' in bill:
                bills[id] = bill.split('&')[0][0:-1:1]

        sep = [',', '.']
        for s in sep:
            bills = list(map(lambda x: x.replace(s, ''), bills))
        
        self.logger.info('Querying...')

        with Manager() as manager:
            self.logger.info('Filtering the billionaires...')
            registeredBill = list(filter(lambda x: manager.checkForBillionaire({'name':x.capitalize()}), ["-".join(bill.lower().split(" ")) for bill in bills]))
            billNames = list(filter(lambda x: not manager.checkForBillionaire({'name':x.capitalize()}), ["-".join(bill.lower().split(" ")) for bill in bills]))
            self.logger.info('Filtered the billionaires')
            for bill in registeredBill:
                self.bl.append(manager.getBillionaire(bill.capitalize())) 

        self.bill_urls = [f'https://www.forbes.com/profile/{name}/?list=billionaires' for name in billNames]
        constants.loading = 10
        self.logger.info('Processing the billionaires!')

        for url in self.bill_urls:
            self.parse(url)
            constants.loading += 90 / len(self.bill_urls)
            if constants.loading > 10.2:
                break 

    def parse(self, url):

        name:str = url.split('/')[4]
        try:
            self.logger.info('Checking if the current url %s is valid', url)
            self.driver.get(url)
            wait = WebDriverWait(driver = self.driver, timeout=10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//dl[@class="listuser-block"]/dl/dt')))
        except:
            self.logger.warning('The %s url is not valid', url)
            return None 
        finally:
            pass 

        self.logger.info('The url %s is valid', url)

        labels = self.driver.find_elements(By.XPATH, '//dl[@class="listuser-block"]/dl/dt') + ['Real Time Net Worth']
        values = self.driver.find_elements(By.XPATH, '//dl[@class="listuser-block"]/dl/dd') + [self.driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "profile-info__item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "profile-info__item-value", " " ))]')]
        
        labels, values = ['Real Time Net Worth' if label == 'Real Time Net Worth' else label.text for label in labels], [value.text for value in values]
    
        attributes = list(zip(labels, values))
        dictInfo:dict = {label : value for (label, value) in attributes}
        dictInfo.setdefault('name', name.capitalize())
        
        self.bl.append(dictInfo)
        self.logger.info('Collected all the information from the current url %s', url)
        

    def __del__(self):
        with Manager() as manager:
            self.logger.info('Processing the billionaires and inserting them into the Database')
            print(self.bl)
            manager.process(self.bl)


def main():
    crawler = Crawler()
    crawler.start_requests()

if __name__ == '__main__':
    main()
