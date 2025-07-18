import pygame
import sys
from constantes import *
from mapa import Mapa
from astar import AStar

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("A* Laberinto 5x5 Interactivo")
        self.fuente = pygame.font.SysFont(None, 24)
        self.reiniciar()

    def reiniciar(self):
        self.mapa = Mapa(FILAS, COLUMNAS)
        self.inicio = None
        self.destino = None
        self.estado = 'seleccionando'
        self.camino = []

    def ejecutar(self):
        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

                if evento.type == pygame.MOUSEBUTTONDOWN and self.estado == 'seleccionando':
                    self.procesar_clic(evento.pos)

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE and self.inicio and self.destino:
                        self.estado = 'resuelto'
                        astar = AStar(self.mapa)
                        self.camino = astar.encontrar_camino(self.inicio, self.destino)
                    elif evento.key == pygame.K_r:
                        self.reiniciar()

            self.dibujar()

        pygame.quit()
        sys.exit()

    def procesar_clic(self, pos):
        fila = pos[1] // TAM_CELDA
        col = pos[0] // TAM_CELDA


        if col >= COLUMNAS:
            return

        if self.inicio is None:
            self.inicio = (fila, col)
        elif self.destino is None and (fila, col) != self.inicio:
            self.destino = (fila, col)
        elif (fila, col) != self.inicio and (fila, col) != self.destino:
            self.mapa.grid[fila][col] = '#'

    def dibujar(self):
        self.pantalla.fill(BLANCO)
        self.mapa.dibujar(self.pantalla, self.inicio, self.destino, self.camino)
        self.dibujar_texto()
        pygame.display.flip()

    def dibujar_texto(self):
        instrucciones = [
            "[INSTRUCCIONES]",
            "Clic 1: Inicio (Verde)",
            "Clic 2: Destino (Rojo)",
            "Clics siguientes: Obstáculos (Negro)",
            "ESPACIO: Iniciar A*",
            "R: Reiniciar mapa"
        ]
        for i, linea in enumerate(instrucciones):
            texto = self.fuente.render(linea, True, (0, 0, 0))
            self.pantalla.blit(texto, (COLUMNAS * TAM_CELDA + 10, 20 + i * 25))

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()

