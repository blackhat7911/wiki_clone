from frontend.home_page import *
from backend.ImageConverter import *
from backend.main import *
from io import BytesIO
from PIL import Image, ImageTk

class Hawa(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.uname = StringVar()

        self.file = ""
        self.binaryData = ""
        self.binData = StringVar()

        self.i = ImageConverter(self.file)
        self.b = Backend()

        img_btn = Button(root, text="image", command=self.img_dialog)
        img_btn.pack()

        img_ent = Entry(root, textvariable=self.binData)
        img_ent.pack()

        user_ent = Entry(root, textvariable=self.uname)
        user_ent.pack()

        add_btn = Button(root, text="add", command=self.add_db)
        add_btn.pack()

        show_btn = Button(root, text="show", command=self.show)
        show_btn.pack()

    def imageToBinary(self):
        with open(self.file, 'rb') as fh:
            self.binaryData = fh.read()
            self.binData.set(self.binaryData)
        return self.binaryData

    def binaryToImage(self):
        fh = open('img.png', 'wb')
        fh.write(self.binaryData)
        fh.close()

    def img_dialog(self):
        self.file = filedialog.askopenfilename(initialdir="root/home/", title="Select File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
        self.imageToBinary()

    def add_db(self):
        username = self.uname.get()
        image = self.binData.get()

        if username == "" or image == "":
            messagebox.showerror("Err", "all req")
        else:
            query = 'insert into test values (%s,%s)'
            value = (username, image)
            self.b.add(query, value)
            self.b.conn.commit()
            messagebox.showinfo("Suss", "Added")

    def show(self):
        fetch_qry = "select * from test"
        self.b.cur.execute(fetch_qry)
        record = self.b.cur.fetchone()

        img = Image.open(BytesIO(record))
        dsfa = ImageTk.PhotoImage(img)

        panel = Label(self, image=dsfa)
        panel.pack()

if __name__ == '__main__':
    mas = Tk()
    app = Hawa(mas)
    mainloop()

