import tkinter as tk
import time
from game_settings import Settings
class Game:
    def __init__(self):
        self.root = Settings()
        self.game_score = 0
        self.time = self.root.song_length_bymin
        self.game_startornot = True
        self.game_pause = False
    def end_game(self):
        self.game_startornot = False
    def start_game (self):
        self.game_startornot = True
    def pause_game(self):
        self.game_pause = True
    def continue_game(self):
        self.game_pause = False
    
