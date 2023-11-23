import tkinter as tk
class Settings:
    def __init__(self):
        #game status
        self.level = 0
        self.song_length_bymin = 2
        self.game_score = 0
        self.background_color = "gray"
        self.display_height = 240
        self.display_width = 240
        #bar settings
        self.bar_width = 60
        self.bar_height = 240
        self.bar_speed = 5
    def get_speed(self):
        return self.game_speed
    def get_level(self):
        return self.level
    def get_game_score(self):
        return self.game_score
    def levelup(self):
        self.level += 1
    def add_game_score(self):
        self.game_score += 1


