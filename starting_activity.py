from PIL import Image, ImageDraw, ImageFont
from game_settings import Settings
import display
import random
class Start:
    def __init__(self):
        self.gui = display.Display()
        self.root = Settings()
    def end_game(self):
        self.root.end_game = True
    def start_game (self):
        self.root.start_game = True
    def gen_random_pic(self):
        return random.randint(1,5)


    

