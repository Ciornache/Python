from sympy import isprime


def process_item(x:int) -> int:
    while True:
        x=x+1
        if isprime(x):
            return x
        
n=int(input())
print(process_item(n))
