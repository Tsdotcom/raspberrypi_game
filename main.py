from PIL import Image, ImageDraw, ImageFont
import display
import starting_activity
disp = display.Display()
main_game = starting_activity.Game()
def main():
    # my_image = Image.new("RGB",(disp.width,disp.height))
    # my_draw = ImageDraw.Draw(my_image)
    # my_draw.rectangle((0,0,disp.width,disp.height),fill=(255,0,0,100))
    # disp.disp.image(my_image)
    if main_game.root.start_game == False:
        pass
    if main_game.root.end_game == True:
        pass

if __name__ == '__main__':
    main()
