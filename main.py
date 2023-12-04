from PIL import Image, ImageDraw, ImageFont
import display
import starting_activity
import os
from itertools import product

def main():
    st = starting_activity.Start()
    ds = display.Display()
    if st.root.start_game == False:
        st.start_game()
        num = st.gen_random_pic()
        img1 = Image.open('game_images/gameimages/3.jpg').resize((120,120))
        display.Display().disp.image(img1)
        # img2= Image.open('game_images/gameimages/2.jpg').resize((120,120))
        # display.Display().disp.image(img2)
    if st.root.end_game == True:
        pass

if __name__ == '__main__':

    main()
