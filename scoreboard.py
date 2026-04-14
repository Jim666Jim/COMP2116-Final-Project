"""
Scoreboard class - Tracks current score and high score
"""

import pygame
import os

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
    
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return 0
    
    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
    
    def increase_score(self):
        self.score += 10
    
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def reset_score(self):
        self.score = 0
    
    def draw(self, screen, screen_width):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (200, 200, 200))
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (screen_width - high_score_text.get_width() - 10, 10))