from utils import process_item

while True:
    n=input()
    if n == 'q':
        break 
    print(process_item(int(n)))