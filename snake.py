"""
Snake class - Handles snake movement, growth, and collision logic
"""

import pygame

class Snake:
    def __init__(self, start_x, start_y, grid_size):
        self.grid_size = grid_size
        self.body = [(start_x, start_y)]
        self.direction = "RIGHT"
        self.grow_flag = False
        self.alive = True
    
    def head(self):
        return self.body[0]
    
    def move(self):
        head_x, head_y = self.body[0]
        
        if self.direction == "UP":
            new_head = (head_x, head_y - self.grid_size)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + self.grid_size)
        elif self.direction == "LEFT":
            new_head = (head_x - self.grid_size, head_y)
        else:
            new_head = (head_x + self.grid_size, head_y)
        
        self.body.insert(0, new_head)
        
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    
    def grow(self):
        self.grow_flag = True
    
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            if i == 0:
                color = (100, 255, 100)
            else:
                color = (50, 200, 50)
            
            pygame.draw.rect(screen, color, 
                           (segment[0], segment[1], self.grid_size - 1, self.grid_size - 1))