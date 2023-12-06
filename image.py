from PIL import Image, ImageOps, ImageEnhance
from display import Display 
import os
from itertools import product
from os import listdir 
from os.path import isfile, join
from natsort import natsorted 
from controller import Controller
import random
class ImageGUI:
    def __init__(self):
        self.img_displayer = Display()
        self.control = Controller()
        self.dir_in = "/home/tsdotcom/esw/mygame/game_images"
        self.dir_out = "/home/tsdotcom/esw/mygame/tiles"
        self.tile_size = 60
        self.selected_pic =  f"{self.dir_in}/{self.control.get_random_num()}.jpg"
        self.pic_shuffled_list = []
        self.new_img = 'shuffled.jpg'
    def crop(self):
        img = Image.open(self.selected_pic).resize((240,240))
        w, h = img.size
        grid = product(range(0, h-h%self.tile_size, self.tile_size), range(0, w-w%self.tile_size, self.tile_size))
        self.pic_shuffled_list = list(range(16))
        random.shuffle(self.pic_shuffled_list)
        idx = 0
        for i, j in grid:
            box = (j, i, j+self.tile_size, i+self.tile_size)
            out = os.path.join(self.dir_out, f'{self.pic_shuffled_list[idx]}.jpg')
            img.crop(box).save(out)
            idx += 1
    def show(self,path):
        img = Image.open(path).resize((240,240))
        self.img_displayer.disp.image(img)
    def rotate90(self):
        return self.open_img.rotate(90)
    def multiple_images(self):
        listofimages = []
        files = [ f for f in listdir(self.dir_out) if isfile(join(self.dir_out,f)) ]
        onlyfiles = natsorted(files)
        for i in range(0,len(onlyfiles)):
            listofimages.append(f"{self.dir_out}/{onlyfiles[i]}")
        images = [Image.open(x).resize((60,60)) for x in listofimages]
        new_img = Image.new('RGB', (240, 240))
        num = 0
        for i in range(0,240,60):
            for k in range(0,240,60):
                new_img.paste(images[num],(k,i))         
                num += 1
         
        new_img.save('shuffled.jpg')  
    def delete_images(self):
        for file in os.listdir(self.dir_out):
            if file.endswith('.jpg'):
                try:
                    os.remove(file)
                except:
                    FileExistsError
    def border_image(self, path):
        img = Image.open(path).resize((59,59))
        img_with_border = ImageOps.expand(img, border=1, fill='white')
        img_with_border.save(path)
    def highlight_image(self,path):
        img = Image.open(path).resize((60,60))
        enhaced = ImageEnhance.Brightness(img)
        img = enhaced.enhance(0.5)
        img.save(f'{path}test.png')
    def rename_img(self,source,dest):
        temp = "/home/tsdotcom/esw/mygame/tiles/x.jpg" # middle 
        os.rename(dest,temp)
        os.rename(source,dest)
        os.rename(temp,source)
