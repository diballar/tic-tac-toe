import pygame
import keyboard
import sys
import random
from threading import Thread
import os
import time

path = os.path.realpath(__file__)
file_name = os.path.basename(path)
path = path.replace(file_name, '')
os.chdir(path)

def thread(target, daemon_q):
        thread0 = Thread(target= target)
        if daemon_q == True:
            thread0.daemon = True
        else: thread0.daemon = False
        thread0.start

def draw_stuff():
    screen.fill(blue)
    
    for i in pos_x:
            if i == True:
                if i == topl_x:
                    x_rect.topleft = 50, 50
                    screen.blit(x, x_rect)
                if i == top_x:
                    x_rect.top = 50
                    x_rect.centerx = width / 2
                    screen.blit(x, x_rect)
                if i == topr_x:
                    x_rect.topright = width - 50, 50
                    screen.blit(x, x_rect)
                if i == left_x:
                    x_rect.left = 50
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == center_x:
                    x_rect.centerx = width / 2
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == right_x:
                    x_rect.right = width - 50
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == lowl_x:
                    x_rect.bottomleft = 50, height - 50
                    screen.blit(x, x_rect)
                if i == low_x:
                    x_rect.centerx = width / 2
                    x_rect.bottom = height - 50
                    screen.blit(x, x_rect)
                if i == lowr_x:
                    x_rect.bottomright = width - 50, height - 50
                    screen.blit(x, x_rect)
    for p in pos_o:
            if p == True:
                if p == topl_o:
                    o_rect.topleft = 50, 50
                    screen.blit(o, o_rect)
                if p == top_o:
                    o_rect.top = 50
                    o_rect.centerx = width / 2
                    screen.blit(o, o_rect)
                if p == topr_o:
                    o_rect.topright = width - 50, 50
                    screen.blit(o, o_rect)
                if p == left_o:
                    o_rect.left = 50
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == center_o:
                    o_rect.centerx = width / 2
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == right_o:
                    o_rect.right = width - 50
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == lowl_o:
                    o_rect.bottomleft = 50, height - 50
                    screen.blit(o, o_rect)
                if p == low_o:
                    o_rect.centerx = width / 2
                    o_rect.bottom = height - 50
                    screen.blit(o, o_rect)
                if p == lowr_o:
                    o_rect.bottomright = width - 50, height - 50
                    screen.blit(o, o_rect)

    line2.centerx = (width / 3) * 2
    line2.centery = height / 2
    pygame.draw.rect(screen, white, line2)

    line2.centerx = (width / 3)
    pygame.draw.rect(screen, white, line2)

    line1.centerx = width / 2
    line1.centery = height / 3
    pygame.draw.rect(screen, white, line1)

    line1.centery = (height / 3) * 2
    pygame.draw.rect(screen, white, line1)


blue = (65, 105, 225)

white = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption("Basic Pygame Main Loop")

won_q = 0

x = pygame.image.load("funi.png")
x_rect = x.get_rect()

o = pygame.image.load("funo.png")
o_rect = o.get_rect()

