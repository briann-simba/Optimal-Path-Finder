import pygame
from pygame.locals import *
import main as algorithms
pygame.font.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
shade = (40,40,40)
green = (0, 255, 0)
path = (230,230,250)
blue = (0, 0, 255)

font = pygame.font.SysFont(None, 16)
kisumu_label = font.render('KISUMU', True, white)
nakuru_label = font.render('NAKURU', True, white)
nairobi_label = font.render('NAIROBI', True, white)
thika_label = font.render('THIKA', True, white)
mombasa_label = font.render('MOMBASA', True, white)
isiolo_label = font.render('ISIOLO', True, white)
garissa_label = font.render('GARISSA', True, white)
kitui_label = font.render('KITUI', True, white)
eldoret_label = font.render('ELDORET', True, white)
malindi_label = font.render('MALINDI', True, white)


def setup(start, end):
    #get an array of all attempts done.
    bfs = algorithms.BreadthFirst(start, end)
    dfs = algorithms.DepthFirst(start, end)
    aStar = algorithms.aStar(start, end)

    return bfs, dfs, aStar

attempts = setup("Kisumu", "Malindi") #Change towns here to change path
bfs = attempts[0]
dfs = attempts[1]
aStar = attempts[2]
bfs_attempts = bfs[0]
dfs_attempts = dfs[0]
aStar_attempts = aStar[0]

bfs_optimal = bfs[1].split(" --> ")
dfs_optimal = dfs[1].split(" --> ")
aStar_optimal = aStar[1].split(" --> ")
print("DFS: ", aStar_optimal)
screen= pygame.display.set_mode((display_width,display_height))

def highlight(town, parent):
    if town == "Kisumu":
        pygame.draw.ellipse(screen, blue, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi

        if parent == "Nakuru":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, blue, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Eldoret":
            pygame.draw.line(screen, blue, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    elif town == "Nakuru":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, blue, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi

        if parent == "Kisumu":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, blue, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Nairobi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, blue, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    elif town == "Nairobi":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, blue, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi)

        if parent == "Nakuru":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, blue, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Thika":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, blue, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Mombasa":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, blue, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    elif town == "Thika":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, blue, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi

        if parent == "Nairobi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, blue, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Kitui":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, blue, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Isiolo":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, blue, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    elif town == "Mombasa":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, blue, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi

        if parent == "Nairobi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, blue, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Malindi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, blue, (770, 340), (720, 370))#mombasa malindi
    elif town == "Malindi":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, blue, (760, 330, 20, 20))#Malindi

        if parent == "Mombasa":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, blue, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Kitui":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, blue, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Garissa":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, blue, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
    if town == "Kitui":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, blue, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi
        if parent == "Thika":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, blue, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Malindi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, blue, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
    if town == "Garissa":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, blue, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi
        if parent == "Isiolo":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, blue, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Malindi":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, blue, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    if town == "Isiolo":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, blue, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi
        if parent == "Thika":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, blue, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Garissa":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, blue, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

    if town == "Eldoret":
        pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
        pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
        pygame.draw.ellipse(screen, blue, (70 , 170, 20, 20))#Eldoret
        pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
        pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
        pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
        pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
        pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
        pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
        pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi
        if parent == "Nakuru":
            pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, blue, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi
        elif parent == "Kisumu":
            pygame.draw.line(screen, blue, (30 , 310), (80 , 180))#kisumu eldoret
            pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
            pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
            pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
            pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
            pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
            pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
            pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
            pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
            pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
            pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
            pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi

