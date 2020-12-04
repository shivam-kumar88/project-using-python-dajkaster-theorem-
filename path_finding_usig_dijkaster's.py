import pygame
import math
import os
import random

#colour gradients
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#display setup#######
pygame.init()
WIDTH, HIGHT = 1000, 600
win = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("path finder game using dijkstra's theorm")
win.fill(WHITE)

#letter inside the box
all_words = ['A', 'B', 'C', 'D', 'E']
#word = random.choice(all_words)

#FOR BUTTON VARIABLES
length = 40
wide = 40
gap = 0
size = 9
xaxis, posx = 50, 50
yaxis, posy = 50, 50
ixaxis, iyaxia = 92, 92 # initial x axis and y axis for the info from where the box is starting
verticalsize = 3
WORD_FONT = pygame.font.SysFont('Helvetica', 40)
ltr = "a"
LETTERS_FONTS = pygame.font.SysFont('comicsans', 35)
listofxaxis = []
listofyaxis = []

#sudoku making
colour = RED

def box(colour):
    pygame.draw.rect(win, colour, (xaxis, yaxis, length, wide))
    pygame.draw.line(win, BLACK, ((xaxis + 1), yaxis), ((xaxis + 41), yaxis), 2)
    pygame.draw.line(win, BLACK, (xaxis, (yaxis + 1)), (xaxis, (yaxis + 41)), 2)
    pygame.draw.line(win, BLACK, (xaxis, (yaxis + 41)), ((xaxis + 41), (yaxis + 41)), 2)
    pygame.draw.line(win, BLACK, ((xaxis + 41), yaxis), ((xaxis + 41), (yaxis + 41)), 2)
    listofxaxis.append(xaxis)
    listofyaxis.append(yaxis)

print(listofxaxis)
print(listofyaxis)
def box_letter(colour, ltr, posx, posy):
    text = LETTERS_FONTS.render(ltr, 1, colour)
    win.blit(text, (posx, posy))


# making of the box
box_letter(BLACK, '9*9 BOX with random letters', 100, 25)

# game loop setup
run = True

# for horizontal box
for i in range(0, size):
    xaxis += 42
    for j in range(0, size):
        yaxis = 50 + ((j+1) * 42)
        box(GREEN)
        box_letter(BLACK, random.choice(all_words), (xaxis+7), yaxis)

# changes
# for clicked box
pygame.draw.rect(win, BLUE, (xaxis, (yaxis+20), (length), (wide-20)))




# box_letter(BLACK, random.choice(all_words), (xaxis+7), yaxis)
    # box_letter(BLACK, "3")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)





    pygame.display.update()

