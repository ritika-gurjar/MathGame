#each card needs to have a fact
import pygame

class Card:

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1
    
    @property
    def num2(self):
        return self._num2
    
    @property
    def total(self):
        return self.num1 + self.num2
        
    def __str__(self):
        return "Card: " + str(self.num1) + " + " + str(self.num2) + " = " + str(self.total)
    
    def __repr__(self):
        return str(self)
    
    def rect(self, left, top, width, height):
        return pygame.Rect(left, top, width, height)
    
    def text(self):
        base_font = pygame.font.Font(None, 32) 
        return base_font.render(self.clue(), True, "#1C1D21") 
    
    def clue(self):
        return "Card: " + str(self.num1) + " + " + str(self.num2)



    
