import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from backend.ImageConverter import *
from backend.main import *
from model.user_model import *
from PIL import Image, ImageTk
from tkinter import ttk

class Main:
    def __init__(self, root):
        self.root = root

        self.win_title = ""
        self.app_title = "Wikipedia"

        # colors codes
        self.white = "#ffffff"
        self.black = "#000000"
        self.gray = "#dcdcdc"
        self.aqua = "#00ffff"
        self.navy = "#000080"
        self.red = "#ff0000"
        self.green = "#00ff00"

        # variables
        self.writer = StringVar()
        self.title = StringVar()
        self.search_text = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.image_value = StringVar()
        self.image_name = StringVar()
        self.filename = ""
        self.binaryData = ""
        self.desc = StringVar()

        # fonts
        self.title_font = "new times roman"
        self.header_font = "arial"
        self.plain_font = "candara"

        # font sizes
        self.title_size = 34
        self.header_size = 25
        self.plain_size = 12
        self.small_size = 8

        # font weight
        self.normal = "normal"
        self.bold = "bold"
        self.italic = "italic"
        self.underline = "underline"

        # geometry
        self.width = 800
        self.height = 600

        self.set_title(self.win_title)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.configure(background=self.white)
        self.root.resizable(width=False, height=False)

        self.backend = Backend()
        self.user_model = User(self.username, self.email, self.image_value, self.password)

    def switch_frame(self, frame):
        self.root.withdraw()
        win = Toplevel()
        frame(win)

    def set_title(self, win_title):
        self.root.title(win_title)

    def imageToBinary(self):
        with open(self.filename, 'rb') as fh:
            self.binaryData = fh.read()
            self.image_value.set(self.binaryData)
        return self.binaryData

    def binaryToImage(self, uname):
        fh = open("//home//bishal//Desktop//sem2-assignments//algoanddb//wiki_clone//db_images//{}.png".format(uname), 'wb')
        fh.write(self.binaryData)
        fh.close()

    def image_browser(self):
        self.filename = filedialog.askopenfilename(initialdir="root/home/", title="Select File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
        self.imageToBinary()
        self.image_name.set(self.filename)