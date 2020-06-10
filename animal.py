import os
import random
import game_config as gc

from pygame import image, transform

#this function will make count a images used in game 
animals_count = dict((a,0) for a in gc.ASSET_FILES)

#this function will count a images name and count in game
def available_animals():
    return [a for a, c in animals_count.items() if c<2]

class Animal:
    def __init__(self, index):
        #setting index
        self.index = index
        #setting numbr of rows and colums
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        #random to choose random function
        self.name= random.choice(available_animals())
        animals_count[self.name] +=1

        # giving path
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.image =image.load(self.image_path)
        # giving gray screen size according to image of animals
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN))
        #create a copy of image and then fill with gray 200 is for it 
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        #if 2 images are matched so it will not get repeated
        self.skip = False 
