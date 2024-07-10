import pygame
import sys
import random
from pygame.math import Vector2
from pygame import mixer

class Fruit:
    def __init__(self, snake):
        self.snake = snake
        self.randomize()

    def draw(self, screen):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple_img, fruit_rect)

    def randomize(self):
        while True:
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.pos = Vector2(self.x, self.y)
            if self.pos not in self.snake.body:
                break

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 3), Vector2(5, 3), Vector2(4, 3)]
        self.direction = Vector2(1, 0)
        self.block = False
        self.speed = 5  

    def draw(self, screen):
        for block in self.body:
            snake_block = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, snake_color, snake_block)

    def move(self):
        if self.block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.block = True

    def increase_speed(self):
        self.speed += 1  

    def get_speed(self):
        return self.speed

class Main:
    def __init__(self):
        self.snake = Snake()
        self.apple = Fruit(self.snake)
        self.apple_count = 0  
        self.high_score = self.load_high_score()  
        self.update_speed() 
        self.game_over = False  

    def update(self):
        if not self.game_over:
            self.snake.move()
            self.check_collision()
            self.check_fail()

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)
        self.draw_apple_count(screen)  
        self.draw_high_score(screen)  
        if self.game_over:
            self.draw_game_over(screen)  

    def draw_apple_count(self, screen):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Apples: {self.apple_count}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    def draw_high_score(self, screen):
        font = pygame.font.Font(None, 30)
        text = font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
        screen.blit(text, (10, 40))

    def draw_game_over(self, screen):
        font = pygame.font.Font(None, 80)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (cell_size * cell_number // 2 - game_over_text.get_width() // 2, cell_size * cell_number // 2 - game_over_text.get_height() // 2))

        font = pygame.font.Font(None, 40)
        prompt_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        screen.blit(prompt_text, (cell_size * cell_number // 2 - prompt_text.get_width() // 2, cell_size * cell_number // 2 + game_over_text.get_height() // 2))

    def check_collision(self):
        if self.apple.pos == self.snake.body[0]:
            self.apple.randomize()
            self.snake.add_block()
            mixer.music.play()
            self.snake.increase_speed()  
            self.apple_count += 1  
            self.update_speed()  

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.set_game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.set_game_over()

    def set_game_over(self):
        if self.apple_count > self.high_score:
            self.high_score = self.apple_count
            self.save_high_score(self.high_score)  
        self.game_over = True

    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open("high_score.txt", 'r') as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0  

    def save_high_score(self, score):
        """Save the high score to a file."""
        with open("high_score.txt", 'w') as file:
            file.write(str(score))

    def update_speed(self):
        """Update the game speed based on the snake's current speed."""
        new_interval = max(100, 500 - (self.snake.get_speed() - 5) * 20)
        pygame.time.set_timer(SCREEN_UPDATE, new_interval)

pygame.init()
mixer.init()
mixer.music.load("eating.mp3")
mixer.music.set_volume(0.7)

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 500)

main_game = Main()

apple_img = pygame.image.load('apple.webp').convert_alpha()

# Define colors
background_color = (173, 216, 230)  # Light blue
snake_color = (255, 165, 0)  # Warm orange

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if not main_game.game_over:
                if event.key == pygame.K_UP and main_game.snake.direction.y == 0:
                    main_game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and main_game.snake.direction.y == 0:
                    main_game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_RIGHT and main_game.snake.direction.x == 0:
                    main_game.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_LEFT and main_game.snake.direction.x == 0:
                    main_game.snake.direction = Vector2(-1, 0)
            else:
                if event.key == pygame.K_r:
                    main_game = Main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    screen.fill(background_color)  
    main_game.draw(screen)
    pygame.display.update()
    clock.tick(main_game.snake.get_speed()) 
