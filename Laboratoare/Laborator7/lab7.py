import random 
import time 
import math 
import os
import hashlib
import json
import stat
import zipfile

def ex1(a, b):
    start = time.time()
    while True:
        x = random.randint(a, b)
        time.sleep(x)
        now = time.time()
        minutes = (now - start) / 60
        print(f'The program is running for {int(minutes)} minutes and {round((now - start) % 60, 2)} seconds')



def ex2():

    def decorator(f):
        def wrapperFunction(*args, **kwargs):
            start = time.time()
            ok = f(args[0])
            if ok:
                print('The number is prime')
            else:
                print('The number is not prime')
            end = time.time()
            return end - start
        return wrapperFunction

    @decorator
    def isPrime(x):
        if x < 2:
            return False 
        
        if x == 2 or x == 3:
            return True

        if x % 2 == 0 or x % 3 == 0:
            return False
        
        for i in range(5, int(math.sqrt(x)) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False 
        
        return True

    @decorator
    def isPrime2(x):

        if x < 2:
            return False 
        
        if x == 2:
            return True
        
        if x % 2 == 0:
            return False 
        
        for i in range(3, int(math.sqrt(x)), 2):
            if x % i == 0:
                return False 
        
        return True
    
    time1 = isPrime(1000000000100011)
    time2 = isPrime2(1000000000100011)
    if time1 > time2:
        print('Function isPrime2 is faster than isPrime')
    elif time1 < time2:
        print('Function isPrime is faster than isPrime2')
    else:
        print('No notable difference')

def ex3(filePath1, filePath2):
    sha256 = hashlib.sha256()
    sha256v2 = hashlib.sha256()
    with open(filePath1, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256.update(data)
    
    with open(filePath2, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256v2.update(data)

    if sha256.hexdigest() == sha256v2.hexdigest():
        print('Files are identical')
    else:
        print('Files are different')

def ex4(directoryName):

    for file in os.listdir(directoryName):

        with open(f'{directoryName}\\{file}', 'rb') as f:
            data = f.read()   
            md5_file = hashlib.md5(data)
            sha256_file = hashlib.sha256(data)
            size = len(data)
            absolutePath = os.path.abspath(f'{directoryName}\\{file}')
            creationTime = time.ctime(os.path.getctime(f'{directoryName}\\{file}'))
            fileInfo = {'name':file.split('.')[0], 
                        'md5_file':md5_file.hexdigest(), 
                        'sha256_file':sha256_file.hexdigest(),
                        'Size':size,
                        'Absolute Path':absolutePath,
                        'Date created':creationTime}

    
        with open('data.json', 'r') as js:
            try:
                data = json.load(js)
            except:
                data = {}
            finally:
                data.setdefault(fileInfo['name'], fileInfo)

        print(data)

        with open('data.json', 'w') as js:
            json.dump(data, js) 
         
def ex5(folderPath, extension, name):
    try:
        zip = zipfile.ZipFile(f'{name}.zip', 'x')
    except:
        zip = zipfile.ZipFile(f'{name}.zip', 'w')
        
    for file in os.listdir(folderPath):
        ext = file.split('.')[-1]
        st = os.stat(f'{folderPath}\\{file}')
        if stat.S_ISREG(st.st_mode):
            print(ext)
            if extension == ext:
                zip.write(f'{folderPath}\\{file}')

def ex6(x):
    timeTuple = time.localtime()
    year = timeTuple[0]
    currDay = timeTuple[7]
    timeSinceEpoch = time.time()
    fullDayName = {'Sun' : 'Sunday', 
                   'Mon' : 'Monday',
                   'Thu': 'Thursday', 
                   'Tue' : 'Tuesday',
                   'Wed' : 'Wednesday',
                   'Sat' : 'Saturday',
                   'Fri' : 'Friday'}
    for i in range(0, x):
        day = time.ctime(timeSinceEpoch - currDay * 24 * 3600).split(' ')[0]
        timeTuple = time.localtime(timeSinceEpoch - currDay * 24 * 3600)
        currDay += timeTuple[7]
        print(f'The New Year Eve in the year of {year - i - 1} was in a {fullDayName[day]}')

def ex7():

    lotoNumbers = [i for i in range(1, 50)]
    winningNumbers = []
    for i in range(0, 6):
        winningNumber = random.choice(lotoNumbers)
        lotoNumbers.remove(winningNumber)
        winningNumbers.append(winningNumber)
    
    print('The winning numbers are:')
    for number in winningNumbers:
        print(number, end = '\n', sep = ',')

def ex8(a_path, to_hextract):
    if zipfile.is_zipfile(a_path):
        myzip = zipfile.ZipFile(a_path, mode='r')
        data = myzip.read(to_hextract)
        myzip.close()
        print(data)
    


if __name__ == '__main__':
    # ex1(1, 5)
    # ex2()
    # ex3('test.txt', 'test2.txt')
    # ex4("F:\\Diplome")
    # ex5('F:\Python\Laboratoare\Laborator7', 'txt', 'the')
    # ex6(30)
    # ex7()
    # ex8('F:\Python\Laboratoare\Laborator7\\arhiva.zip', 'test3.txt')
    pass      