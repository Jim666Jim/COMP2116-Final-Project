"""
COMP2116 Final Project - Snake Game
Main entry point
"""

import pygame
import sys
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
FPS = 10

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game - COMP2116")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game objects
        self.snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, GRID_SIZE)
        self.food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.scoreboard = Scoreboard()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_r and not self.snake.alive:
                    self.reset()
    
    def update(self):
        if self.snake.alive:
            self.snake.move()
            
            # Check food collision
            if self.snake.head() == self.food.position:
                self.snake.grow()
                self.food.respawn(self.snake.body)
                self.scoreboard.increase_score()
            
            # Check wall collision
            head_x, head_y = self.snake.head()
            if (head_x < 0 or head_x >= SCREEN_WIDTH or 
                head_y < 0 or head_y >= SCREEN_HEIGHT):
                self.snake.alive = False
                self.scoreboard.update_high_score()
            
            # Check self collision
            if self.snake.head() in self.snake.body[1:]:
                self.snake.alive = False
                self.scoreboard.update_high_score()
    
    def draw(self):
        self.screen.fill((20, 20, 30))
        
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 50), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 50), (0, y), (SCREEN_WIDTH, y))
        
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.scoreboard.draw(self.screen, SCREEN_WIDTH)
        
        if not self.snake.alive:
            font = pygame.font.Font(None, 48)
            text = font.render("GAME OVER - Press R to Restart", True, (255, 100, 100))
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    def reset(self):
        self.snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, GRID_SIZE)
        self.food.respawn([])
        self.scoreboard.reset_score()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()