class Nodo:
    def __init__(self, posicion, padre=None):
        self.pos = posicion
        self.padre = padre
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otro):
        return self.pos == otro.pos
