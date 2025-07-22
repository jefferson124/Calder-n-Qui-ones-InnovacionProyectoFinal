import pygame
from minmax import get_best_move

BLACK = (0, 0, 0)
LINE_WIDTH = 5

CELL_SIZE = 100
ROWS, COLS = 3, 3

class Board:
    def __init__(self):
        self.grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def reset(self):
        self.__init__()

    def draw(self, screen):
        for i in range(1, ROWS):
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (300, i * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 300), LINE_WIDTH)

        for y in range(ROWS):
            for x in range(COLS):
                mark = self.grid[y][x]
                if mark:
                    font = pygame.font.SysFont(None, 80)
                    text = font.render(mark, True, BLACK)
                    text_rect = text.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(text, text_rect)

    def handle_click(self, x, y):
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if self.grid[row][col] == "" and not self.game_over:
            self.grid[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.game_over = True
            else:
                self.current_player = "O"
                self.ai_move()

    def ai_move(self):
        move = get_best_move(self.grid)
        if move:
            row, col = move
            self.grid[row][col] = "O"
            if self.check_winner():
                self.winner = "O"
                self.game_over = True
            else:
                self.current_player = "X"

    def check_winner(self):
        lines = []

        # Filas y columnas
        for i in range(3):
            lines.append(self.grid[i])
            lines.append([self.grid[0][i], self.grid[1][i], self.grid[2][i]])

        # Diagonales
        lines.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        lines.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        for line in lines:
            if line[0] != "" and all(cell == line[0] for cell in line):
                return True

        # Empate
        if all(cell != "" for row in self.grid for cell in row):
            self.winner = None
            self.game_over = True
            return False

        return False

