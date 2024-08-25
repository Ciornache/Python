# Problem 1
# def getSetOperations(a, b):
#     a, b = set(a), set(b)
#     return [a & b, a | b, a - b, b - a]
# print(getSetOperations({1, 2, 3}, {3, 4, 5}))

# Problem 2
# def getDictionary(s:str):
#     return {ch:s.count(ch) for ch in set(s)}
# print(getDictionary("Hello World"))

# Problem 3
# def compareDictionaries(d:dict, d2:dict):
#     d3={k:d[k] for k in d.keys() if k in d2 and d[k] == d2[k]}
#     if(len(d3) == len(d) == len(d2)):
#         return True
#     else:
#         return False 
# print(compareDictionaries({"1":[1,2,3], "hellow":12, "baba":2}, {"1":[1,2,3], "hellow":12, "baba":2}));

# Problem 4
# def buildXmlElement(tag:str, content:str, **d):
#     return f'<{tag} {"".join(list(str(k)+"="+d[k] for k in d.keys()))}>{content}</{tag}>';
# print(buildXmlElement("a", "Hello there", href="http://python.org ", _class ="my-link ", id="someid"));

# Problem 5
# def validateDictionary(s:set, d:dict):
#     k=list(s)[0];
#     return len(d)==len({k:d[k] for k in s if k[0] in d.keys() and d[k[0]][0:len(k[1])] == k[1] and d[k[0]][-len(k[3]):0] == k[3] and k[2] in d[k[0]][len(k[1]):-len(k[3])-1]});
# print(validateDictionary({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out"}));

# Problem 6
# def problem6(l:list):
#     return len(set(l)), len([k for k in set(l) if l.count(k) > 1]);

# Problem 7
# def combineSets(*l):
#     d=dict();
#     for (index1, s) in enumerate(l):
#         for (index2, s2) in enumerate(l):
#             if index1 < index2:
#                 d[f'{s} | {s2}'] = s|s2;
#                 d[f'{s} & {s2}'] = s&s2;
#                 d[f'{s} - {s2}'] = s-s2;
#                 d[f'{s2} - {s}'] = s2-s;
#     return d;
# print(combineSets({1, 2}, {2, 3}));

# Problem 8
# def startLoop(mapping:dict):
#     s=[]; k=mapping['start'];
#     while k not in s:
#         s.append(k);
#         k=mapping[k];
#     return list(s);
# print(startLoop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}));

# Problem 9
# def my_function(*args, **kwargs):
#     return len({l for l in kwargs.values()} & set(args))


try:
    x=5/0;
except (ZeroDivisionError) as e:
    print(str(e), type(e));
    print(type(int));