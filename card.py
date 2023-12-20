#each card needs to have a fact
import pygame
import constants

class Card:

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self.clicked = False

    @property
    def num1(self):
        return self._num1
    
    @property
    def num2(self):
        return self._num2
    
    @property
    def total(self):
        return self.num1 + self.num2
    
    def set_clicked(self):
        self.clicked = not self.clicked
        
    def __str__(self):
        return "Card: " + str(self.num1) + " + " + str(self.num2) + " = " + str(self.total)
    
    def __repr__(self):
        return str(self)
    
    def rect(self, left, top, width, height):
        return pygame.Rect(left, top, width, height)
    
    def text(self):
        base_font = pygame.font.Font(None, 90) 
        return base_font.render(self.clue(), True, constants.colors["burnt umber"]) 
    
    def clue(self):
        return str(self.num1) + " + " + str(self.num2)
    
    def draw(self, start_x, start_y, screen):
        if not self.clicked:
            pygame.draw.rect(screen, constants.colors["buff"], self.rect(start_x, start_y, 250, 130), 0, 10)
        else:
            pygame.draw.rect(screen, constants.colors["bronze"], self.rect(start_x, start_y, 250, 130), 0, 10)
        screen.blit(self.text(), (start_x + 50, start_y + 40))



    
