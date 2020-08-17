from frontend.home_page import *
from backend.ImageConverter import *

class Hawa(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.file = ""
        self.binaryData = ""
        self.binData = StringVar()

        self.i = ImageConverter(self.file)

        lbl = Label(root, textvariable=self.binData, font=("arial", 12, "bold"))
        lbl.pack(side=TOP)

        btn = Button(root, text="click", command=self.img_dialog)
        btn.pack(side=BOTTOM)

    def imageToBinary(self):
        with open(self.file, 'rb') as fh:
            self.binaryData = fh.read()
            self.binData.set(self.file)
        return self.binaryData


    def binaryToImage(self):
        fh = open('img.png', 'wb')
        fh.write(self.binaryData)
        fh.close()

    def img_dialog(self):
        self.file = filedialog.askopenfilename(initialdir="root/home/", title="Select File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
        self.imageToBinary()


if __name__ == '__main__':
    mas = Tk()
    app = Hawa(mas)
    mainloop()

