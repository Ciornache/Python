# Problem 1.1
# import utils 


# Problem 1.2
# import app

# Problem 2

# def kwargs_sum(*args, **kwargs):
#     answer = 0
#     for key, value in kwargs.items():
#         if type(value) is int:
#             answer += value 
#     return answer

# my_function = lambda *args, **kwargs: sum(kwargs.values())
# print(my_function(1, 2, c = 1, d = 2))
# print(kwargs_sum(1, 2, c = 1, d = 2))

# Problem 3

# def listComprehension(s:str) -> list:
#     return [c for c in s if c in "aeiouAEIOU"]
# filterLambdaFunction = lambda s: list(filter(lambda c: c in "aeiouAEIOU", s))
# def myFunction(s:str) -> list:
#     l:list = []
#     for c in s:
#         if c in "aeiouAEIOU":
#             l.append(c)
#     return l 

# Problem 4
# def filterParams(*args, **kwargs):
#     return list({frozenset(a) for a in args if type(a) is dict and len(a.keys()) > 1 for k in a.keys() if type(k) is str and len(k) > 2}.union({frozenset(k) for k in kwargs.values() if type(k) is dict and len(k.keys()) > 1 for r in k.keys() if type(r) is str and len(r) > 2}))
# print(filterParams({1: 2, 3: 4, 5: 6}, 
#                    {'a': 5, 'b': 7, 'c': 'e'}, 
#                    {2: 3}, 
#                    [1, 2, 3],
#                    {'abc': 4, 'def': 5},
#                    3764,
#                    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#                    test={1: 1, 'test': True}))

# Problem 5
# def filterList(l:list) -> list:
#     return list(filter(lambda x: type(x) is int or type(x) is float, l))


# Problem 6
# def getEvenOdd(l:list) -> list:
#     return list(zip(list(filter(lambda x:not x%2, l)), list(filter(lambda x:x%2, l))))

# Problem 7
# def sum_digits(x):
#     return sum(map(int, str(x)))

# def process(**kwargs):
#     fib=[1,1];
#     [fib.append(fib[k-1]+fib[k-2]) for k in range(2, 1000)]
#     if 'filters' in kwargs.keys():
#         for l in kwargs['filters']:
#             fib=list(filter(l, fib))
#     start=0;end=len(fib)
#     if 'offset' in kwargs.keys():
#         start=kwargs['offset']
#     if 'limit' in kwargs.keys():
#         end=start+kwargs['limit']
#     return fib[start:end]
    
# print(process(
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#     limit=2,
#     offset=2
# ) )

# Problem 9
# def getStatistics(pairs:list) -> list:
#     return [{'sum':e[0]+e[1], 'prod':e[0]*e[1], 'pow':e[0]**e[1]} for e in pairs]


