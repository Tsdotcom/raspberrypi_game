from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import ttk
import time
from game_settings import Settings
import display
class Start:
    def __init__(self):
        self.root = Settings()
    def end_game(self):
        self.root.end_game = True
    def start_game (self):
        self.root.start_game = True
    def start_gui(self):
        self.start_root = Start()
        self.gui = tk.Tk()
        self.start_button_text = tk.StringVar()
        self.start_button_text.set("START GAME")
        self.end_button_text = tk.StringVar()
        self.end_button_text.set("QUIT GAME")
        self.background_style = ttk.Style()
        self.background_style.configure('.',background='gray')
        self.main_frame = ttk.Frame(self.gui,style="main_frame.TFrame",height= self.start_root.root.display_height, width=
                            self.start_root.root.display_width)
        self.start_button = ttk.Button(self.main_frame, text='START', style='start_button.Tbutton', textvariable=self.start_button_text, width = 15, command=self.start_root.start_game)
        self.end_button = ttk.Button(self.main_frame,text='QUIT', style='quit_button.Tbutton', textvariable=self.end_button_text, width = 15, command=self.start_root.end_game() )
        self.start_button.grid(row = 2, columnspan=3, pady=5)
        self.end_button.grid(row = 4, columnspan= 3, pady= 5)
        self.gui.mainloop()
    
    

    

