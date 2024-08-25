import copy

class Carte:

    def  __init__(self):
        pass

    def GetInfo(self):
        pass


class Roman(Carte):

    __slots__ = ('nume', 'autor')

    def __init__(self, nume, autor):
        super().__init__
        self.nume = nume 
        self.autor = autor 

    def GetInfo(self):
        return f'Roman {self.nume} de {self.autor}'
    

class Revista(Carte):

    __slots__ = ('nume', 'autor')

    def __init__(self, nume, nrArticole):
        super().__init__
        self.nume = nume 
        self.nrArticole = nrArticole

    def GetInfo(self):
        return f'Revista {self.nume} cu {self.nrArticole} articole'

class Biblioteca():

    __slots__ = ('count', 'elements')

    def __init__(self):
        self.elements = []
        self.count = 0

    def __iadd__(self, element):
        self.elements.append(element)
        return self 

    def __iter__(self):
        return copy.deepcopy(self)

    def __next__(self):
        if self.count < len(self.elements):
            self.count = self.count + 1
            return self.elements[self.count - 1]
        else:
            raise StopIteration
    
    def __int__(self):
        return len(self.elements)

    def PrintFilter(self, f):
        for book in list(filter(f, self.elements)):
            print(book.GetInfo())

def main():
    b = Biblioteca()
    (b.__iadd__(Roman('DON QUIJOTE', 'MIGUEL DE CERVANTES'))).__iadd__(Revista('Journal of Artificial Intelligence', 100))
    b += Roman('MACBETH', 'WILLIAM SHAKESPEARE')

    for book in b:
        print(book.GetInfo())
    
    print(f'Numar de intrari in biblioteca: {int(b)}')
    print('Lista doar cu romane:')
    b.PrintFilter(lambda c: issubclass(type(c), Roman))

if __name__ == '__main__':
    main()