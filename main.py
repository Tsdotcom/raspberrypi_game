from PIL import Image, ImageDraw, ImageFont, ImageSequence
import starting_activity
from os import listdir 
from os.path import isfile, join
import numpy
from image import ImageGUI
import sys
from controller import Controller
def main():
    st = starting_activity.Start()
    # ds = display.Display()
    ds = ImageGUI(3)
    ct = Controller()
    if st.root.start_game == False:
        st.start_game()
        num = st.gen_random_pic()
        # while True:
        #     ct.onClick()
        ds.rename_img("/home/tsdotcom/esw/mygame/tiles/1_0_120.jpg","/home/tsdotcom/esw/mygame/tiles/1_120_120.jpg")
    if st.root.end_game == True:
        pass

if __name__ == '__main__':


    main()
