import math
from nodo import Nodo
from constantes import FILAS, COLUMNAS

class AStar:
    def __init__(self, mapa):
        self.mapa = mapa

    def heuristica(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def get_vecinos(self, nodo):
        vecinos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direcciones:
            x, y = nodo.pos[0] + dx, nodo.pos[1] + dy
            if 0 <= x < FILAS and 0 <= y < COLUMNAS and self.mapa.grid[x][y] != '#':
                vecinos.append(Nodo((x, y), nodo))
        return vecinos

    def encontrar_camino(self, inicio, destino):
        inicio_nodo = Nodo(inicio)
        destino_nodo = Nodo(destino)

        abiertos = [inicio_nodo]
        cerrados = []

        while abiertos:
            abiertos.sort(key=lambda nodo: nodo.f)
            actual = abiertos.pop(0)
            cerrados.append(actual)

            if actual == destino_nodo:
                camino = []
                while actual:
                    camino.append(actual.pos)
                    actual = actual.padre
                return camino[::-1]

            for vecino in self.get_vecinos(actual):
                if vecino in cerrados:
                    continue

                vecino.g = actual.g + 1
                vecino.h = self.heuristica(vecino.pos, destino_nodo.pos)
                vecino.f = vecino.g + vecino.h

                if any(abierto for abierto in abiertos if vecino == abierto and vecino.g > abierto.g):
                    continue

                abiertos.append(vecino)
        return None
