import os;

# Problem 1
# def getExtensions(director:str):
#     entries=sorted({''.join(fisier.split('.')[-1:-2:-1]) for fisier in os.listdir(director) if len(fisier.split('.'))>1})
#     return entries

# Problem 2
# def writeToFile(director:str, file:str):
#     entries={fisier for fisier in os.listdir(director) if fisier[0] == 'C'}
#     print(entries)
#     try:
#         with open(file, "x") as f:
#              pass
#     except FileExistsError:
#         pass
#     finally:
#         with open(file, "w") as f:
#             for entry in entries:
#                 f.write(os.path.abspath(f'{director}\{entry}\n'))

# writeToFile("D:/Documents", "D:/Downloads/fisier.txt")

# Problem 3
# def f(my_path:str):
#     if os.path.isfile(my_path):
#         with open(my_path, "r") as f:
#             entries=list(f.read())
#             entries.reverse()
#             return list(reversed(entries[:20]))
#     else:
#         entries=sorted([''.join(fisier.split('.')[-1:-2:-1]) for fisier in os.listdir(my_path) if len(fisier.split('.'))>1])
#         return sorted([(entry, entries.count(entry)) for entry in set(entries)], key=lambda x:x[1], reverse=True);

# print(f("D:/Downloads/fisier.txt"))
# print(f("D:/Documents"));

# Problem 4
# def getExtensions(director:str):
#     entries=sorted({''.join(fisier.split('.')[-1:-2:-1]) for fisier in os.listdir(director) if len(fisier.split('.'))>1})
#     return entries

# Problem 5
# def search(target:str, to_search:str) -> list[str]:
#     if os.path.isfile(target):
#         with open(target, "r") as f:
#             if target[-3:] == 'txt' and f.read().split().count(to_search) > 0:
#                 return [target]
#         return []
#     elif os.path.isdir(target):
#         files=[];
#         for file in os.listdir(target):
#             try:
#                 files.append(*search(f'{target}/{file}', to_search))
#             except TypeError:
#                 pass
#         return files
#     else:
#         return [];
    
# print(*search("D:/Documents/Test", 'int'));

# Problem 6

# def handleException(ex:BaseException):
#     pass
# def search(target:str, to_search:str, callback) -> list[str]:
#     if os.path.isfile(target):
#         with open(target, "r") as f:
#             if target[-3:] == 'txt' and f.read().split().count(to_search) > 0:
#                 return [target]
#         return []
#     elif os.path.isdir(target):
#         files=[];
#         for file in os.listdir(target):
#             try:
#                 files.append(*search(f'{target}/{file}', to_search, callback))
#             except TypeError as e:
#                 callback(e)
#         return files
#     else:
#         return [];
    
# print(*search("D:/Documents/Test", 'int', handleException))

# Problem 7 

print("The weather is {0:d} and the total temperature is at a staggering {0:d} degrees C".format(42, 32, 5, 1, '42', 42, True, False))

s='Jaspreet'
print(s, repr(s))