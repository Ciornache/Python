from pymongo import MongoClient 
from pymongo.write_concern import WriteConcern 
import pymongo as mongo

class Manager:
    __slots__ = ('client',  'db', 'collection', 'dbName', 'collectionName')
    def __init__(self) -> None:
        self.dbName = 'Forbes'
        self.collectionName = 'Billionaires'

    def __enter__(self) -> None:
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[self.dbName]
        self.collection = self.db[self.collectionName]
        return self 
    
    def __exit__(self, type, value, traceback) -> None:
        self.client.close()

    def checkForBillionaire(self, billInfo:dict) -> int:
        return self.collection.count_documents(filter={'name':billInfo['name']}) > 0

    def updateBillionaire(self, billInfo:dict) -> None:
        self.collection.replace_one(filter = {'name':billInfo['name']}, replacement=billInfo)

    def addBillionaire(self, billInfo:dict) -> None:
        self.collection.insert_one(billInfo)

    def process(self, bills:list[dict]) -> None:
        
        print(bills)

        documents:list[dict] = self.collection.find({})

        for document in documents:
            document.update({'updated': 0 })
            self.updateBillionaire(document)
        
        for bill in bills:
            bill.setdefault('updated', 1)
            self.updateBillionaire(bill) if self.checkForBillionaire(bill) else self.addBillionaire(bill)
        
        filteredDocumentList = list(filter(lambda s: not s['updated'], self.collection.find({})))
        for document in filteredDocumentList:
            self.deleteBillionaire(document)
        
        print('Finished processing')

    def deleteBillionaire(self, billInfo:dict) -> None:
        self.collection.find_one_and_delete(filter = {'name':billInfo['name']})
    
    def reset(self):
        for document in self.collection.find(filter={}):
            self.deleteBillionaire(document)
    
    def printBillionaires(self):
        bills = self.collection.find(filter={})
        for (id,bill) in enumerate(bills):
            print(f'Billionaire {id}', bill)
        bills.close()
    
    def getBillionaire(self, name:str):
        cursor = self.collection.find(filter={'name':name})
        for element in cursor:
            bill = element 
        return bill

    def getBillionaires(self, limit:int, filter:list) -> list:
        return list(self.collection.find(filter={}).limit(limit).sort(filter=filter))

    def countAmericanBillionaires(self) -> int:
        return [bill for bill in self.collection.find({}) if bill['Citizenship'] == 'United States'].count()
    
    def getKthFPhilantropicalScore(self, limit:int) -> list:
        bills:list[dict] = self.collection.find(filter = {})
        scores = sorted([value['Philanthropy Score'] for bill in bills for value in bill.values() if 'Philantropy Score' in value.keys()], reverse = True)
        if len(scores) < limit:
            return None 
        return scores[limit - 1]


def main():
    
    # bills = [{'name':'Whatever', 'fortune':'1.97 trillion'}, {'name':'Other', 'fortune':'something'}]
    # Context Manager

    # __enter__ -> Allocates resources for the object and creates the connection to the database 
    # __exit__ -> Closes the connection to the database

    with Manager() as manager:
        # manager.process(bills)
        # manager.reset()
        manager.printBillionaires()
        pass 


if __name__ == '__main__':
    main()