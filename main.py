from PIL import Image, ImageDraw, ImageFont
import display
import starting_activity
import os
disp = display.Display()
starting_gui = starting_activity.Start()
# img_path = os.path("game_images/gameimages/1.jpeg")
def main():
    # my_image = Image.new("RGB",(disp.width,disp.height))
    # my_draw = ImageDraw.Draw(my_image)
    # my_draw.rectangle((0,0,disp.width,disp.height),fill=(255,0,0,100))
    # disp.disp.image(my_image)
    if starting_gui.root.start_game == False:
        starting_gui.start_game()
    # image = Image.new("RGB", (disp.width, disp.height))
    # draw = ImageDraw.Draw(image)
    # draw.rectangle((0,0,disp.width, disp.height), fill=(255,0,0,100))
    with Image.open("./game_images/gameimages/1.jpeg") as im:
        im.rotate(45).show()
        
    if starting_gui.root.end_game == True:
        pass

if __name__ == '__main__':
    main()
