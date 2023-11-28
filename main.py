from PIL import Image, ImageDraw, ImageFont
import display
disp = display.Display()
def main():
    my_image = Image.new("RGB",(disp.width,disp.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0,0,disp.width,disp.height),fill=(255,0,0,100))
    disp.disp.image(my_image)
def stop_game():
    disp.disp.

if __name__ == '__main__':
    main()
