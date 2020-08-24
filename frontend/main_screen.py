from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from backend.ImageConverter import *
from backend.main import *

class Main:
    def __init__(self, root):
        self.root = root

        self.win_title = ""

        # colors codes
        self.white = "#ffffff"
        self.black = "#000000"
        self.gray = "#dcdcdc"
        self.aqua = "#00ffff"
        self.navy = "#000080"
        self.green = "#00ff00"

        # variables
        self.search_text = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.img_value = StringVar()
        self.img_name = "add image"

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

        #self.image_values = ImageConverter(self.filename)
        self.backend = Backend()

    def switch_frame(self, frame):
        win = Tk()
        frame(win)
        self.root.withdraw()

    def set_title(self, win_title):
        self.root.title(win_title)

    def img_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir="root/home/", title="Select File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
        self.image_name.set(self.filename)
