from PIL import Image, ImageDraw, ImageFont
from display import Display 
import os
from itertools import product
class Image:
    def __init__(self,random_num):
        self.img_displayer = Display()
        self.open_img = Image.open(self.img_path).resize((self.img_displayer.width,self.img_displayer.height))
        self.opened_img = ""
        self.name = random_num+".jpg"
        self.dir_in = "/home/tsdotcom/esw/mygame/game_images/gameimages"
        self.dir_out = "/home/tsdotcom/esw/mygame/game_images/gameimages/tiles"
        self.tile_size = 60
    def crop(self,filename, dir_in, dir_out, d):
        name, ext = os.path.splitext(filename)
        img = Image.open(os.path.join(dir_in, filename)).resize((240,240))
        w, h = img.size
        grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
        for i, j in grid:
            box = (j, i, j+d, i+d)
            out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
            img.crop(box).save(out)
    def show(self):
        self.img_displayer.disp.image(self.open_img)
    def rotate90(self):
        return self.open_img.rotate(90)
