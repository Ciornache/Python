from forbes_crawler.forbes import Crawler
import os 
import time 
import forbes_crawler.constants as constants  
import threading 
import sys  
from Project.database.database import Manager 
import pymongo as mongo 

def main():
    prevLoading = None
    time.sleep(3) 
    while constants.loading < 100: 
        if prevLoading != constants.loading: 
            # os.system('cls')
            print('Processing', end='', flush=True)
            for _ in range(3):
                print('.', end='', flush=True)
                time.sleep(0.3)
            print(' ' * 10 + str(round(constants.loading, 2)) + '%', flush=True)
            prevLoading = constants.loading
    
    args = list(filter(lambda s: s[0] == '-', sys.argv))
    with Manager() as manager:
        for arg in args:
            match arg:
                case '-y':
                    print(f'The top 10 youngest billionaires are as follow')
                    billList = manager.getBillionaires(limit=10, filter=[('Age', mongo.ASCENDING), ('name', mongo.ASCENDING)])
                    for (key, values) in billList.items():
                        print(f'Bill name:{key}')
                        for key2, value2 in values.key():
                            print(f'{key2}:value2')
                case '-a':
                    print(f'The number of billionaires with American citizenship are: {manager.countAmericanBillionaires()}')
                case '-k':
                    print(f'The 10-th philantropical score belongs to: {manager.getKthPhilantropicalScore(10)}')

def crawl():
    crawler = Crawler()
    crawler.start_requests()

if __name__ == '__main__':

    thread = threading.Thread(target=main)
    thread2 = threading.Thread(target=crawl)
    
    thread.daemon = True
    thread2.daemon = True
    
    thread.start()
    thread2.start()    
    thread.join()
    thread2.join()