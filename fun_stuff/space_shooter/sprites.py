import pygame
import random
from constants import WIDTH, HEIGHT, WHITE

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/spaceship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 7  # Speed of the spaceship

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(self.game.screen.get_rect()) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()  

class Star(pygame.sprite.Sprite):
    def __init__(self, game, left_bound, right_bound):
        super().__init__()
        size = random.randint(5, 15)  
        self.image = self.create_star_image(size)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = random.randint(left_bound, right_bound - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, HEIGHT // 2)
        self.speed = 2 + (self.game.level - 1) * 0.5  

    def create_star_image(self, size):
        star_image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(star_image, WHITE, (size // 2, size // 2), size // 2)
        return star_image

    def update(self):
        self.rect.y += self.speed
        if self.rect.colliderect(self.game.spaceship.rect):
            self.game.lives -= 1
            self.kill()
            if self.game.lives <= 0:
                self.game.game_over = True
            else:
                self.game.create_new_stars(1)
        elif self.rect.y > HEIGHT:
            self.kill()
            if self.game.lives > 0:
                self.game.create_new_stars(1)
