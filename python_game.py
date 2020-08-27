import pygame

pygame.init() #initialization

#Screen setting
screen_width = 480 #width size
screen_height = 640 #height size
screen = pygame.display.set_mode((screen_width, screen_height))

#Screen title
pygame.display.set_caption("Mintae Game") #game name 

#Background load
background = pygame.image.load("/Users/mintae/Desktop/Python_game/pygame_basic/background.png")

#Sprite load
character = pygame.image.load("/Users/mintae/Desktop/Python_game/pygame_basic/character.png")
character_size = character.get_rect().size #image size set
character_with = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - (character_with/2) #half of Screen width
character_y_pos = screen_height - character_height #bottom of screen height


#Even loop
running = True #Check that game is playing

while running:
    for event in pygame.event.get(): #which event is happend?
        if event.type == pygame.QUIT: #Quit event is happend?
            running = False

    screen.blit(background, (0, 0)) #background locate
    screen.blit(character, (character_x_pos, character_y_pos)) #character locate

    pygame.display.update() #Recall background


#Game close
pygame.quit()