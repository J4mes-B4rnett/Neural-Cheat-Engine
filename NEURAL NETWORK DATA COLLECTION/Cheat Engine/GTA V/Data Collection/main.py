
# James Barnett - Toilet Br3ak Training API - 06/07/21 #
#                                                      #
# This python script will capture your screen and key  #
# presses and pair them. This is used as data to train #
# the cheat engine neural network.                     #
#                                                      #
#               © MIT License 2021                     #


# { Controls }                                         #
# Timing -                                             #
#                                                      #
# Less time interval means more accuracy, however      #
# there is also more storage and RAM consumption.      #
# Ideal for mid/high-range computers.                  #
# 
# More time interval means less accuracy, however
# there is less storage and RAM consumption, making it #
# ideal for mid/low-range computers,                   #
#                                                      #
#                                                      #

# Imports necessary libraries

from PIL import Image # Image manipulation
import keyboard as kb # Keyboard input
import time as tm # Time controller
import mss # Screenshot handler

import skimage # Image manipulation
import skimage.io # Image file stream
import skimage.feature # Image manipulation

import json # Keyboard input file manager

_dir = "img\\"  # Directory of where to store images
json_location = 'keymap.json' # Name/location of the keymap database

index = 0  # File name

active = True

keymap = {} # Temporary dictionary to store key inputs

while True: # Forever
    tm.sleep(1.5) # Timing control
    if active: # When active
        with mss.mss() as screen:  # Open MSS instance

            directory = "{0}{1}.bmp".format(_dir, index) # Processed directory
            screen.shot(output=directory) # Take screenshot and temporarily store it in directory

            screenshot = skimage.io.imread(fname=directory, as_gray=True) # Re-open the image as grayscale
            screenshot = skimage.feature.canny( # Apply edge detection features to it
                image=screenshot,        # Image object
                sigma=2.0,               # Type of activation to use
                low_threshold=0.1,       # Low threshold for black
                high_threshold=0.2,      # # High threshold for white
            )   
            
            skimage.io.imsave(directory, screenshot) # Save processed image permanently

            print("New Capture: {0}\{1}.bmp".format(_dir, index)) # Output location and name of new file
            
            keys = []

            try:
                if kb.is_pressed('w'):
                    keys.append('w')

                if kb.is_pressed('a'):
                    keys.append('a')

                if kb.is_pressed('s'):
                    keys.append('s')

                if kb.is_pressed('d'):
                    keys.append('d')

            except:
                continue

            keymap[index] = keys

            with open('keymap.json', 'w') as fp:
                json.dump(keymap, fp)

            index += 1  # Incremental step (file name)