import math
import time
from functools import reduce

class Circle:
    __slots__ = ('radius', 'coordinates')
    def __init__(self, radius:int, coordinates:tuple):
        self.radius = radius
        self.coordinates = coordinates
    def getArea(self) -> int:
        return math.pi * self.radius ** 2
    def getPerimeter(self) -> int:
        return 2 * math.pi * self.radius

class Person:
    __slots__ = ('name', 'country', 'date_of_birth')
    def __init__(self, name:str, country:str, date_of_birth:str):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculateAge(self):
        day, month, year = [int(x) for x in self.date_of_birth.split('.')]
        currYear = int(time.localtime()[0]); currMonth = int(time.localtime()[1]); currDay = int(time.localtime()[2])
        return currYear - year - 1 if month > currMonth or month == currMonth and day > currDay else currYear - year


class Stack:
    __slots__ = ('elements')
    
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]
    
    def __add__(self, s):
        self.elements += s.elements
        return self
    
    def __str__(self) -> None:
        s = str(reduce(lambda x, y:str(y)+'\n'+str(x), self.elements))
        return f'The elements that form the Stack from top to bottom are:\n{s}'        
        

def main() -> None: 
    
    # Problem 1
    # c = Circle(10, (1.2, 3.1))
    # print(f'The perimeter of the circle is {c.getPerimeter()} and the area is {c.getArea()}')

    # Problem 2
    # p = Person('Stefan', 'Romania', '09.11.2004')
    # print(p.calculateAge())

    s = Stack()
    s2 = Stack()

    s.push(1); s.push(2); s.push(3); s.push(4); 
    s2.push(5); s2.push(6); s2.push(7)

    s += s2
    print(s)

    s.pop()

    print(s)

    pass

if __name__ == '__main__':
    main()