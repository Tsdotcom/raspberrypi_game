from display import Display
class Controller:
    def __init__(self):
        self.control = Display()
        self.up = self.control.button_U
        self.down = self.control.button_D
        self.right = self.control.button_R
        self.left = self.control.button_L
        self.choosebut = self.control.button_A
        self.rotatebut = self.control.button_B
        self.x = 0
        self.y = 0
        self.rotate = False
        self.choose = False
    def onClick(self, condition):
        while condition:
            if not self.up.value:
                self.y -= 60
            if not self.down.value:
                self.y += 60
            if not self.choosebut.value:
                self.choose = True
            if not self.rotatebut.value:
                self.rotate = True
            if not self.right.value:
                self.x += 60
            if not self.left.value:
                self.x -= 60
    def clear_pos(self):
        if self.x >= 240:
            self.x = 0
        if self.y >= 240:
            self.y = 0
    
