import pygame
import requests
from wordle import words_api
import random

# CONSTANTS
screen_bg_color = [255, 255, 255]
GREEN = [30, 191, 25]
YELLOW = [237, 240, 60]
GRAY = [69, 69, 68]
# Letter class constants
dimensions = 50
no_letter_outline_color = [143, 143, 143]
yes_letter_outline_color = [0, 0, 0]
border_width = 2

# button
reset_button = pygame.Rect(115, 390, 120, 40)

# ---------- WORDLE FUNCTIONALITY -----------
# word the user has to guess
word_of_day = "TRAIT"
# keeps the game loop running
run = True
# wordle grid
wordle_array = []
# The usable alphabetic letters a user can input
alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']
user_row = 0
# is the current wordle finished?
global wordle_finished
wordle_finished = False

def run():
    global word_of_day, run, wordle_array, alphabet, user_row, wordle_finished
    # get a random 5-letter word from the txt file (backup scenario)
    def txt_get_word():
        with open('wordle/five_letter_words.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                global word_of_day
                word_of_day = random.choice(lines).strip().upper()
                print(word_of_day)

    def txt_legit_word(word):
        with open('wordle/five_letter_words.txt', 'r') as file:
            lines = file.readlines()
            # print(lines)
            if word.lower()+"\n" in lines:
                print("True")
                return True
            else:
                print("False")
                return False

    # pygame setup
    pygame.init()
    pygame.font.init()
    # create the game screen
    screen = pygame.display.set_mode((500, 500))
    # Window title
    pygame.display.set_caption('Wordle')
    # fonts
    font = pygame.font.Font('freesansbold.ttf', 32)
    small_font = pygame.font.Font('freesansbold.ttf', 20)

    # wordle letter object
    class Letter:
        def __init__(self, has_letter:bool=False, letter:chr=None):
            self.has_letter = has_letter
            self.letter = letter
            self.row_correct = None
            # status relative to the word of the day
            # possible values include:
            # unknown, not in word, wrong pos, right pos
            self.status = "unknown"
            # if there's a double letter!
            self.double_letter = None

        # draw itself on the screen
        def show(self, x:float, y:float):
            # if the "check word" function has been called and the letters got statuses! (will turn gray, yellow, green, etc)
            if self.status == "right pos":
                if self.double_letter == True and self.row_correct == False:
                    pygame.draw.rect(screen, YELLOW, (x, y, dimensions, dimensions))
                else:
                    pygame.draw.rect(screen, GREEN, (x, y, dimensions, dimensions))
            elif self.status == "wrong pos":
                if self.double_letter == True and self.row_correct == False:
                    pygame.draw.rect(screen, GRAY, (x, y, dimensions, dimensions))
                else:
                    pygame.draw.rect(screen, YELLOW, (x, y, dimensions, dimensions))
            elif self.status == "not in word":
                pygame.draw.rect(screen, GRAY, (x, y, dimensions, dimensions))
            
            # when the user is still inputting their guess
            if self.has_letter == True:
                pygame.draw.rect(screen, yes_letter_outline_color, (x, y, dimensions, dimensions), border_width)
            else:
                pygame.draw.rect(screen, no_letter_outline_color, (x, y, dimensions, dimensions), border_width)
            
            # draw letter
            text = font.render(self.letter, True, (0, 0, 0))
            # text rect is like a thing for text to sit on/be seen on
            textRect = text.get_rect()
            #NOTE: the c and r come from the 2 for loops this function is called in, so be careful here!
            textRect.center = (115 + c*55 + dimensions/2, 50+ r*55 + dimensions/2)
            screen.blit(text, textRect)
            

    # setup
    def setup():
        global wordle_finished, user_row
        # words_api.get_word()
        txt_get_word()
        wordle_finished = False
        user_row = 0
        wordle_array.clear()
        for r in range(0, 6, 1):
            word_array = []
            for c in range(0, 5, 1):
                word_array.append(Letter())
            wordle_array.append(word_array)

    # assigns statuses to different boxes
    def check_word(word_array):             
        word_correct = True
        print(word_of_day)
        for i in range(len(word_array)):
            # first check if the letter is in the correct position
            if word_array[i].letter == word_of_day[i:i+1]:
                print("correct pos!")
                word_array[i].status = "right pos"
            # 2nd, check if letter is in the word
            elif word_array[i].letter in word_of_day:
                print("in there but wrong pos")
                word_correct = False
                word_array[i].status = "wrong pos"
            # if none, then must not be in word
            else:
                print("not there")
                word_array[i].status = "not in word"
                word_correct = False
            # if its not correct, check if its because of double letters
            # find any double letters 
            word = ""
            for i in range(len(word_array)):
                word += word_array[i].letter
            for i in range(len(word_array)):
                count_letter = word.count(word_array[i].letter)
                double_letter = word_array[i].letter
                if count_letter > 1:
                    for c in range(len(word_array)):
                        if word_array[i].letter == double_letter:
                            word_array[i].double_letter = True
                    # check if the word is correct
            print(word)
        if word_correct == True:
            global wordle_finished
            wordle_finished = True
        else:
            for i in range(len(word_array)):
                word_array[i].row_correct = False

    def draw_buttons():
        global reset_button
        # reset button
        pygame.draw.rect(screen, (92, 92, 92), reset_button, width=0, border_radius = 6)
        reset_text = small_font.render("Reset", True, (255, 255, 255))
        reset_rect = reset_text.get_rect()
        reset_rect.center = (175, 410)
        screen.blit(reset_text, reset_rect)

    def button_click():
        x, y = pygame.mouse.get_pos()
        if reset_button.collidepoint(x, y):
            print("Reset!")
            setup()
    # end of function definitions


    setup()
    # draw loop
    while run:
        screen.fill(screen_bg_color)
        # draw the lil boxes
        for r in range(0, 6, 1):
            for c in range(0, 5, 1):
                wordle_array[r][c].show(115 + c*55, 50 + r*55)
        
        draw_buttons()
        # event handler. basically takes all events
        # its seen, runs through them, and then the 
        # if statements we write filters thru them 
        # based on what we want to happen
        for event in pygame.event.get():
            # print(event)
            # close window --> stop running
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # locate the position of the mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Mouse X: {mouse_x}, Mouse Y: {mouse_y}")
                button_click()

            # type in a letter to spell a word
            if event.type == pygame.KEYDOWN and wordle_finished == False:
                # find out which key it was
                print(event.unicode.upper())
                # this turns events/keys you pressed into a string
                key = event.unicode.upper()
                # if the key was "enter/return", check how correct the word is
                # we use event.key because it's not really a character..
                if event.key == pygame.K_RETURN:
                    print("enter key pressed !")
                    # check if all boxes have a letter
                    all_boxes_have_letters = True
                    for i in range(len(wordle_array[user_row])):
                        if wordle_array[user_row][i].has_letter == False:
                            all_boxes_have_letters = False
                    if all_boxes_have_letters == True:
                        word = ""
                        for i in range(len(wordle_array[user_row])):
                            word += wordle_array[user_row][i].letter
                        if txt_legit_word(word):
                            check_word(wordle_array[user_row])
                            if(user_row < 6):
                                user_row += 1
                
                # if the key was "backspace", delete the most recent letter in the word
                if event.key == pygame.K_BACKSPACE:
                    print("backspace pressed")
                    # traverse through the letters in reverse order
                    for i in range(len(wordle_array[user_row])-1, -1, -1):
                        if wordle_array[user_row][i].has_letter == True:
                            wordle_array[user_row][i].has_letter = False
                            wordle_array[user_row][i].letter = None
                            # we only want to adjust the most recent letter of the word (the last written existing letter)
                            # so terminate before the code can get to the previous letters, so it only deletes the most recent
                            break


                # if its not enter, and its some sort of alphabetic letter, fill it into the space
                if key in alphabet:
                    for letter in wordle_array[user_row]:
                        if letter.has_letter == False:
                            print("this box doesn't have a letter and ur pressing key " + key)
                            letter.has_letter = True
                            letter.letter = str(key)
                            # we only want to adjust the first letter of the wordle thats free when we press a button, not the rest.
                            # so terminate before the code can loop through the other letters.
                            # breaks out of the for loop
                            break

        # update the screen
        pygame.display.flip()

    pygame.quit()
