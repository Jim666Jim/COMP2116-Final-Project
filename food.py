"""
Food class - Generates food at random positions
"""

import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, grid_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.position = (0, 0)
        self.respawn([])
    
    def respawn(self, snake_body):
        while True:
            x = random.randrange(0, self.screen_width, self.grid_size)
            y = random.randrange(0, self.screen_height, self.grid_size)
            self.position = (x, y)
            
            if self.position not in snake_body:
                break
    
    def draw(self, screen):
        center_x = self.position[0] + self.grid_size // 2
        center_y = self.position[1] + self.grid_size // 2
        pygame.draw.circle(screen, (255, 50, 50), (center_x, center_y), self.grid_size // 2 - 2)