win_screen = pygame.image.load("win_screen.png")
win_rect = win_screen.get_rect(center = (width // 2, height // 2))

font = pygame.font.Font(None, 36)
text_render = font.render(f"{won_q}", False, white)
text_rect = text_render.get_rect(center = (width // 2, height - 50))

line1 = pygame.rect.Rect(0, 0, width - 100, 20)
line2 = pygame.rect.Rect(0, 0, 20, height - 100)

topl_x, top_x, topr_x, left_x, center_x, right_x, lowl_x, low_x, lowr_x = False, False, False, False, False, False, False, False, False
topl_o, top_o, topr_o, left_o, center_o, right_o, lowl_o, low_o, lowr_o = False, False, False, False, False, False, False, False, False

pos_x = [topl_x, top_x, topr_x,
    left_x, center_x, right_x,
    lowl_x, low_x, lowr_x]

pos_o = [topl_o, top_o, topr_o,
    left_o, center_o, right_o,
    lowl_o, low_o, lowr_o]


turn_x = True
game_play = True

rowt_x = topl_x, top_x, topr_x
rowc_x = left_x, center_x, right_x
rowl_x = lowl_x, low_x, lowr_x
coll_x = topl_x, left_x, lowl_x
colc_x = top_x, center_x, low_x
colr_x = topr_x, right_x, lowr_x
diag1_x = topl_x, center_x, lowr_x
diag2_x = topr_x, center_x, lowl_x

rowt_o = topl_o, top_o, topr_o
rowc_o = left_o, center_o, right_o
rowl_o = lowl_o, low_o, lowr_o
coll_o = topl_o, left_o, lowl_o
colc_o = top_o, center_o, low_o
colr_o = topr_o, right_o, lowr_o
diag1_o = topl_o, center_o, lowr_o
diag2_o = topr_o, center_o, lowl_o

# Main loop
os.system('cls')
while True:

    draw_stuff()
    pygame.display.flip()

    rowt_x = topl_x, top_x, topr_x
    rowc_x = left_x, center_x, right_x
    rowl_x = lowl_x, low_x, lowr_x
    coll_x = topl_x, left_x, lowl_x
    colc_x = top_x, center_x, low_x
    colr_x = topr_x, right_x, lowr_x
    diag1_x = topl_x, center_x, lowr_x
    diag2_x = topr_x, center_x, lowl_x

    rowt_o = topl_o, top_o, topr_o
    rowc_o = left_o, center_o, right_o
    rowl_o = lowl_o, low_o, lowr_o
    coll_o = topl_o, left_o, lowl_o
    colc_o = top_o, center_o, low_o
    colr_o = topr_o, right_o, lowr_o
    diag1_o = topl_o, center_o, lowr_o
    diag2_o = topr_o, center_o, lowl_o

    if rowt_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if rowc_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if rowl_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if coll_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if colc_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if colr_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if diag1_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"
    if diag2_x == (True, True, True):
        game_play = False
        won_q = "x's won!, restarting in 3 seconds"

    if rowt_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if rowc_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if rowl_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if coll_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if colc_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if colr_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if diag1_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"
    if diag2_o == (True, True, True):
        game_play = False
        won_q = "o's won!, restarting in 3 seconds"

    # Update game logic here
    pos_x = [topl_x, top_x, topr_x,
    left_x, center_x, right_x,
    lowl_x, low_x, lowr_x]

    pos_o = [topl_o, top_o, topr_o,
    left_o, center_o, right_o,
    lowl_o, low_o, lowr_o]
    

    # Draw game elements here
    
    for i in pos_x:
            if i == True:
                if i == topl_x:
                    x_rect.topleft = 50, 50
                    screen.blit(x, x_rect)
                if i == top_x:
                    x_rect.top = 50
                    x_rect.centerx = width / 2
                    screen.blit(x, x_rect)
                if i == topr_x:
                    x_rect.topright = width - 50, 50
                    screen.blit(x, x_rect)
                if i == left_x:
                    x_rect.left = 50
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == center_x:
                    x_rect.centerx = width / 2
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == right_x:
                    x_rect.right = width - 50
                    x_rect.centery = height / 2
                    screen.blit(x, x_rect)
                if i == lowl_x:
                    x_rect.bottomleft = 50, height - 50
                    screen.blit(x, x_rect)
                if i == low_x:
                    x_rect.centerx = width / 2
                    x_rect.bottom = height - 50
                    screen.blit(x, x_rect)
                if i == lowr_x:
                    x_rect.bottomright = width - 50, height - 50
                    screen.blit(x, x_rect)
    for p in pos_o:
            if p == True:
                if p == topl_o:
                    o_rect.topleft = 50, 50
                    screen.blit(o, o_rect)
                if p == top_o:
                    o_rect.top = 50
                    o_rect.centerx = width / 2
                    screen.blit(o, o_rect)
                if p == topr_o:
                    o_rect.topright = width - 50, 50
                    screen.blit(o, o_rect)
                if p == left_o:
                    o_rect.left = 50
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == center_o:
                    o_rect.centerx = width / 2
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == right_o:
                    o_rect.right = width - 50
                    o_rect.centery = height / 2
                    screen.blit(o, o_rect)
                if p == lowl_o:
                    o_rect.bottomleft = 50, height - 50
                    screen.blit(o, o_rect)
                if p == low_o:
                    o_rect.centerx = width / 2
                    o_rect.bottom = height - 50
                    screen.blit(o, o_rect)
                if p == lowr_o:
                    o_rect.bottomright = width - 50, height - 50
                    screen.blit(o, o_rect)
    pygame.display.flip()
            
    if game_play:
        if turn_x:
            ans = input("x's turn: ").lower()
            if ans == "quit":
                pygame.quit()
                sys.exit()
            if ans == "reset":
                topl_x, top_x, topr_x, left_x, center_x, right_x, lowl_x, low_x, lowr_x = False, False, False, False, False, False, False, False, False
                topl_o, top_o, topr_o, left_o, center_o, right_o, lowl_o, low_o, lowr_o = False, False, False, False, False, False, False, False, False
                os.system('cls')
            if ans == "topleft":
                if topl_x == False and topl_o == False:
                    topl_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "topcenter":
                if top_x == False and top_o == False:
                    top_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "topright":
                if topr_x == False and topr_o == False:
                    topr_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "centerleft":
                if left_x == False and left_o == False:
                    left_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "center":
                if center_x == False and center_o == False:
                    center_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "centerright":
                if right_x == False and right_o == False:
                    right_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomleft":
                if lowl_x == False and lowl_o == False:
                    lowl_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomcenter":
                if low_x == False and low_o == False:
                    low_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomright":
                if lowr_x == False and lowr_o == False:
                    lowr_x = True
                    turn_x = False
                    draw_stuff()
                else: print("invalid move")
        else:
            ans = input("o's turn: ").lower()
            if ans == "quit":
                pygame.quit()
                sys.exit()
            if ans == "reset":
                topl_x, top_x, topr_x, left_x, center_x, right_x, lowl_x, low_x, lowr_x = False, False, False, False, False, False, False, False, False
                topl_o, top_o, topr_o, left_o, center_o, right_o, lowl_o, low_o, lowr_o = False, False, False, False, False, False, False, False, False
                os.system('cls')
            if ans == "topleft":
                if topl_x == False and topl_o == False:
                    topl_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "topcenter":
                if top_x == False and top_o == False:
                    top_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "topright":
                if topr_x == False and topr_o == False:
                    topr_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "centerleft":
                if left_x == False and left_o == False:
                    left_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "center":
                if center_x == False and center_o == False:
                    center_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "centerright":
                if right_x == False and right_o == False:
                    right_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomleft":
                if lowl_x == False and lowl_o == False:
                    lowl_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomcenter":
                if low_x == False and low_o == False:
                    low_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
            if ans == "bottomright":
                if lowr_x == False and lowr_o == False:
                    lowr_o = True
                    turn_x = True
                    draw_stuff()
                else: print("invalid move")
    else:
        draw_stuff()
        screen.blit(win_screen, win_rect)
        text_render = font.render(f"{won_q}", False, white)
        text_rect = text_render.get_rect(center = (width // 2, height - 50))
        screen.blit(text_render, text_rect)
        pygame.display.flip()
        time.sleep(3)
        topl_x, top_x, topr_x, left_x, center_x, right_x, lowl_x, low_x, lowr_x = False, False, False, False, False, False, False, False, False
        topl_o, top_o, topr_o, left_o, center_o, right_o, lowl_o, low_o, lowr_o = False, False, False, False, False, False, False, False, False
        game_play = True
        os.system('cls')

    # Set the frames per second
    pygame.time.Clock().tick(60)

    pygame.display.flip()
