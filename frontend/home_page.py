from frontend.login import *
from frontend.main_screen import *
from frontend.posts import *
from frontend.login import *
from frontend.edit_page import *
from frontend.delete_page import *

class HomePage(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Home Page"
        self.set_title(self.win_title)

        # navigation bar
        navbar = Frame(root, bg=self.gray)

        title = Label(navbar, text=self.app_title, font=(self.title_font, self.header_size, self.normal))
        title.pack(side=LEFT, padx=5, pady=5)

        logout = Button(navbar, text="Logout", command=lambda: self.switch_frame(Login), fg=self.white, bg=self.red,
                        font=(self.plain_font, self.plain_size, self.normal))
        logout.pack(side=RIGHT, pady=5)

        # search bar
        search_bar = Frame(navbar)

        entry_box = Entry(search_bar, textvariable=self.search_text, font=(self.plain_font, self.plain_size, self.normal), width=16)
        entry_box.pack(side=LEFT)
        search_btn = Button(search_bar, text="Search", command=self.search_activity, font=(self.plain_font, self.plain_size, self.normal), bg=self.navy, width=10, fg=self.white)
        search_btn.pack(side=RIGHT)

        search_bar.pack(side=RIGHT, padx=5, pady=8)

        navbar.pack(side=TOP, fill=BOTH)

        # body container
        body_container = Frame(root, bg=self.gray)

        # title container
        self.title_container = Label(body_container, textvariable=self.title, font=(self.header_font, self.header_size, self.normal))
        self.title_container.place(x=10, y=10)

        # text container
        info_container = Frame(body_container, bg=self.white)
        info_container.place(x=10, y=50, width=530, height=455)
        scrolly = Scrollbar(info_container, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.text_area = Text(info_container, font=(self.plain_font, self.plain_size, self.normal), yscrollcommand=scrolly)
        self.text_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.text_area.yview)

        body_container.place(x=15, y=70, width=550, height=515)

        # image container
        self.image_container = Frame(root, bg=self.gray)

        self.img = PhotoImage(file="//home//bishal//Desktop//sem2-assignments//algoanddb//wiki_clone//static//app_icon.png")
        self.ig_lbl = Label(self.image_container, image=self.img)
        self.ig_lbl.pack()

        self.image_container.place(x=585, y=70, width=195, height=160)

        # buttons container
        button_container = Frame(root, bg=self.gray)

        label = Label(button_container, text="Settings", font=(self.plain_font, self.plain_size, self.normal))
        label.place(x=10, y=15)
        add_btn = Button(button_container, text="+Add", command=lambda: self.switch_frame(Posts), bg=self.green, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        add_btn.place(x=10, y=40, width=175, height=30)
        edit_btn = Button(button_container, text="Edit", command=lambda: self.switch_frame(EditPage), bg=self.navy, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        edit_btn.place(x=10, y=80, width=175, height=30)
        del_btn = Button(button_container, text="Delete", command=lambda: self.switch_frame(Delete), bg=self.red, fg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        del_btn.place(x=10, y=120, width=175, height=30)

        button_container.place(x=585, y=245, width=195, height=160)

        # user details container
        detail_container = Frame(root, bg=self.gray)

        label = Label(detail_container, text="Posted By : ", font=(self.plain_font, self.plain_size, self.normal))
        label.place(x=10, y=70)
        username = Label(detail_container, textvariable=self.writer, font=(self.plain_font, self.plain_size, self.normal))
        username.place(x=10, y=90)

        detail_container.place(x=585, y=425, width=195, height=160)

        self.default_info()

# show default info
    def default_info(self):
        file = open("/home/bishal/Desktop/sem2-assignments/algoanddb/wiki_clone/static/app_desc.txt", "r")
        for dataline in file.readlines():
            info = dataline.split("-")
            self.title.set(info[0])
            self.writer.set(info[2])
            self.text_area.insert('1.0', info[1])
            self.image_name.set("")

# search activity
    def search_activity(self):
        search_text = self.search_text.get()

        select_query = "select * from posts"

        self.backend.cur.execute(select_query)
        posts = self.backend.cur.fetchall()
        posts_record = []

        for post in posts:
            posts_record.append(post[1])

        index = posts_record.index(search_text)

        if search_text == "":
            messagebox.showerror("Input Error", "You haven't input any text")

        elif search_text not in posts_record:
            messagebox.showerror("Search Error", "Search result not found")

        else:
            self.title.set(posts[index][1].title())
            self.writer.set(posts[index][4])
            self.text_area.delete("1.0", END)
            self.text_area.insert("1.0", posts[index][2])

            self.img = PhotoImage(file="//home//bishal//Desktop//sem2-assignments//algoanddb//wiki_clone//db_images//{0}.png".format(posts[index][1]))
            self.ig_lbl = Label(self.image_container, image=self.img)
            self.ig_lbl.pack()
            self.ig_lbl.image = self.img
