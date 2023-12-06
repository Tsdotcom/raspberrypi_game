from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
from display import Display 
import os
from itertools import product
from os import listdir 
from os.path import isfile, join
from natsort import natsorted 
class ImageGUI:
    def __init__(self,random_num):
        self.img_displayer = Display()
        self.dir_in = "/home/tsdotcom/esw/mygame/game_images"
        self.dir_out = "/home/tsdotcom/esw/mygame/tiles"
        self.tile_size = 60
    def crop(self,filename, dir_in, dir_out, d):
        name, ext = os.path.splitext(filename)
        img = Image.open(os.path.join(dir_in, filename)).resize((240,240))
        w, h = img.size
        grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
        count = 0
        for i, j in grid:
            box = (j, i, j+d, i+d)
            out = os.path.join(dir_out, f'{count}{ext}')
            count += 1
            img.crop(box).save(out)
    def show(self,img):
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
        new_im = Image.new('RGB', (240, 240))
        num = 0
        for i in range(0,240,60):
            for k in range(0,240,60):
                new_im.paste(images[num],(k,i))         
                num += 1   
        new_im.save('test.jpg')
    def delete_images(self):
        for file in os.listdir(self.dir_out):
            if file.endswith('.jpg'):
                os.remove(file)
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