from PIL import Image, ImageDraw, ImageFont, ImageSequence
import starting_activity
from os import listdir 
from os.path import isfile, join
import numpy
from image import ImageGUI
import sys
from controller import Controller
def main():
    gui = ImageGUI()
    bt_control = Controller()
    if bt_control.startgame == False:
        gui.show(gui.selected_pic)
        gui.delete_images()
        gui.crop()
        gui.multiple_images()
        gui.show(gui.new_img)
        bt_control.onClick(bt_control.endgame)



            

if __name__ == '__main__':
    main()
