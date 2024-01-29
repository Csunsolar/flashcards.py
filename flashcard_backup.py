import pygame
import random
from sys import exit
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename(title="Select a CSV file with Row 1 as Headers. All following rows should be terms in column A and defintions in column B.")

with open(path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    term_dict = {}
    for row in reader:
        term = row[headers[0]]
        dictionary = row[headers[1]]
        term_dict[term] = dictionary

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Flash Cards')
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("Arial", 20)

current_question = ""
current_answer = ""
card_turned = False
rand_on = False
index = 0
random_list = list(term_dict.items())
random.shuffle(random_list)
Rterm_dict = dict(random_list)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
  
            pygame.quit()
            exit()
            # used this to close code bc quiting pygame and then trying to use pygames display update below would error out
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                card_turned = not card_turned
            elif event.key == pygame.K_RIGHT and index < len(term_dict) - 1:
                index += 1
                card_turned = False
            elif event.key == pygame.K_LEFT and index > 0:
                index -= 1
                card_turned = False
            elif event.key == pygame.K_TAB:
                rand_on = not rand_on
                random.shuffle(random_list)
                Rterm_dict = dict(random_list)
                

    instructions = "Space bar will change between the term and definition. Left/Right will flip between flash cards. Tab will randomize the flash cards."
    instructions_object = text_font.render(instructions, True, "White", None, 700)
    instructions_rect = instructions_object.get_rect(center = (400, 30))
    current_question = list(term_dict)[index]
    current_answer = list(term_dict.values())[index]
    current_question_object = text_font.render(current_question, True, "Black")
    current_question_rect = current_question_object.get_rect(center = (400, 200))
    current_answer_object = text_font.render(current_answer, True, "Black", None, 500)
    current_answer_rect = current_answer_object.get_rect(center = (400, 200))
    current_index_object = text_font.render(f"{index + 1}/{len(term_dict)}", True, "Black")
    current_index_rect = current_index_object.get_rect(center = (400, 400))
    Rcurrent_question = list(Rterm_dict)[index]
    Rcurrent_answer = list(Rterm_dict.values())[index]
    Rcurrent_question_object = text_font.render(Rcurrent_question, True, "Black")
    Rcurrent_question_rect = Rcurrent_question_object.get_rect(center = (400, 200))
    Rcurrent_answer_object = text_font.render(Rcurrent_answer, True, "Black", None, 500)
    Rcurrent_answer_rect = Rcurrent_answer_object.get_rect(center = (400, 200))
   


    if not rand_on:
        if not card_turned:
            screen.fill((0, 0, 0))
            screen.blit(instructions_object, instructions_rect)
            pygame.draw.rect(screen, (0, 220, 220), (150, 150, 500, 300))
            screen.blit(current_question_object, current_question_rect)
        else:
            screen.fill((0, 0, 0))
            screen.blit(instructions_object, instructions_rect)
            pygame.draw.rect(screen, (220, 255, 220), (150, 150, 500, 300))
            screen.blit(current_answer_object, current_answer_rect)
    else:
        if not card_turned:
            screen.fill((0, 0, 0))
            screen.blit(instructions_object, instructions_rect)
            pygame.draw.rect(screen, (0, 220, 220), (150, 150, 500, 300))
            screen.blit(Rcurrent_question_object, Rcurrent_question_rect)
        else:
            screen.fill((0, 0, 0))
            screen.blit(instructions_object, instructions_rect)
            pygame.draw.rect(screen, (220, 255, 220), (150, 150, 500, 300))
            screen.blit(Rcurrent_answer_object, Rcurrent_answer_rect)        
  
    screen.blit(current_index_object, current_index_rect)

    pygame.display.update()

    clock.tick(60)

    

