import pygame
from board import Board
from button import Button

WIDTH, HEIGHT = 300, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
FONT = pygame.font.SysFont(None, 40)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("3 en Raya vs IA")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.winner_text = ""
        self.restart_button = Button("Reiniciar", 100, 350, 100, 40, self.restart_game)

    def restart_game(self):
        self.board.reset()
        self.winner_text = ""

    def draw_winner(self):
        if self.winner_text:
            text = FONT.render(self.winner_text, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 320))
            self.screen.blit(text, text_rect)

    def run(self):
        running = True
        while running:
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.board.game_over:
                    x, y = pygame.mouse.get_pos()
                    self.board.handle_click(x, y)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.restart_button.handle_event(event)

            self.board.draw(self.screen)

            if self.board.game_over and not self.winner_text:
                if self.board.winner == "X":
                    self.winner_text = "Ganaste"
                elif self.board.winner == "O":
                    self.winner_text = "Perdiste"
                else:
                    self.winner_text = "Empate"

            self.draw_winner()
            self.restart_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
