from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
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
        self.image_name = StringVar()
        self.filename = "add image"

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

        # error messages
        self.empty = "All fields are required"
        self.login_err = "Your login credintials donot match"

        # images
        self.user_profile = "/home//bishal/Desktop/sem2-assignments/algoanddb/wiki_clone/static/user_img.png"
        self.search_icon = "/home/bishal/Desktop/sem2-assignments/algoanddb/wiki_clone/static/search_icon.png"

        # geometry
        self.width = 800
        self.height = 600

        self.set_title(self.win_title)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.configure(background=self.white)
        self.root.resizable(width=False, height=False)

        #self.image_values = ImageConverter()

    def switch_frame(self, frame):
        win = Tk()
        frame(win)
        self.root.withdraw()

    def set_title(self, win_title):
        self.root.title(win_title)

    def img_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir="root/home/", title="Select File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
        self.image_name.set(self.filename)

    def empty_msg(self):
        messagebox.showerror("Error", "All fields are required")

    def invalid_msg(self):
        messagebox.showerror("Error", "Sorry, that didn't work")