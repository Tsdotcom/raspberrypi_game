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
        self.img_height = Display().height
        self.img_width = Display().width
        # self.draw = ImageDraw()
        self.name = '1.jpg'
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
        # img = Image.open(path).resize((self.img_height,self.img_width))
        self.img_displayer.disp.image(img)
    def rotate90(self):
        return self.open_img.rotate(90)
    def multiple_images(self):
        listofimages = []
        
        # onlyfiles = [ f for f in listdir(self.dir_out) if isfile(join(self.dir_out,f)) ]
        # onlyfiles.sort(reverse=False)
        print(sorted(listdir(self.dir_out)))
        # for i in range(0,len(onlyfiles)):
        #     listofimages.append(f"{self.dir_out}/{onlyfiles[i]}")
        # images = [Image.open(x).resize((60,60)) for x in listofimages]
        # new_im = Image.new('RGB', (240, 240))
        # x_offset = 0
        # y_offset = 0
        # print(listofimages)
        # for im in images:
        #     if x_offset == 240:
        #         x_offset = 0
        #         y_offset += im.size[0]
        #         new_im.paste(im, (x_offset,y_offset))
        #     else:    
        #         new_im.paste(im, (x_offset,y_offset))
        #         x_offset += im.size[0]
        # new_im.save('test.jpg')
    def save_image_pos(self):
        pass
    def delete_images(self):
        for file in os.listdir(self.dir_out):
            if file.endswith('.jpg'):
                os.remove(file)
    def border_image(self, path):
        img = Image.open(path).resize((80,80))
        img_with_border = ImageOps.expand(img, border=1, fill='white')
        img_with_border.save(f'{path}test.png')
    def highlight_image(self,path):
        img = Image.open(path).resize((80,80))
        enhaced = ImageEnhance.Brightness(img)
        img = enhaced.enhance(0.5)
        img.save(f'{path}test.png')
    def rename_img(self,source,dest):
        temp = "/home/tsdotcom/esw/mygame/tiles/1_x_y.jpg" # middle 
        os.rename(dest,temp)
        os.rename(source,dest)
        os.rename(temp,source)