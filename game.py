#4 by 4 array to represent the facts
import pygame
import random
from card import Card
import constants

def run_game():
    board = create_board()
    
    pygame.init()
    screen = pygame.display.set_mode((1200, 720))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #if event.type == pygame.MOUSEBUTTONDOWN: 

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(constants.colors["eerie black"])

        # RENDER YOUR GAME HERE
        start_y = 60
        start_x = 50
        for i in range(4):
            for j in range(4):
                board[i][j].draw(start_x, start_y, screen, )
                start_x += 285
            start_y += 170
            start_x = 50


        # flip() the display to put your work on screen
        pygame.display.flip()

pygame.quit()


#creates the board
def create_board():
    nums = [8,9,10]

    ordered_board = [[Card(0,7), Card(1,6), Card(2,5), Card(3,4)]]
    
    for i in range(3):
        row = []
        num = nums[i]
        nums_used = []
        for j in range(4):
            num1 = random.randint(1,num - 1)
            while num1 in nums_used:
                num1 = random.randint(1,num - 1)
            num2 = num - num1
            nums_used += [num1, num2]
            row += [Card(num1, num2)]

        ordered_board += [row]

    #Board has been made, now it needs to be reordered
    board = []
    for i in range(4):
        row = []
        for j in range(4):
            row_num = random.randint(0,len(ordered_board) - 1)
            col_num = random.randint(0,len(ordered_board[row_num]) - 1)
            #print(ordered_board[row_num][col_num])
            row += [ordered_board[row_num][col_num]]
            ordered_board[row_num].pop(col_num)
            if ordered_board[row_num] == []:
                ordered_board.pop(row_num)
        board += [row]
    
    return board


run_game()