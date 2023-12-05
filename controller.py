from display import Display
class Controller:
    def __init__(self):
        self.control = Display()
        self.up = self.control.button_U
        self.down = self.control.button_D
        self.right = self.control.button_R
        self.left = self.control.button_L
        self.place = self.control.button_A
        self.rotate = self.control.button_B
    def onClick(self):
        if not self.up.value:
            print("UP")
        if not self.down.value:
            print("DOWN")
        if not self.place.value:
            print("place")
        if not self.rotate.value:
            print("rotate")
        if not self.right.value:
            print("right")
        if not self.left.value:
            print("left")
        