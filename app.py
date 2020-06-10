#library
import pygame
import game_config as gc

#import things we gonna use in this code
from pygame import display, event , image
from animal import Animal
from time import sleep

def find_index(x,y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index
#function we are going to use in this which will help use us import things
pygame.init() 

#This function will help us display the game name
display.set_caption('My game') 

#this function will help us create the screen
screen = display.set_mode((512,512)) 

#this variable will store the image to display whcih we gonna need when 2 images get matches
matched= image.load('other_assets/matched.png')

#this is boolean variable which will tell if game is running or not
running = True

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

#Loop which will start the game
while running:
    #variable with function which we imported via event which will let us use mouse and keyboard movements
    #will remove the movement from the queue 
    current_events = event.get()
    #loop that will keep game running until queue and game ends
    for e in current_events:
        #default function which will end the game and set running
        #variable to false to stop the game
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]

        screen.fill((255, 255, 255))
        #this function is telling that image will not be displayed until it is not flipped
        for _,tile in enumerate(tiles):
            image_i = tile.image if tile.index in current_images else tile.box 
            if not tile.skip:
                screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))

        if len(current_images) == 2:
            idx1, idx2 = current_images
            if tiles[idx1].name == tiles[idx2].name:
                tiles[idx1].skip = True
                tiles[idx2].skip = True
                sleep(0.8)
                screen.blit(matched, (0,0))
                display.flip()
                sleep(0.8)
                current_images = []

        display.flip()

print(' Goodbye! ')


