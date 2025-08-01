import pygame
from pygame.locals import *
import sys
import random
import math

# import game files
import hangman.hangman
from tic_tac_toe import tic_tac_toe
import hangman
from wordle import wordle

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

clock = pygame.time.Clock()

def draw_title():
    global title_font, random_color
    text = title_font.render("This is a Game Library", True, white, random_color)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 8)
    screen.blit(text, text_rect)

def draw_buttons():
    global button_font, button_rect_left, button_rect_middle, button_rect_right
    pygame.draw.rect(screen, (250, 0, 0), button_rect_left)
    button_text = button_font.render("Tic Tac toe", True, white)
    text_rect = button_text.get_rect(center=button_rect_left.center)
    screen.blit(button_text, text_rect)
    pygame.draw.rect(screen, (250, 0, 0), button_rect_middle)
    button_text = button_font.render("Hangman", True, white)
    text_rect = button_text.get_rect(center=button_rect_middle.center)
    screen.blit(button_text, text_rect)
    pygame.draw.rect(screen, (250, 0, 0), button_rect_right)
    button_text = button_font.render("Wordle", True, white)
    text_rect = button_text.get_rect(center=button_rect_right.center)
    screen.blit(button_text, text_rect)

def button_click():
    # global random_color
    x, y = pygame.mouse.get_pos()
    if button_rect_left.collidepoint(x, y):
        tic_tac_toe.run()
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    if button_rect_middle.collidepoint(x, y):
        hangman.hangman.run()
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    if button_rect_right.collidepoint(x, y):
        wordle.run()
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        return
    

class Dot:
    def __init__(self):
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)
        self.radius = random.randint(2, 6)
        self.speed = random.uniform(0.1, 0.5)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        angle = random.uniform(0, 2 * math.pi)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


dots = []
dots_num = 100
for i in range(dots_num):
    dots.append(Dot())



running = True
while running:
    screen.fill(white)

    for i in range(len(dots)):
        dots[i].update()
        dots[i].draw(screen)

    clock.tick(60)
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
