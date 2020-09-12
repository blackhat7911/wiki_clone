from frontend.main_screen import *
from frontend.home_page import *

class Posts(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Add Information"
        self.set_title(self.app_title)

        navbar = Frame(root, bg=self.gray)

        title = Label(navbar, text=self.app_title, font=(self.title_font, self.header_size, self.normal))
        title.pack(side=LEFT, padx=5, pady=5)

        navbar.pack(side=TOP, fill=BOTH)

        body_container = Frame(root, bg=self.white)

        info_label = Label(body_container, text="Add Information Here", bg=self.white, font=(self.header_font, self.header_size, self.normal))
        info_label.place(x=10, y=10)

        sep_line = ttk.Separator(body_container, orient=HORIZONTAL)
        sep_line.place(x=10, y=50, width=750, height=5)

        user_lbl = Label(body_container, text="Username", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        user_lbl.place(x=10, y=80)
        user_ent = Entry(body_container, textvariable=self.username, font=(self.plain_font, self.plain_size, self.normal))
        user_ent.place(x=200, y=80, width=300, height=30)

        title_lbl = Label(body_container, text="Title", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        title_lbl.place(x=10, y=110)
        title_ent = Entry(body_container, textvariable=self.title, font=(self.plain_font, self.plain_size, self.normal))
        title_ent.place(x=200, y=110, width=300, height=30)

        image_lbl = Label(body_container, text="Image", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        image_lbl.place(x=10, y=140)
        image_btn = Button(body_container, text="Add", command=self.image_browser, font=(self.plain_font, self.plain_size, self.normal))
        image_btn.place(x=200, y=140, width=100, height=30)
        img_name = Label(body_container, textvariable=self.image_name, bg=self.white, font=(self.plain_font, self.small_size, self.normal))
        img_name.place(x=310, y=140, width=450, height=30)

        imageval_lbl = Label(body_container, text="Image Value", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        imageval_lbl.place(x=10, y=170)
        imageval_ent = Entry(body_container, textvariable=self.image_value, bg=self.white, state=DISABLED, font=(self.plain_font, self.plain_size, self.normal))
        imageval_ent.place(x=200, y=170, width=300, height=30)

        desc_lbl = Label(body_container, text="Description", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        desc_lbl.place(x=10, y=200)
        self.desc_ent = Text(body_container, font=(self.plain_font, self.plain_size, self.normal))
        self.desc_ent.place(x=200, y=200, width=300, height=250)

        sep_line = ttk.Separator(body_container, orient=HORIZONTAL)
        sep_line.place(x=10, y=460, width=750, height=5)

        save_btn = Button(body_container, text="Save", command=self.save_activity, bg=self.green, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        save_btn.place(x=200, y=480, width=100, height=30)
        clr_btn = Button(body_container, text="Clear", command=self.clear_activity, bg=self.navy, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        clr_btn.place(x=310, y=480, width=100, height=30)
        cancel_btn = Button(body_container, text="Cancel", command=lambda: self.switch_frame(HomePage), bg=self.red, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        cancel_btn.place(x=420, y=480, width=100, height=30)

        body_container.place(x=15, y=70, width=770, height=515)

    def save_activity(self):
        title = self.title.get().lower()
        image_value = self.image_value.get()
        info = self.desc_ent.get("1.0", "end-1c")
        username = self.username.get()

        select_query = "select * from posts"

        self.backend.cur.execute(select_query)
        posts = self.backend.cur.fetchall()
        posts_record = []

        for post in posts:
            posts_record.append(post[0])

        if title == "" or image_value == "" or info == "" or username == "":
            messagebox.showerror("Input Error", "All fields are required")

        elif title in posts_record:
            messagebox.showerror("Error", "Post already exists")

        else:
            insert_query = "insert into posts (title,information,image,username) values (%s,%s,%s,%s)"
            values = (title, info, image_value, username)
            self.backend.cur.execute(insert_query, values)
            self.backend.conn.commit()
            self.binaryToImage(title)
            messagebox.showinfo("Success", "Posted successfully")

    def clear_activity(self):
        self.title.set("")
        self.image_value.set("")
        self.username.set("")
        self.image_name.set("")
        self.desc_ent.delete("1.0", END)
