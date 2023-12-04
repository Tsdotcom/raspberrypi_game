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
        # st.start_gui(num)
    if st.root.end_game == True:
        pass

if __name__ == '__main__':

    main()
