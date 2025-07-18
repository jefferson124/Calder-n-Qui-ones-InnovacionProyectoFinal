import random
import pygame
from constantes import *

class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grid = [['0' for _ in range(columnas)] for _ in range(filas)]

    def colocar_obstaculos(self, cantidad, inicio, destino):
        colocados = 0
        while colocados < cantidad:
            f = random.randint(0, self.filas - 1)
            c = random.randint(0, self.columnas - 1)
            if self.grid[f][c] == '0' and (f, c) != inicio and (f, c) != destino:
                self.grid[f][c] = '#'
                colocados += 1

    def dibujar(self, pantalla, inicio, destino, camino):
        for i in range(self.filas):
            for j in range(self.columnas):
                x, y = j * TAM_CELDA, i * TAM_CELDA
                color = BLANCO
                if (i, j) == inicio:
                    color = VERDE
                elif (i, j) == destino:
                    color = ROJO
                elif self.grid[i][j] == '#':
                    color = NEGRO
                elif (i, j) in camino:
                    color = AMARILLO
                pygame.draw.rect(pantalla, color, (x, y, TAM_CELDA, TAM_CELDA))
                pygame.draw.rect(pantalla, GRIS, (x, y, TAM_CELDA, TAM_CELDA), 1)
