import math;
import functools;

# Problem 1
# s=input().split(' ');
# s=[int(i) for i in s];
# print(functools.reduce(math.gcd, s));

# Problem 2
# s=input();
# vowels=['a','e','i','o','u'];
# count=(s.count(vowel) for vowel in vowels);

# Problem 3
# s, s2 = input().split(' ');
# print(s.count(s2));

# Problem 4
# s=input();
# s2="";
# ok=0;
# for ch in s:
#     if str(ch).isupper():
#         if ok != 0:
#             s2 += f"_{ch.lower()}";
#         else:
#             ok += 1;s2 += ch.lower();
#     else:
#         s2 += ch;
# print(s2);

# Problem 5
# s=input();
# n=len(s);
# matrix=list();
# matrix.append(s);
# for i in range(1, n):
#     s=input();
#     matrix.append(s);

# for i in range(0, int((n+1) / 2)):
#     for j in range(i, n - i):
#         print(matrix[i][j], end="");
#     for j in range(i + 1, n - i):
#         print(matrix[j][n-i-1], end="");
#     for j in range(n-i-2, i-1, -1):
#         print(matrix[n-i-1][j], end="");
#     for j in range(n-i-2,i,-1):
#         print(matrix[j][i],end="");

# Problem 6
# s=input();
# if s == s[-1:-len(s)-1:-1]:
#     print("The string is a palindrome!");
# else:
#     print("The string is not a palindrome");

#Problem 7
# s=input();
# l=list(((ch,pos) for pos, ch in enumerate(s) if ch >= '0' and ch <= '9'));
# pos=l[0][1]; number=str(l[0][0]);
# l.pop(0);
# for num in l:
#     if pos+1==num[1]:
#         number+=num[0]; pos=num[1];
#     else:
#         break;
# print(number);

#Problem 8
# bits=0;
# number=bin(int(input()))[2:];
# for bit in number:
#     if bit == '1':
#         bits = bits + 1;
# print(bits);

#Problem 9
# s=input();
# maxim=max((s.count(chr(ch)) + s.count(chr(ch-32)), idx) for idx, ch in enumerate(range(97,97+26)));
# print(chr(maxim[1]+97));

#Problem 10
# s=input().split();
# print(len(s));