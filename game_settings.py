import tkinter as tk
class Settings:
    def __init__(self):
        #game status
        self.display_height = 240
        self.display_width = 240
        #bar settings
        self.start_game = False
        self.continue_game = False
        self.end_game = False
    def start(self):
        self.start_game = True
    def go_on(self):
        self.continue_game = True
    def end(self):
        self.end_game = True



