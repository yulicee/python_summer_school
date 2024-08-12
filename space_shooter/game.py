import pygame
import sys
import os
from sprites import Spaceship, Bullet, Star
from constants import WIDTH, HEIGHT, WHITE, BLACK, RED

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Shooter")
        self.font = pygame.font.Font(None, 36)
        self.load_assets()
        self.spaceship_speed = 7  # Define spaceship speed here
        self.reset_game()

    def load_assets(self):
        self.background = pygame.image.load('assets/background.jpg')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.laser_sound = pygame.mixer.Sound('assets/laser.wav')
        self.explosion_sound = pygame.mixer.Sound('assets/explosion.wav')
        self.high_score = self.read_high_score()

    def read_high_score(self):
        """Read the high score from the file."""
        HIGH_SCORE_FILE = "highscore.txt"
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        return 0

    def write_high_score(self, score):
        """Write the high score to the file."""
        HIGH_SCORE_FILE = "highscore.txt"
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))

    def get_star_spawn_area(self):
        """Return the horizontal bounds for star spawning based on spaceship position."""
        left_bound = max(self.spaceship.rect.centerx - WIDTH // 4, 0)
        right_bound = min(self.spaceship.rect.centerx + WIDTH // 4, WIDTH)
        return left_bound, right_bound

    def create_new_stars(self, count):
        for _ in range(count):
            star = Star(self)
            self.all_sprites.add(star)
            self.stars.add(star)

    def increase_level(self):
        self.level += 1
        self.create_new_stars(self.level)

    def game_over_screen(self):
        self.screen.blit(self.background, (0, 0))
        game_over_text = self.font.render(f"Game Over! Final Score: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)
        restart_text = self.font.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        self.screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))
        pygame.display.flip()

    def reset_game(self):
        self.level = 1
        self.score = 0
        self.lives = 5
        self.game_over = False
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.spaceship = Spaceship(self)
        self.create_new_stars(self.level)
        self.countdown()
        self.show_instructions()

    def show_instructions(self):
        """Display game instructions."""
        self.screen.blit(self.background, (0, 0))
        instructions_font = pygame.font.Font(None, 36)
        instructions = [
            "Welcome to Space Shooter!",
            "Use ARROW KEYS to move.",
            "Press SPACE to shoot.",
            "Avoid the stars and shoot them for points.",
            "You have 5 lives. Game over when you run out.",
            "Press 'R' to restart or 'Q' to quit after game over."
        ]
        for i, line in enumerate(instructions):
            text = instructions_font.render(line, True, WHITE)
            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100 + i * 30))
        pygame.display.flip()
        pygame.time.wait(5000)  # Show instructions for 5 seconds

    def countdown(self):
        """Display a countdown timer before the game starts."""
        countdown_font = pygame.font.Font(None, 74)
        for i in range(3, 0, -1):
            self.screen.blit(self.background, (0, 0))
            countdown_text = countdown_font.render(str(i), True, WHITE)
            self.screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2 - countdown_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(1000)  # Wait for 1 second

        self.screen.blit(self.background, (0, 0))
        ready_text = countdown_font.render("Go!", True, WHITE)
        self.screen.blit(ready_text, (WIDTH // 2 - ready_text.get_width() // 2, HEIGHT // 2 - ready_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.laser_sound.play()
                        bullet = Bullet(self.spaceship.rect.centerx, self.spaceship.rect.top)
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)
                    if event.key == pygame.K_r and self.game_over:
                        self.reset_game()
                    if event.key == pygame.K_q and self.game_over:
                        pygame.quit()
                        sys.exit()

            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.spaceship.move(-self.spaceship_speed, 0)
                if keys[pygame.K_RIGHT]:
                    self.spaceship.move(self.spaceship_speed, 0)
                if keys[pygame.K_UP]:
                    self.spaceship.move(0, -self.spaceship_speed)
                if keys[pygame.K_DOWN]:
                    self.spaceship.move(0, self.spaceship_speed)

                self.all_sprites.update()

                for bullet in self.bullets:
                    hit_stars = pygame.sprite.spritecollide(bullet, self.stars, True)
                    for star in hit_stars:
                        self.explosion_sound.play()
                        self.score += 10
                        bullet.kill()
                        if not self.stars:
                            self.increase_level()

                if self.lives <= 0:
                    self.game_over = True
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.write_high_score(self.high_score)

                self.screen.blit(self.background, (0, 0))
                self.all_sprites.draw(self.screen)
                score_text = self.font.render(f"Score: {self.score}", True, WHITE)
                level_text = self.font.render(f"Level: {self.level}", True, WHITE)
                lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
                self.screen.blit(score_text, (10, 10))
                self.screen.blit(level_text, (10, 40))
                self.screen.blit(lives_text, (10, 70))
                self.screen.blit(self.spaceship.image, self.spaceship.rect)
                pygame.display.flip()
                pygame.time.Clock().tick(30)  # 30 frames per second
            else:
                self.game_over_screen()
