import pygame

pygame.init() #initialization

#Screen setting
screen_width = 480 #width size
screen_height = 640 #height size
screen = pygame.display.set_mode((screen_width, screen_height))

#Screen title
pygame.display.set_caption("Mintae Game") #game name

#Even loop
running = True #Check that game is playing

while running:
    for event in pygame.event.get(): #which event is happend?
        if event.type == pygame.QUIT: #Quit event is happend?
            running = False

#Game close
pygame.quit()