import sys
from text_to_speech import convertToMp3
import os
import stat 
import re 
import functools

input_directory = sys.argv[1]
output_directory = sys.argv[2]

def traverseFolder(input_directory:str, output_directory:str) -> None:
    global size 
    statResult = os.stat(input_directory)
    if stat.S_ISDIR(statResult.st_mode):
        for folder in os.listdir(input_directory):
            traverseFolder(f'{input_directory}/{folder}', output_directory)
    else:
        with open(input_directory, 'r') as f:
            text:str = f.read()
            p = re.compile(r"[a-zA-z0-9\s\-\']+.")
            filteredLine = p.findall(text)
            for sentence in filteredLine:
                size = size + 1
                convertToMp3(sentence, output_directory, size)

def getIndex(directory:str) -> int:
    
    statResult = os.stat(directory)
    if not stat.S_ISDIR(statResult.st_mode):
        return 0
    maxi = 0
    for dir in os.listdir(directory):
        p = re.compile(r'\d+')
        if p.search(dir):
            obj = p.search(dir).group()
            maxi = max(int(obj), maxi)
    return maxi

if __name__ == '__main__':
    size = os.stat(output_directory).st_size
    traverseFolder(input_directory, output_directory)
    print(getIndex(output_directory))
