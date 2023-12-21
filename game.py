#4 by 4 array to represent the facts
#Plus wins. Wins are represented as a list of cards. 
import pygame
import random
from card import Card
import constants

def run_game():
    board = create_board()
    wins = []
    gamestate = (wins, board)
    posns = pos_board(constants.start_x, constants.start_y, constants.inc_x - 15, constants.inc_y - 40, constants.inc_x, constants.inc_y, board)
    
    pygame.init()
    screen = pygame.display.set_mode((1200, 720))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                rc = pos_to_rc(pygame.mouse.get_pos(), posns)
                if rc != -1:
                    board[rc[0]][rc[1]].set_clicked()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gamestate = check_board(gamestate)
                posns = pos_board(constants.start_x, constants.start_y, constants.inc_x - 15, constants.inc_y - 40, constants.inc_x, constants.inc_y, board)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(constants.colors["eerie black"])

        # RENDER YOUR GAME HERE
        draw_game(gamestate, screen)


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
            row += [ordered_board[row_num][col_num]]
            ordered_board[row_num].pop(col_num)
            if ordered_board[row_num] == []:
                ordered_board.pop(row_num)
        board += [row]
    
    return board

#returns a 2dlist of positions
def pos_board(start_x, start_y, width, height, inc_x, inc_y, board):
    posns = []
    x = start_x
    start_y = start_y + (4 - len(board)) * inc_y
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            posn = [(x, start_y), (x + width, start_y + height)]
            row += [posn]
            x += inc_x
        start_y += inc_y
        x = start_x
        posns += [row]
    return posns

#converts a position to a row and column
def pos_to_rc(xy, posns):
    for i in range(len(posns)):
        for j in range(len(posns[0])):
            cur_pos = posns[i][j]
            top_left = cur_pos[0]
            bottom_right = cur_pos[1]
            if top_left[0] <= xy[0] <= bottom_right[0] and top_left[1] <= xy[1] <= bottom_right[1]:
                return (i,j)
    
    return -1

#checks whether the board has produced a winning combo
def check_board(gamestate):
    #find which ones are true
    #if the length of this is not equal to 4, return the same thing.
    #If it is 4, check that the totals are the same.
    #If the totals are the same, something new needs to happen.
    #our gamestate changes I guess.
    clicked = []
    board = gamestate[1]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].clicked:
                clicked += [board[i][j]]
    
    if len(clicked) == 4:
        nums = {card.total for card in clicked}
        if len(nums) == 1:
            #swap the four cards with whatever is in the first row of board.
            gamestate = rearrange(gamestate)
    
    return gamestate

def draw_game(gamestate, screen):
    
    wins = gamestate[0]
    board = gamestate[1]

    colors2 = ["sunset", "cambridge blue", "hooker's green", "light coral"]

    #draws wins
    start_y = constants.start_y
    start_x = constants.start_x
    for i in range(len(wins)):
        rect = pygame.Rect(start_x, start_y, 4 * constants.inc_x - 40, constants.height)
        pygame.draw.rect(screen, constants.colors["green"], rect, 0, 10)
        base_font = pygame.font.Font(None, 90) 
        text = base_font.render(str(wins[i][0].total), True, constants.colors["eerie black"])
        screen.blit(text, (start_x + 50, start_y + 40))
        start_y += constants.inc_y

    #draws board
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j].draw(start_x, start_y, screen)
            start_x += constants.inc_x
        start_y += constants.inc_y
        start_x = constants.start_x
        
#swap the four cards with whatever is in the first row of board.
def rearrange(gamestate):
    #go thru and find indexes of clicked cards and store them in tuples
    #then go thru each one and replace

    wins = gamestate[0]
    board = gamestate[1]

    posns = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].clicked:
                posns += [(i,j)]

    posns2 = [(0,0), (0,1), (0,2), (0,3)]

    for i in range(4):
        swap(posns[i], posns2[i], board)

    wins += [board[0]]
    board.pop(0)
    return [wins, board]
    
def swap(tuple1, tuple2, board):
    #print(board)
    el1 = board[tuple1[0]][tuple1[1]]
    el2 = board[tuple2[0]][tuple2[1]]
    board[tuple1[0]][tuple1[1]] = el2
    board[tuple2[0]][tuple2[1]] = el1

run_game()
