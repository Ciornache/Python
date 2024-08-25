import requests as http
import re 
from bs4 import Tag, NavigableString, BeautifulSoup
import unicodedata as data
from Database.database import Database
import logging
import logging.config
import json 
from Config.constants import wikiUrl

def parseCountry(url:str, connection:Database, **kwargs):

    headers, logger, options, separators = kwargs.values()
    response = http.request(url=url, headers=headers, method='GET')
    if response.status_code == 200:

        logger.info(f'Connection was established succesfully to the url: {url}')
        soup = BeautifulSoup(markup=response.content, features='html.parser')
        tableElement = soup.select_one('.infobox')

        if tableElement == None:
            logger.warning(f"The current country {url} doesn't have a valid information page")
            return None 
        
        trElements = tableElement.select('tr')
        document = {}

        for tr in trElements:
            for option in options:
                
                if option == 'language':
                    pattern = re.compile(f'Official.+{option}')
                else:
                    pattern = re.compile(f'{option}')
                areaPattern = re.compile('Area')

                if tr.th != None:
                    text = traverseHtmlTree(tr.th)
                    if areaPattern.search(text) and option == 'Area':
                        newTr = tr.find_next_sibling()
                        text = traverseHtmlTree(newTr.td)
                        document.setdefault('Total Area', text.split('\xa0km2')[0].split('[')[0].split('\xa0sq')[0])
                    elif pattern.search(text):
                        text = traverseHtmlTree(tr.td)
                        if option == 'Capital' or option == 'Largest City':
                            for i in range(0, 10):
                                text = text.split(sep=f'{i}')[0]
                        elif option == 'Density':
                            text = text.split(sep='/km2')[0].split(sep='/sq\u00a0mi')[0]
                        document.setdefault(option,text.split('[')[0])
        
        if 'Largest city' not in document.keys():
            if 'Capital' in document.keys():
                document.setdefault('Largest city', document['Capital'])
            else:
                logger.warning('Link not lead to a country. It does not have a capital')
                return None

        document.setdefault('Name', url.split('/')[-1])
        logger.info('Normalizing the information...')
        
        for key, value in document.items():
            for sep in separators:
                document[key] = value.split(sep)[0];


        logger.info('Fetching the country in the database...')
        connection.processCountry(document)
        logger.info('Country fetched succesfully!')

    else:
        logger.error('Connection was not succesful!')

def traverseHtmlTree(htmlElement):
    if type(htmlElement) != Tag:
        
        if type(htmlElement) == NavigableString:
            return htmlElement.text
        else:
            return ''
    else:
        childList = list(htmlElement.children)
        text = []
        for child in childList:
            text.append(traverseHtmlTree(child))
        return ''.join(text)


def configureLogger():
    with open('F:\Python\Proiecte A\Wikipedia Crawler\Config\\botLoggerConfig.json', 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config=config)
    logger = logging.getLogger(__name__)
    return logger

def run():

    logger = configureLogger()
    with open('F:\Python\Proiecte A\Wikipedia Crawler\Config\country-info.json', 'r') as f:
            logger.info('Reading the Country options...')
            js = json.load(f)
            options = js['info']
    
    with open('F:\Python\Proiecte A\Wikipedia Crawler\Config\separators.json', 'r') as f:
        logger.info('Reading the separators...')
        js = json.load(f)
        separators = js['sep']

    with http.Session() as sesssion:
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        response = http.request(url=wikiUrl, headers=headers,method='GET')
        if response.status_code == 200:
            logger.info(f'Connection was established succesfully to the url: {wikiUrl}')
            soup = BeautifulSoup(response.content, 'html.parser')
            tableElement = soup.select_one('.wikitable.sortable')
            anchorTags = tableElement.select('a[title]')
            with Database() as database:
                for anchor in anchorTags:
                    if anchor.parent.name != 'td' and anchor.parent.name != 'i':
                        logger.info(f'Skipping the country {anchor["href"]} for bad format')
                        continue
                    try:
                        if anchor.parent.find_previous_sibling().span.text != '-':
                            parseCountry(f'https://en.wikipedia.org/{anchor["href"]}', database, headers=headers, logger=logger, options=options, separators=separators)
                    except AttributeError:
                        parseCountry(f'https://en.wikipedia.org/{anchor["href"]}', database, headers=headers, logger=logger,options=options,separators=separators)

if __name__ == '__main__':
    run()
    