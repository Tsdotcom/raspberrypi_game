class Shooter:
    def __init__(self):
        self.shape = "circle"
        self.color = "blue"
        self.position = (0,0)
        self.button_pressed = False
    def pressed(self):
        self.button_pressed = True
    def start_lightning(self):
        pass