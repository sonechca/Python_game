import pygame

pygame.init() #initialization

#Screen setting
screen_width = 480 #width size
screen_height = 640 #height size
screen = pygame.display.set_mode((screen_width, screen_height))

#Screen title
pygame.display.set_caption("Mintae Game") #game name 

#background load
background = pygame.image.load("/Users/mintae/Desktop/Python_game/pygame_basic/background.png")

#Even loop
running = True #Check that game is playing

while running:
    for event in pygame.event.get(): #which event is happend?
        if event.type == pygame.QUIT: #Quit event is happend?
            running = False

    screen.blit(background, (0, 0)) #background locate

    pygame.display.update() #Recall background


#Game close
pygame.quit()