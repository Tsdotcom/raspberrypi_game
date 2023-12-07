from display import Display
import random
from image import ImageGUI
class Controller:
    def __init__(self):
        self.control = Display()
        self.img_gui = ImageGUI()
        self.up = self.control.button_U
        self.down = self.control.button_D
        self.right = self.control.button_R
        self.left = self.control.button_L
        self.choosebut = self.control.button_A
        self.rotatebut = self.control.button_B
        self.endbut = self.control.button_C
        self.x = 0
        self.y = 0
        self.rotate = False
        self.choose = False
        self.endgame = False
        self.startgame = False
        self.random_num = 0
    def onClick(self, condition):
        while not condition:
            if not self.up.value:
                self.y -= 4
                self.img_gui.border_image(self.x + self.y)
                self.img_gui.multiple_images()
                self.img_gui.show(self.img_gui.new_img)
            if not self.down.value:
                self.y += 4
                self.img_gui.border_image(self.x + self.y)
                self.img_gui.multiple_images()
                self.img_gui.show(self.img_gui.new_img)
            if not self.choosebut.value:
                self.choose = True
            if not self.rotatebut.value:
                self.rotate = True
            if not self.right.value:
                self.x += 1
                self.img_gui.border_image(self.x + self.y)
                self.img_gui.multiple_images()
                self.img_gui.show(self.img_gui.new_img)
            if not self.left.value:
                self.x -= 1
                self.img_gui.border_image(self.x + self.y)
                self.img_gui.multiple_images()
                self.img_gui.show(self.img_gui.new_img)
            if not self.endbut.value:
                self.endgame = True
           
    def clear_pos(self):
        if self.x == 240:
            self.x = 0
        if self.y >= 240:
            self.y = 0

if __name__ == '__main__':
    start = Controller()
    start.onClick(False)