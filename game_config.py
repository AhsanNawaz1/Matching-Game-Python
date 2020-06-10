import os

#These variables will look after image representation on screen
IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

#this is save the directory where images are store
ASSET_DIR = 'assets'
#this loop will load which picture in assets
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

assert len(ASSET_FILES) == 8
