class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        else:
            return "La pila está vacía"

    def is_empty(self):
        return len(self.elementos) == 0


#Uso de la clase Pila
pila = Pila()
pila.push('Z')
pila.push('Y')
pila.push('X')
pila.push('W')
pila.push('V')
pila.push('U')
pila.push('T')
pila.push('S')
pila.push('R')
pila.push('Q')
pila.push('P')
pila.push('O')
pila.push('N')
pila.push('M')
pila.push('Hanka')
pila.push('L')
pila.push('K')
pila.push('J')
pila.push('I')
pila.push('H')
pila.push('G')
pila.push('F')
pila.push('E')
pila.push('D')
pila.push('C')
pila.push('B')
pila.push('A')

print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())