def optimal(arr): #highlights the optimal path
    for i in range(len(arr)):
        if arr[i] == "Kisumu":
            pygame.draw.ellipse(screen, path, (15 , 295, 30, 30), width=2)#Kisumu
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Nakuru":
                pygame.draw.line(screen, blue, (30 , 310), (150, 270))#kisumu nakuru
            elif arr[i+1] == "Eldoret":
                pygame.draw.line(screen, blue, (30 , 310), (80 , 180))#kisumu eldoret
        elif arr[i] == "Nakuru":
            pygame.draw.ellipse(screen, path, (135, 255, 30, 30), width=2)#Nakuru
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Kisumu":
                pygame.draw.line(screen, blue, (30 , 310), (150, 270))
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, blue, (150, 270), (250, 350))
            elif arr[i+1] == "Eldoret":
                pygame.draw.line(screen, blue, (80 , 180), (150, 270))#eldoret nakuru
        elif arr[i] == "Nairobi":
            pygame.draw.ellipse(screen, path, (235, 335, 30, 30), width=2)#Nairobi
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Thika":
                pygame.draw.line(screen, blue, (250, 350), (310, 280))#nairobi thika
            elif arr[i+1] == "Nakuru":
                pygame.draw.line(screen, blue, (150, 270), (250, 350))#nakuru nairobi
            elif arr[i+1] == "Mombasa":
                pygame.draw.line(screen, blue, (250, 350), (720, 370))#nairobi mombasa
        elif arr[i] == "Thika":
            pygame.draw.ellipse(screen, path, (295, 265, 30, 30), width=2)#Thika
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, blue, (250, 350), (310, 280))#nairobi thika
            elif arr[i+1] == "Isiolo":
                pygame.draw.line(screen, blue, (310, 280), (340, 120))#thika isiolo
            elif arr[i+1] == "Kitui":
                pygame.draw.line(screen, blue, (310, 280), (500, 290))#thika kitui
        elif arr[i] == "Mombasa":
            pygame.draw.ellipse(screen, path, (705, 355, 30, 30), width=2)#Mombasa
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, blue, (250, 350), (720, 370))#nairobi mombasa
            elif arr[i+1] == "Malindi":
                pygame.draw.line(screen, blue, (770, 340), (720, 370))#mombasa malindi
        elif arr[i] == "Malindi":
            pygame.draw.ellipse(screen, path, (755, 325, 30, 30), width=2)#Malindi
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Garissa":
                pygame.draw.line(screen, blue, (580, 200), (770, 340))#garissa malindi
            elif arr[i+1] == "Kitui":
                pygame.draw.line(screen, blue, (500, 290), (770, 340))#kitui malindi
            elif arr[i+1] == "Mombasa":
                pygame.draw.line(screen, blue, (770, 340), (720, 370))#mombasa malindi
        elif arr[i] == "Garissa":
            pygame.draw.ellipse(screen, path, (565, 185, 30, 30), width=2)#Garissa
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Malindi":
                pygame.draw.line(screen, blue, (580, 200), (770, 340))#garissa malindi
            elif arr[i+1] == "Isiolo":
                pygame.draw.line(screen, blue, (340, 120), (580, 200))#isiolo garissa
        elif arr[i] == "Isiolo":
            pygame.draw.ellipse(screen, path, (325, 105, 30, 30), width=2)#Isiolo
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Thika":
                pygame.draw.line(screen, blue, (310, 280), (340, 120))#thika isiolo
            elif arr[i+1] == "Garissa":
                pygame.draw.line(screen, blue, (340, 120), (580, 200))#isiolo garissa
        elif arr[i] == "Eldoret":
            pygame.draw.ellipse(screen, path, (65 , 165, 30, 30), width=2)#Eldoret
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Nakuru":
                pygame.draw.line(screen, blue, (80 , 180), (150, 270))#eldoret nakuru
            elif arr[i+1] == "Kisumu":
                pygame.draw.line(screen, blue, (30 , 310), (80 , 180))#kisumu eldoret
        elif arr[i] == "Kitui":
            pygame.draw.ellipse(screen, path, (485, 275, 30, 30), width=2)#Kitui
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Thika":
                pygame.draw.line(screen, blue, (310, 280), (500, 290))#thika kitui
            elif arr[i+1] == "Malindi":
                pygame.draw.line(screen, blue, (500, 290), (770, 340))#kitui malindi

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(shade)
    #Draw all the 5 towns
    pygame.display.set_caption("Optimal Path Finder")
    pygame.draw.ellipse(screen, red, (20 , 300, 20, 20))#Kisumu
    pygame.draw.ellipse(screen, red, (140, 260, 20, 20))#Nakuru
    pygame.draw.ellipse(screen, red, (70 , 170, 20, 20))#Eldoret
    pygame.draw.ellipse(screen, red, (240, 340, 20, 20))#Nairobi
    pygame.draw.ellipse(screen, red, (300, 270, 20, 20))#Thika
    pygame.draw.ellipse(screen, red, (330, 110, 20, 20))#Isiolo
    pygame.draw.ellipse(screen, red, (490, 280, 20, 20))#Kitui
    pygame.draw.ellipse(screen, red, (570, 190, 20, 20))#Garissa
    pygame.draw.ellipse(screen, red, (710, 360, 20, 20))#Mombasa
    pygame.draw.ellipse(screen, red, (760, 330, 20, 20))#Malindi

    # Draw the roads between the towns
    pygame.draw.line(screen, red, (30 , 310), (80 , 180))#kisumu eldoret
    pygame.draw.line(screen, red, (30 , 310), (150, 270))#kisumu nakuru
    pygame.draw.line(screen, red, (80 , 180), (150, 270))#eldoret nakuru
    pygame.draw.line(screen, red, (150, 270), (250, 350))#nakuru nairobi
    pygame.draw.line(screen, red, (250, 350), (310, 280))#nairobi thika
    pygame.draw.line(screen, red, (250, 350), (720, 370))#nairobi mombasa
    pygame.draw.line(screen, red, (310, 280), (500, 290))#thika kitui
    pygame.draw.line(screen, red, (310, 280), (340, 120))#thika isiolo
    pygame.draw.line(screen, red, (500, 290), (770, 340))#kitui malindi
    pygame.draw.line(screen, red, (340, 120), (580, 200))#isiolo garissa
    pygame.draw.line(screen, red, (580, 200), (770, 340))#garissa malindi
    pygame.draw.line(screen, red, (770, 340), (720, 370))#mombasa malindi



    #Label the towns
    screen.blit(kisumu_label, (40, 320))
    screen.blit(nakuru_label, (160, 270))
    screen.blit(nairobi_label, (260, 360))
    screen.blit(thika_label, (320,290))
    screen.blit(eldoret_label, (100, 180))
    screen.blit(isiolo_label, (350, 100))
    screen.blit(kitui_label, (510, 300))
    screen.blit(garissa_label, (590, 190))
    screen.blit(malindi_label, (750, 350))
    screen.blit(mombasa_label, (690, 380))

    optimal_path = "Optimal Path = " + " --> ".join(aStar_optimal)
    for track in bfs_attempts: #Change this to see different paths (bfs_attempts, dfs_attempts, aStar_attempts)
        for town in track:
            if town[1] == True:
                highlight(town[0], town[2])
                pygame.time.wait(750)
        optimal(aStar_optimal)

        screen.blit(font.render(optimal_path, True, white), (display_width/2 - 250, display_height/2 + 200))
        pygame.display.update()


pygame.quit()
