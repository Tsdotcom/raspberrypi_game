import tkinter as tk
class Settings:
    def __init__(self):
        #game status
        self.level = 0
        self.song_length_bymin = 2
        self.background_color = "gray"
        self.display_height = 240
        self.display_width = 240
        #bar settings
        self.start_game = False
        self.continue_game = False
        self.end_game = False
    def get_level(self):
        return self.level
    def levelup(self):
        self.level += 1
    def start(self):
        self.start_game = True
    def go_on(self):
        self.continue_game = True
    def end(self):
        self.end_game = True



