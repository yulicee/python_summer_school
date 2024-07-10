import pygame
import sys
import random

# Pygame initialization
pygame.init()

# Constants and configurations
WINDOW_SIZE = (600, 600)
CARD_SIZE = (100, 100)
CARD_PADDING = 10
WINDOW_COLOR = (240, 240, 240)    # Light grey background
CARD_COLOR = (210, 210, 210)      # Slightly darker light grey for card color
FONT_COLOR = (0, 0, 0)            # Black font color
BACKGROUND_COLOR = (100, 100, 100)  # Dark grey background for the cards
TEXT_COLOR = (0, 0, 0)            # Black text color

# Pygame setup
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Memory Card Game")
clock = pygame.time.Clock()

# File to store high score
HIGH_SCORE_FILE = "high_score.txt"

class Card:
    def __init__(self, x, y, id):
        self.rect = pygame.Rect(x, y, CARD_SIZE[0], CARD_SIZE[1])
        self.open = False
        self.id = id
        self.opening_time = None  

    def draw(self, screen):
        """Draw a card on the screen."""
        pygame.draw.rect(screen, CARD_COLOR if self.open else BACKGROUND_COLOR, self.rect)

        if self.open:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.id), True, FONT_COLOR)
            screen.blit(text, (self.rect.x + CARD_SIZE[0] // 2 - text.get_width() // 2,
                               self.rect.y + CARD_SIZE[1] // 2 - text.get_height() // 2))

    def start_opening(self):
        self.opening_time = pygame.time.get_ticks()

    def is_opening_finished(self):
        if self.opening_time is None:
            return False
        elapsed_time = pygame.time.get_ticks() - self.opening_time
        return elapsed_time >= 500

    def open_card(self):
        self.open = True

    def close_card(self):
        self.open = False
        self.opening_time = None  

class Main:
    def __init__(self):
        self.high_score = self.load_high_score()
        self.reset_game()
        self.show_input_prompt = True
        self.input_text = ''
        self.prompt_type = 'rounds'
        self.game_finished = False
        self.restart_or_quit_prompt = False

    def reset_game(self):
        """Reset game state for a new round."""
        self.cards = []
        self.card_ids = ["lion", "dog", "cat", "tiger", "mouse", "snake", "rhino", "fish"] * 2
        random.shuffle(self.card_ids)
        self.create_cards()
        self.opened_cards = []
        self.moves = 0
        self.matched_pairs = 0
        self.game_finished = False
        self.restart_or_quit_prompt = False

    def create_cards(self):
        """Create card objects based on shuffled card IDs."""
        num_columns = 4
        num_rows = 4
        total_width = num_columns * CARD_SIZE[0] + (num_columns - 1) * CARD_PADDING
        total_height = num_rows * CARD_SIZE[1] + (num_rows - 1) * CARD_PADDING
        start_x = (WINDOW_SIZE[0] - total_width) // 2
        start_y = (WINDOW_SIZE[1] - total_height) // 2

        for i in range(num_rows):
            for j in range(num_columns):
                if self.card_ids:
                    card_id = self.card_ids.pop()
                else:
                    card_id = "empty"
                x = start_x + j * (CARD_SIZE[0] + CARD_PADDING)
                y = start_y + i * (CARD_SIZE[1] + CARD_PADDING)
                card = Card(x, y, card_id)
                self.cards.append(card)

    def check_matching_cards(self):
        """Check if two opened cards have the same ID."""
        if len(self.opened_cards) == 2:
            card1, card2 = self.opened_cards
            if card1.id == card2.id:
                self.opened_cards = []
                self.matched_pairs += 1
                if self.matched_pairs == len(self.cards) // 2:
                    self.game_finished = True
                    self.show_restart_or_quit_prompt()
                    self.print_game_result()
            else:
                pygame.time.set_timer(pygame.USEREVENT, 500)

    def show_restart_or_quit_prompt(self):
        """Set the flag to show the restart or quit prompt."""
        self.restart_or_quit_prompt = True

    def handle_restart_or_quit_prompt(self):
        """Handle user input for restart or quit prompt."""
        if self.input_text.lower() in ['', 'y', 'yes']:
            self.restart_game()
        elif self.input_text.lower() in ['n', 'no']:
            pygame.quit()
            sys.exit()

    def handle_match_delay(self):
        """Close unmatched cards after a delay."""
        pygame.time.set_timer(pygame.USEREVENT, 0)
        for card in self.opened_cards:
            card.close_card()
        self.opened_cards = []

    def handle_card_click(self, card):
        """Handle click event on cards."""
        if not card.open and len(self.opened_cards) < 2 and not self.game_finished and not self.restart_or_quit_prompt:
            card.open_card()
            card.start_opening()
            self.opened_cards.append(card)
            self.moves += 1
            if len(self.opened_cards) == 2:
                self.check_matching_cards()
                if not self.opened_cards:
                    pygame.time.set_timer(pygame.USEREVENT, 500)

    def print_game_result(self):
        """Print game result and update high score."""
        print(f"Game finished in {self.moves} moves.")
        if self.moves < self.high_score:
            self.high_score = self.moves
            self.save_high_score(self.high_score)
            print(f"New best score: {self.high_score} moves!")
        else:
            print(f"Best score remains: {self.high_score} moves.")

    def handle_input(self, event):
        """Handle user input for prompts."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.prompt_type == 'rounds':
                    if self.input_text.isdigit():
                        self.total_games = max(1, int(self.input_text))
                        self.input_text = ''
                        self.show_input_prompt = False
                        self.prompt_type = None
                        self.reset_game()
                    else:
                        self.input_text = ''
                elif self.restart_or_quit_prompt:
                    self.handle_restart_or_quit_prompt()

            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def draw_input_prompt(self):
        """Draw the input prompt on the screen."""
        prompt_text = ''
        if self.prompt_type == 'rounds':
            prompt_text = f"How many rounds do you want to play?: {self.input_text}"
        elif self.restart_or_quit_prompt:
            prompt_text = "Do you want to restart the game? (Y/n): " + self.input_text
        font_size = self.get_dynamic_font_size(prompt_text)
        font = pygame.font.Font(None, font_size)
        prompt_surf = font.render(prompt_text, True, TEXT_COLOR)
        screen.blit(prompt_surf, (WINDOW_SIZE[0] // 2 - prompt_surf.get_width() // 2, WINDOW_SIZE[1] // 2))

    def get_dynamic_font_size(self, text):
        """Calculate dynamic font size to fit window width."""
        max_width = WINDOW_SIZE[0] - 20
        font_size = 36
        font = pygame.font.Font(None, font_size)
        while font.size(text)[0] > max_width and font_size > 12:
            font_size -= 1
            font = pygame.font.Font(None, font_size)
        return font_size

    def draw_scores(self):
        """Draw current moves and high score."""
        font = pygame.font.Font(None, 36)
        moves_text = f"Moves: {self.moves}"
        high_score_text = f"Best Score: {self.high_score}"
        
        moves_surf = font.render(moves_text, True, TEXT_COLOR)
        high_score_surf = font.render(high_score_text, True, TEXT_COLOR)
        
        screen.blit(moves_surf, (10, 10))
        screen.blit(high_score_surf, (10, 50))

    def load_high_score(self):
        """Load high score from file."""
        try:
            with open(HIGH_SCORE_FILE, 'r') as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return float('inf')

    def save_high_score(self, score):
        """Save high score to file."""
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(score))

    def restart_game(self):
        """Reset all game states to restart the game."""
        self.reset_game()
        self.restart_or_quit_prompt = False
        self.show_input_prompt = True
        self.prompt_type = 'rounds'


# Initialize the game
main = Main()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif main.show_input_prompt:
            main.handle_input(event)
        elif main.restart_or_quit_prompt:
            main.handle_input(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for card in main.cards:
                if card.rect.collidepoint(mouse_x, mouse_y):
                    main.handle_card_click(card)
        elif event.type == pygame.USEREVENT:
            main.handle_match_delay()

    # Clear the screen
    screen.fill(WINDOW_COLOR)

    # Draw cards
    for card in main.cards:
        card.draw(screen)

    # Draw prompts or scores
    if main.show_input_prompt or main.restart_or_quit_prompt:
        main.draw_input_prompt()
    else:
        main.draw_scores()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
