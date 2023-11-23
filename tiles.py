from game_settings import Settings
class Tiles:
    def __init__(self):
        self.height = Settings().bar_height
        self.width = Settings().bar_width
        self.speed = Settings().bar_speed
        self.color = "black"
        self.position = (0,0)
    def add_speed(self):
        self.speed += 5
        Settings().bar_speed = self.speed 
