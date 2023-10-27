import pygame
import sys
import math
import time

# Colors
PINK = (255, 182, 193)
WHITE = (255, 255, 255)

class Cat_Mouse_game:
    def __init__(self):
        """
            Two-player game of Cat and Mouse.

            Attributes:
                - ROWS, COLUMNS, GRID_SIZE, RADIUS: Dimensions and sizes.
                - size: Window dimensions.
                - Sounds and images for game elements.
                - board: 2D list representing the game board.

            Methods:
                - game_board(): Initialize empty board.
                - check_valid_location(col): Check if column is valid.
                - open_row(col): Find available row for chip.
                - drop_chips(row, col, chips): Place chip.
                - check_victory(chips): Check for victory.
                - display_board(): Draw the board.
                - display_winner(player): Display winner and duration.
                - display_current_player(): Display current player's turn.
                - reset_game(): Reset game state.
                - play(): Main game loop.
            """
        # Constants
        self.ROWS = 6
        self.COLUMNS = 7
        self.GRID_SIZE = 100
        self.RADIUS = int(self.GRID_SIZE / 2 - 5)
        self.WINDOW_WIDTH = self.COLUMNS * self.GRID_SIZE
        self.WINDOW_HEIGHT = (self.ROWS + 1) * self.GRID_SIZE
        self.size = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Load images and sounds
        pygame.mixer.init()
        self.player_win_sound = pygame.mixer.Sound("winning.mp3")
        self.drop_sound_player1 = pygame.mixer.Sound("cat_noise.mp3")
        self.drop_sound_player2 = pygame.mixer.Sound("player2.mp3")

        self.cat_image = pygame.image.load("cat.png")
        self.cat_image = pygame.transform.scale(self.cat_image, (self.GRID_SIZE, self.GRID_SIZE))

        self.mouse_image = pygame.image.load("mouse.png")
        self.mouse_image = pygame.transform.scale(self.mouse_image, (self.GRID_SIZE, self.GRID_SIZE))

        self.board = self.game_board()
        self.round_finished = False
        self.turn = 0
        self.start_time = 0
        self.current_player = 1

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.myfont = pygame.font.SysFont("calibri", 50)
        self.display_board()

    def game_board(self):
        return [[0 for i in range(self.COLUMNS)] for j in range(self.ROWS)]

    def check_valid_location(self, col):
        return self.board[self.ROWS - 1][col] == 0

    def open_row(self, col):
        for r in range(self.ROWS):
            if self.board[r][col] == 0:
                return r

    def drop_chips(self, row, col, chips):
        self.board[row][col] = chips

    def check_victory(self, chips):
        # Horizontal Check
        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS):
                if (
                        self.board[r][c] == chips and
                        self.board[r][c + 1] == chips and
                        self.board[r][c + 2] == chips and
                        self.board[r][c + 3] == chips
                ):
                    return True
        # Vertical Check
        for c in range(self.COLUMNS):
            for r in range(self.ROWS - 3):
                if (
                        self.board[r][c] == chips and
                        self.board[r + 1][c] == chips and
                        self.board[r + 2][c] == chips and
                        self.board[r + 3][c] == chips
                ):
                    return True
        # Postivitely Sloped Diagonals Check
        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS - 3):
                if (
                        self.board[r][c] == chips and
                        self.board[r + 1][c + 1] == chips and
                        self.board[r + 2][c + 2] == chips and
                        self.board[r + 3][c + 3] == chips
                ):
                    return True
        # Negatively Sloped Diagonals Check
        for c in range(self.COLUMNS - 3):
            for r in range(3, self.ROWS):
                if (
                        self.board[r][c] == chips and
                        self.board[r - 1][c + 1] == chips and
                        self.board[r - 2][c + 2] == chips and
                        self.board[r - 3][c + 3] == chips
                ):
                    return True

    def display_board(self):
        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                pygame.draw.rect(self.screen, PINK, (c * self.GRID_SIZE, r * self.GRID_SIZE + self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
                pygame.draw.circle(self.screen, WHITE, (int(c * self.GRID_SIZE + self.GRID_SIZE / 2), int(r * self.GRID_SIZE + self.GRID_SIZE + self.GRID_SIZE / 2)), self.RADIUS)

        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                if self.board[r][c] == 1:
                    self.screen.blit(self.cat_image, (c * self.GRID_SIZE, (self.ROWS - 1 - r) * self.GRID_SIZE + self.GRID_SIZE))
                elif self.board[r][c] == 2:
                    self.screen.blit(self.mouse_image, (c * self.GRID_SIZE, (self.ROWS - 1 - r) * self.GRID_SIZE + self.GRID_SIZE))
        pygame.display.update()

    def display_winner(self, player):
        # Display the winner and game duration
        end_time = time.time()
        duration = round(end_time - self.start_time)
        label = self.myfont.render(f"Cat wins in {duration} seconds!" if player == 1 else f"Mouse wins in {duration} seconds!", 1, WHITE)
        self.screen.blit(label, (40, 10))
        self.player_win_sound.play()

    def display_current_player(self):
        # Display current player's turn
        font = pygame.font.Font(None, 36)
        player_text = font.render(f'Current Player: {self.current_player}', True, WHITE)
        self.screen.blit(player_text, (40, 10))
        pygame.display.update()

    def reset_game(self):
        # Reset the game state
        self.board = self.game_board()
        self.round_finished = False
        self.turn = 0
        self.start_time = 0
        self.current_player = 1
        self.screen.fill(PINK)
        self.display_board()
        self.display_current_player()

    def play(self):
        # Main game loop
        while not self.round_finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    # Highlight column on hover
                    pygame.draw.rect(self.screen, WHITE, (0, 0, self.WINDOW_WIDTH, self.GRID_SIZE))
                    mouse_click_x = event.pos[0]
                    if self.current_player == 1:
                        self.screen.blit(self.cat_image, (mouse_click_x - self.GRID_SIZE / 2, 0))
                    else:
                        self.screen.blit(self.mouse_image, (mouse_click_x - self.GRID_SIZE / 2, 0))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Process mouse click
                    pos = pygame.mouse.get_pos()
                    pygame.draw.rect(self.screen, PINK, (0, 0, self.WINDOW_WIDTH, self.GRID_SIZE))
                    if self.start_time == 0:  # Start timer on first move
                        self.start_time = time.time()
                    mouse_click_x = event.pos[0]
                    col = int(math.floor(mouse_click_x / self.GRID_SIZE))
                    if self.check_valid_location(col):
                        row = self.open_row(col)
                        self.drop_chips(row, col, self.current_player)
                        self.drop_sound_player1.play() if self.current_player == 1 else self.drop_sound_player2.play()
                        if self.check_victory(self.current_player):
                            self.display_winner(self.current_player)
                            self.round_finished = True
                            self.turn = 1
                    self.display_board()
                    self.current_player = 3 - self.current_player
                    if self.round_finished:
                        pygame.time.wait(6000)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reset the game when 'r' key is pressed
                        self.reset_game()
            self.display_current_player()

if __name__ == "__main__":
    game = Cat_Mouse_game()
    game.play()
