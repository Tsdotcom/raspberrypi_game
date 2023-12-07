import time
from image import ImageGUI
from controller import Controller
import display
from PIL import Image, ImageDraw, ImageFont
gui = ImageGUI()
bt_control = Controller()
disp = display.Display()
def main():
    if bt_control.startgame == False:
        show_by_time()
        gui.delete_images()
        gui.crop()
        gui.multiple_images()
        gui.show(gui.new_img)
        selected_image = 0
        while not bt_control.endgame:
            command = {'right' : False, 'left' : False, 'down' : False, 'up' : False, 'end' : False, 'select': False, 'put' : False }
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
                img = Image.new("RGB",(240,240))
                tt = ImageDraw.Draw(img)
                myFont = ImageFont.truetype('FreeMono.ttf', 50)
                tt.text((70,70),"END",font=myFont ,fill=(255,0,0))
                img.save('/home/tsdotcom/esw/mygame/end.jpg')
                gui.show('/home/tsdotcom/esw/mygame/end.jpg')
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
def show_by_time():
    start = time.time()
    period_of_time = 5
    while True:
        gui.show(gui.selected_pic)
        if time.time() > start + period_of_time:
            return 
if __name__ == '__main__':
    main()            


