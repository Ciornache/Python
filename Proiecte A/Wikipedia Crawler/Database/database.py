import pymongo as mongo
from pymongo import MongoClient 
import re

class Database:

    __slots__ = ('connection', 'collection', 'client')

    def connect(self):
        self.connection = MongoClient(host='mongodb://127.0.0.1:27017', connect=True)
        self.client = self.connection.get_database('World')
        self.collection = self.client.get_collection('Countries')

    def __init__(self) -> None:
        pass 

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close() 

    def addNewCountry(self, document:dict) -> None:
        self.collection.insert_one(document=document)

    def checkForCountry(self, countryName:str) -> bool:
        return self.collection.find_one(filter={'Name':countryName}) != None

    def updateCountry(self, document:dict) -> None:
        self.collection.find_one_and_replace(filter={'Name':document['Name']}, replacement=document)

    def processCountry(self, document:dict) -> None:
        if not self.checkForCountry(document['Name']):
            self.addNewCountry(document)
        else:
            self.updateCountry(document)

    def getTopTenBy(self, category:str):
        countries = list(country for country in self.collection.find(filter={}, projection={'_id':False}) if category in country.keys())
        countries.sort(reverse=True,key=lambda x:(len(x[f'{category}']), x[f'{category}'], x['Name']))
        return countries[0:10]

    def printCountries(self) -> None:
        countries = list(self.collection.find(filter={}))
        for country in countries:
            print(country)
    
    def deleteCountry(self, document:dict) -> None:
        self.collection.find_one_and_delete(filter={'Name':document['Name']})

    def reset(self) -> None:
        countries = self.collection.find(filter={})
        for country in countries:
            self.deleteCountry(country)
    
    def getCountriesByLanguage(self, lang:str) -> list[dict]:
        countries:list[dict] = self.collection.find(filter = {}, projection = {'_id':False})
        queryResponse = {}
        for country in countries:
            pattern = re.compile(f'\W*{lang}\W*')
            if 'language' in country.keys():
                if pattern.search(country['language']) != None:
                    queryResponse.setdefault(country['Name'], country)
                    queryResponse[country['Name']].pop('Name')
            
        return queryResponse
    
    def getCountriesByGovernment(self, gov:str) -> list[dict]:
        countries:list[dict] = self.collection.find(filter={}, projection={'_id':False})
        pattern = re.compile(f'\W*{gov}\W*')
        queryResponse = {}
        for country in countries:
            if 'Government' in country.keys():
                if pattern.search(country['Government']):
                    queryResponse.setdefault(country['Name'], country)
                    queryResponse[country['Name']].pop('Name')

        return queryResponse
    
    def getCountriesByTimezone(self, timeZone:str) -> list[dict]:
        countries:list[dict] = self.collection.find(filter={}, projection={'_id':False})
        queryResponse = {}
        for country in countries:
            if 'Time zone' in country.keys():
                print(timeZone, country['Time zone'])
                if timeZone in country['Time zone'].split(' '):
                    queryResponse.setdefault(country['Name'], country)
                    queryResponse[country['Name']].pop('Name')
        return queryResponse
    
    def getCountryCapital(self, country:str) -> str:
        document = self.collection.find_one(filter={'Name':country})
        if document != None and 'Capital' in document.keys():
            return document['Capital']
        else:
            return None
        
    def getCountryLargestCity(self, country:str) -> str:
        document = self.collection.find_one(filter={'Name':country})
        if document != None and 'Largest city' in document.keys():
            return document['Largest city']
        else:
            return None
    
    def getLanguageStatistics(self) -> dict:
        languages = self.collection.distinct(key='language')
        queryResponse = {}
        for lang in languages:
            count = len(list(self.collection.find(filter={'language':lang})))
            langDict = {'count':count, 
                        'percentage':count * 100 / self.collection.estimated_document_count()
                      }
            queryResponse.setdefault(lang, langDict)
        subLanguages = []
        for (key, value) in queryResponse.items():
            valid = True
            if len(key) < 5:
                subLanguages.append(key)
                continue
            
            for lang in languages:
                if key != lang and len(lang) > 5:
                    try:
                        pattern = re.compile(fr"{lang}")
                        if pattern.search(key):
                            print(key, lang)
                            valid = False
                            queryResponse[lang]['count'] += value['count']
                            queryResponse[lang]['percentage'] += value['percentage']
                    except:
                        pass

            if not valid:
                subLanguages.append(key)

        for key in subLanguages:
            queryResponse.pop(key)           

        return queryResponse

    def getCountriesByLanguage(self, language:str) -> dict:
        countries = self.collection.find(filter={}, projection={'_id':False})
        queryResponse = {language:[]}
        for country in countries:
            try:
                lang = country['language']
                pattern = re.compile(f'{language}')
                if pattern.search(lang):
                    queryResponse[language].append(country)
            except:
                pass
        return queryResponse





if __name__ == '__main__':
    with Database() as database:
        database.printCountries()
        # database.reset()