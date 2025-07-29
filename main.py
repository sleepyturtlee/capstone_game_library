import pygame
from pygame.locals import *
import sys
import random

# import game files
from tic_tac_toe import tic_tac_toe

pygame.init()
width = 1100
height = 550
white = (255, 255, 255)
black = (0, 0, 0)
background_color = (101, 181, 201) # light blue
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
screen = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption("Game library")
title_font = pygame.font.Font(None, 100)
button_font = pygame.font.Font(None, 32)
button_rect_left = pygame.Rect(60, 300, 120, 40)
button_rect_middle = pygame.Rect(495, 300, 120, 40)
button_rect_right = pygame.Rect(925, 300, 120, 40)

def draw_title():
    global title_font, random_color
    text = title_font.render("This is a Game Library", True, white, random_color)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 8)
    screen.blit(text, text_rect)

def draw_buttons():
    global button_font, button_rect_left, button_rect_middle, button_rect_right
    pygame.draw.rect(screen, (250, 0, 0), button_rect_left)
    button_text = button_font.render("Tic toe", True, white)
    text_rect = button_text.get_rect(center=button_rect_left.center)
    screen.blit(button_text, text_rect)
    pygame.draw.rect(screen, (250, 0, 0), button_rect_middle)
    button_text = button_font.render("middle", True, white)
    text_rect = button_text.get_rect(center=button_rect_middle.center)
    screen.blit(button_text, text_rect)
    pygame.draw.rect(screen, (250, 0, 0), button_rect_right)
    button_text = button_font.render("right", True, white)
    text_rect = button_text.get_rect(center=button_rect_right.center)
    screen.blit(button_text, text_rect)

def button_click():
    # global random_color
    x, y = pygame.mouse.get_pos()
    if button_rect_left.collidepoint(x, y):
        tic_tac_toe.run()
        # random_color = (
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        # )
    # if button_rect_middle.collidepoint(x, y):
        # random_color = (
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        # )
    # if button_rect_right.collidepoint(x, y):
        # random_color = (
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        #     random.randint(0, 255),
        # )
        return
    

running = True
while running:
    screen.fill(white)
    draw_title()
    draw_buttons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            button_click()
    pygame.display.update()