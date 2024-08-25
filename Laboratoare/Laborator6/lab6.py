import re

# Pattern 1
# p1 = re.compile("^\w+$")
# print(p1.match("ABCDEFabcdef123450"))
# print(p1.match("29414safdvapver2352"))
# print(p1.match("124"))
# print(p1.match("*&%@#!}{"))
# print(p1.match("42ec351*"))

# Pattern 2

# p2 = re.compile("ab+?")
# print(p2.search("rabbbbbc"))
# print(p2.search("aaaa"))
# print(p2.search("yesssssbbab"))
# print(p2.search("241042i1204-1"))

# Pattern 4
# p2 = re.compile('ab?')
# print(p2.search('hahasfasf'))

# Pattern 5
# p5 = re.compile('ab{3}')
# print(p5.search('fadfaaabbbdas'))
# print(p5.search('fafsafaabbfasdabas'))

# Pattern 6
# p6 = re.compile('ab{2,3}')
# print(p6.search('fasdasdaabbasdada'))
# print(p6.search('fasdasdaaaaafagab'))

# Pattern 7
# p7 = re.compile('^[a-z]+_[a-z]+$')
# print(p7.search('ab_cd'))
# print(p7.search('_cd'))
# print(p7.search('ab__ac_ab'))

# Pattern 8
# p8 = re.compile('^[A-Z]{1}_[a-z]+$')

# print(p8.search("aab_cbbbc"))
# print(p8.search("aab_Abbbc"))
# print(p8.search("Aaab_abbbc"))

# Pattern 9
# p9 = re.compile('a{1}.*b{1}$')
# print(p9.search("aabbbbd"))
# print(p9.search("aabAbbbc"))
# print(p9.search("accddbbjjjb"))

# Pattern 10
# p10 = re.compile('^\w+')
# print(p10.search("The quick brown fox jumps over the lazy dog."))
# print(p10.search(" The quick brown fox jumps over the lazy dog."))

# Pattern 11
# p11 = re.compile('\w+[-\.?!]$')
# print(p11.search("The quick brown fox jumps over the lazy dog."))
# print(p11.search("The quick brown fox jumps over the lazy dog. "))
# print(p11.search("The quick brown fox jumps over the lazy dog "))

# Pattern 12
# p12 = re.compile('\w*z\w*')
# print(p12.search("The quick brown fox jumps over the lazy dog."))
# print(p12.search("Python Exercises."))

# Pattern 13
# p13 = re.compile(r'\b[^z\s\d]+?\w*z\w*\b')
# obj = p13.search("The quick brown fox jumps over the lazy dog.")
# print(obj.group(0))

# Problem 1

# def extractWords(text:str) -> list:
#     return re.compile(r'\b[\w]+\b').findall(text)
# print(extractWords("This is a text with 7 words"))

# Problem 2

# def function2(regex:str, text:str, x:int) -> list:
#     p=re.compile(regex)
#     l=p.findall(text)
#     return list(filter(lambda st: len(st) == x, l))
# print(function2(r'\ba{2}[^a]\w*b\b', 'this aacadasdab aaabcasdb fsdafaaabcasd aab', 3))

# Problem 3

# def function3(l:list, rl:list):
#     return [s for s in l if len([reg for reg in rl if re.compile(reg).match(s)]) > 0]
# print(function3(['cbc', 'adad', 'vadcasd', 'asdas'], [r'a\w*$', r'\w*c$']))

# Problem 4


def function4(attrs:dict) -> list:
    tags:list=[];match:list=[];ans:list=[]
    for item in attrs.items():
        match.append('='.join(item))
    s=' '.join(match)
    with open('file.xml','r') as f:
        for line in f:
            p=re.compile(f'^<\w+{s}\w*>')
            print(s, str(p))
            if p.match(line):
                ans.append(line)
    return None if ans == [] else ans 

print(function4(attrs={'class': '\"url\"', 'name': '\"url-form\"', 'data-id': '\"item\"'}))