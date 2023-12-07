from display import Display
import random
from image import ImageGUI
class Controller:
    def __init__(self):
        self.control = Display()
        self.img_gui = ImageGUI()
        self.x = 0
        self.y = 0
        self.count = 0
        self.rotate = False
        self.choose = False
        self.endgame = False
        self.startgame = False
        self.random_num = 0
    def clear_pos(self):
        if self.x == 240:
            self.x = 0
        if self.y >= 240:
            self.y = 0