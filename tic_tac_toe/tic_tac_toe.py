import pygame
import sys
import random
from pygame.locals import *

# region     Global variables, window setup, image work, game state var.
# Initialize pygame
pygame.init()

# Global variables
width = 400
height = 400
white = (255, 255, 255)
black = (0, 0, 0)
line_color = (10, 10, 10)
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
board = [[None] * 3, [None] * 3, [None] * 3]

# Window setup
screen = pygame.display.set_mode((width, height + 100), 0, 32)
pygame.display.set_caption("Tic Tac Toe")
screen.fill(white)

# Load and resize images
x_img = pygame.image.load(
    r"tic_tac_toe/assets/x_game_image.png"
)
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.image.load(
    r"tic_tac_toe/assets/o_game_image.png"
)
o_img = pygame.transform.scale(o_img, (80, 80))

# Game state
letter = "X"
draw = False
winner = None
CLOCK = pygame.time.Clock()
fps = 30
# endregion

def run():


    def draw_grid():
        screen.fill(white)
        # vertical lines
        pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
        pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
        # horizontal lines
        pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
        pygame.draw.line(
            screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7
        )


    def draw_status():
        global random_color

        if winner:
            message = f"{winner} won!"
        elif draw:
            message = "Draw game!"
        else:
            message = f"{letter}'s Turn"

        font = pygame.font.Font(None, 30)
        text = font.render(message, True, black)
        screen.fill(random_color, (0, height, width, 100))

        if winner or draw:
            draw_buttons()
            text_rect = text.get_rect(center=(width / 2, height + 30))
            screen.blit(text, text_rect)
        else:
            text_rect = text.get_rect(center=(width / 2, height + 50))
            screen.blit(text, text_rect)

        pygame.display.update()


    def draw_buttons():
        font = pygame.font.Font(None, 28)

        restart_rect = pygame.Rect(60, height + 50, 120, 40)
        pygame.draw.rect(screen, (35, 153, 67), restart_rect)
        restart_text = font.render("Restart", True, white)
        screen.blit(restart_text, (restart_rect.x + 20, restart_rect.y + 8))

        quit_rect = pygame.Rect(220, height + 50, 120, 40)
        pygame.draw.rect(screen, (153, 35, 35), quit_rect)
        quit_text = font.render("Quit", True, white)
        screen.blit(quit_text, (quit_rect.x + 35, quit_rect.y + 8))


    def draw_letter(row, col):
        global board
        cell_size = width // 3
        offset = (cell_size - 80) // 2
        posx = (col - 1) * cell_size + offset
        posy = (row - 1) * cell_size + offset

        if letter == "X":
            screen.blit(x_img, (posx, posy))
            board[row - 1][col - 1] = "X"
        else:
            screen.blit(o_img, (posx, posy))
            board[row - 1][col - 1] = "O"

        pygame.display.update()


    def check_win():
        global winner, draw

        for row in range(3):
            if (
                board[row][0] == board[row][1] == board[row][2]
                and board[row][0] is not None
            ):
                winner = board[row][0]
                pygame.draw.line(
                    screen,
                    (250, 0, 0),
                    (0, (row + 1) * height / 3 - height / 6),
                    (width, (row + 1) * height / 3 - height / 6),
                    4,
                )
                return

        for col in range(3):
            if (
                board[0][col] == board[1][col] == board[2][col]
                and board[0][col] is not None
            ):
                winner = board[0][col]
                pygame.draw.line(
                    screen,
                    (250, 0, 0),
                    ((col + 1) * width / 3 - width / 6, 0),
                    ((col + 1) * width / 3 - width / 6, height),
                    4,
                )
                return

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            winner = board[0][0]
            pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
            return

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            winner = board[0][2]
            pygame.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
            return

        if all([all(row) for row in board]) and winner is None:
            draw = True


    def user_click():
        global letter, winner, draw, random_color

        x, y = pygame.mouse.get_pos()

        if winner or draw:
            handle_game_over_click()
            return

        # Ignore clicks below the grid
        if y > height:
            return

        col = int(x // (width / 3)) + 1
        row = int(y // (height / 3)) + 1

        if row <= 3 and col <= 3 and board[row - 1][col - 1] is None:
            draw_letter(row, col)
            check_win()
            if not winner and not draw:
                if letter == "X":
                    letter = "O"
                else:
                    letter = "X"
                random_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

            draw_status()


    def handle_game_over_click():
        x, y = pygame.mouse.get_pos()

        if 60 <= x <= 180 and height + 50 <= y <= height + 90:
            reset_game()
        elif 220 <= x <= 340 and height + 50 <= y <= height + 90:
            pygame.quit()
            sys.exit()


    def reset_game():
        global board, winner, draw, letter
        board = [[None] * 3, [None] * 3, [None] * 3]
        winner = None
        draw = False
        letter = "X"
        draw_grid()
        draw_status()


    # Start game
    draw_grid()
    draw_status()


    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                user_click()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

        pygame.display.update()
        CLOCK.tick(fps)

def test():
    print("this is a test")