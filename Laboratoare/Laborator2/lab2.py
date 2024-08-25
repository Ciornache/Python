from sympy import *
import functools;
# Problem 1
# def fibonacci(n):
#     l=list();
#     l.append(1), l.append(1);
#     for it in range(2, n):
#         l.append(l[it-1]+l[it-2]);
#     return l;
# print(fibonacci(10));

# Problem 2
# def getPrimeNumbers(l:list):
#     return list(x for x in l if isprime(x) == True);
# print(getPrimeNumbers([4, 2, 3, 1, 5, 1, 61, 41, 41, 321]));

# Problem 3
# def setOperations(a:list, b:list):
#     intersectie=set(x for x in a if x in b);
#     reuniune=set(a).union(set(b));
#     difab=set(x for x in a if x not in b);
#     difba=set(x for x in b if x not in a);
#     return (intersectie, reuniune, difab, difba);

# print(setOperations([1,2], [2, 1, 3]));

# Problem 4
# def getSong(notes:list, moves:list, start):
#     song=[];
#     for move in moves:
#         song.append(notes[start]);
#         start += move; start %= len(notes);
#     song.append(notes[start]);
#     return song;
# print(getSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2));

# Problem 5
# def modifyMatrix(l:list):
#     n=len(l);
#     for (i, l2) in enumerate(l):
#         for (j, x) in enumerate(l2):
#             if i>j:
#                 l[i][j]=0;
#     return l;
# print(modifyMatrix([[1,2,3], [1,2,3], [1,2,3]]));

# Problem 6

# def setOperations(a:list, b:list):
#      reuniune=set(a).union(set(b)); 
#      return reuniune;

# def getElementsByFrequency(*lists):
#     freq=lists[len(lists)-1]
#     listOfLists=[];
#     for l in lists:
#          if type(l) is list:
#               listOfLists.append(l);
#     reuniune=functools.reduce(setOperations, listOfLists)
#     rez=[]
#     for x in reuniune:
#          fr = 0
#          for l in listOfLists:
#               fr += l.count(x)
#          if fr == freq:
#               rez.append(x)
#     return rez;

# print(getElementsByFrequency([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], 2));

# Problem 7

# def isPalindrome(x):
#     s=str(x)
#     if s == s[-1:-len(s)-1:-1]:
#         return True
#     else:
#         return False 

# def getPalindromeInfo(l:list):
#     paList=list(filter(isPalindrome, l));
#     return (len(paList), max(paList));

# print(getPalindromeInfo([11, 22, 132, 144, 414, 505, 55, 14124]));

# Problem 8 

# def getAsciiCodes(l, flag, x = 1):
#     remainders=list(range(0,x))
#     print(remainders);
#     if flag == True:
#         remainders=[x for x in remainders if x == 0]
#     else:
#         remainders.pop(0)
#     print(remainders);
#     rez=[]
#     for element in l:
#         s=set(ch for ch in element if ord(ch) % x in remainders);
#         rez.append(list(s));
#     return rez;

# print(getAsciiCodes(["test", "hello", "lab002"], False, 2));

# Problem 9
# def getListOfBadSpectators(matrix:list):
#     n=len(matrix);
#     spectators = [];
#     for (i, l) in enumerate(matrix):
#         for (j, element) in enumerate(l):
#             if i == 0:
#                 continue;
#             if matrix[i-1][j] > matrix[i][j]:
#                 spectators.append(((i, j)));
#     return spectators;

# print(getListOfBadSpectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]));

# Problem 10
# def getListOfTuples(*lists):
#     maxim=max([len(x) for x in lists]);
#     for x in lists:
#         for i in range(0, maxim-len(x)):
#             x.append(None);
#     rez=[];
#     for i in range(0, maxim):
#         rez.append(tuple([x[i] for x in lists]));
#     return rez;

# print(getListOfTuples([1,2,3],[5,6,7],["a","b","c"]));

# Problem 11
# def sortByThirdCharacter(l:list):
#     def getThirdCharacter(t:tuple):
#         return t[1][2];    
#     l.sort(key=getThirdCharacter);
# l=[('abc','bcd'), ('abc', 'zza')];
# sortByThirdCharacter(l);
# print(l);    

# Problem 12
# def groupByRhyme(l:list):
#     s=set([x[-2:] for x in l]);
#     rez=[];
#     for gr in s:
#         def filterFunction(s):
#             if s[-2:] == gr:
#                 return True;
#             else:
#                 return False;
#         rez.append(list(filter(filterFunction, l)));
#     return rez;

# print(groupByRhyme(['ana', 'banana', 'carte', 'arme', 'parte']));