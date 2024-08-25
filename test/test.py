import random

random.seed(random.randint(1, 100000))

with open('F:/Python/test/hello.txt', 'a') as f:
    f.write(f'{str(random.randint(1, 49))}\n')