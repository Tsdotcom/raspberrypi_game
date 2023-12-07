from PIL import Image, ImageDraw, ImageFont, ImageSequence
import starting_activity
from os import listdir 
from os.path import isfile, join
import numpy
from image import ImageGUI
import sys
from controller import Controller
import display
def main():
    gui = ImageGUI()
    bt_control = Controller()
    disp = display.Display()
    if bt_control.startgame == False:
        gui.show(gui.selected_pic)
        gui.delete_images()
        gui.crop()
        gui.multiple_images()
        gui.show(gui.new_img)
        selected_image = 0
        while not bt_control.endgame:
            command = {'right' : False, 'left' : False, 'down' : False, 'up' : False, 'end' : False, 'select': False, 'put' : False}
            while not disp.button_U.value:
                command['up'] = True
            while not disp.button_D.value:
                command['down'] = True
            while not disp.button_L.value:
                command['left'] = True
            while not disp.button_R.value:
                command['right'] = True
            while not disp.button_A.value:
                command['select'] = True
            while not disp.button_B.value:
                command['put'] = True
            while not disp.button_C.value:
                command['end'] = True
            if command['right'] == True:
                bt_control.x += 1
                gui.border_image(bt_control.x + bt_control.y)
                gui.rename_img(f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg",f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                gui.rename_img(f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                gui.delete_border()  
            if command['left'] == True:
                bt_control.x -= 1
                gui.border_image(bt_control.x + bt_control.y)
                gui.rename_img(f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg",f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                gui.rename_img(f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                gui.delete_border() 
            if command['up'] == True:
                bt_control.y -= 4
                gui.border_image(bt_control.x + bt_control.y)
                gui.rename_img(f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg",f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                gui.rename_img(f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                gui.delete_border() 
            if command['down'] == True:
                bt_control.y += 4
                gui.border_image(bt_control.x + bt_control.y)
                gui.rename_img(f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg",f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                gui.rename_img(f"{gui.bordered_image}{bt_control.x + bt_control.y}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                gui.delete_border() 
            if command['end'] == True:
                break
            if command['select'] == True:
                gui.highlight_image(bt_control.x + bt_control.y)
                gui.rename_img(f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg",f"{gui.highlighted_image}/{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                gui.rename_img(f"{gui.highlighted_image}/{bt_control.x + bt_control.y}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                selected_image = bt_control.x + bt_control.y
                gui.delete_border()
            if command['put'] == True:
                gui.rename_img(f"{gui.dir_out}/{selected_image}.jpg",f"{gui.dir_out}/{bt_control.x + bt_control.y}.jpg")
                gui.multiple_images()
                gui.show(gui.new_img)
                
if __name__ == '__main__':
    main()            


