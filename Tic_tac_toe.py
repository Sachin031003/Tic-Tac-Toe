import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
LINE_HEIGHT = 15

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game variables
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 'X'
game_over = False
winner = None

# Functions
def draw_grid():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(window, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(window, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

def draw_xo():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                x_pos = col * CELL_SIZE + CELL_SIZE // 2
                y_pos = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.line(window, X_COLOR, (x_pos - 40, y_pos - 40), (x_pos + 40, y_pos + 40), LINE_WIDTH)
                pygame.draw.line(window, X_COLOR, (x_pos + 40, y_pos - 40), (x_pos - 40, y_pos + 40), LINE_WIDTH)
            elif board[row][col] == 'O':
                x_pos = col * CELL_SIZE + CELL_SIZE // 2
                y_pos = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.circle(window, O_COLOR, (x_pos, y_pos), CELL_SIZE // 2 - LINE_WIDTH)

def check_win(player):
    # Check rows, columns, and diagonals for a win
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or \
           all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

def check_draw():
    return all(all(cell != '' for cell in row) for row in board)

def restart_game():
    global board, current_player, game_over, winner
    board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = 'X'
    game_over = False
    winner = None

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_win(current_player):
                        game_over = True
                        winner = current_player
                    elif check_draw():
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart_game()

    window.fill(WHITE)
    draw_grid()
    draw_xo()

    if game_over:
        font = pygame.font.Font(None, 36)
        if winner:
            text = f"Player {winner} wins! Press 'R' to restart."
        else:
            text = "It's a draw! Press 'R' to restart."
        text_surface = font.render(text, True, LINE_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text_surface, text_rect)

    pygame.display.flip()
