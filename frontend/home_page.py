from frontend.main_screen import *

class HomePage(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Wikipedia"
        self.set_title(self.win_title)

        top_navbar = Frame(root, bg=self.gray)

        title = Label(top_navbar, text=self.win_title, font=(self.title_font, self.header_size, self.normal))
        title.pack(side=LEFT, padx=5, pady=5)

        nav_container = Frame(top_navbar)

        search_bar = Frame(nav_container)

        entry_box = Entry(search_bar, textvariable=self.search_text, font=(self.plain_font, self.plain_size, self.normal))
        entry_box.pack(side=LEFT)
       # icon = PhotoImage(file=r'{}'.format(self.search_icon))
        search_btn = Button(search_bar, text="Search", image='', command="", font=(self.plain_font, self.plain_size, self.normal))
        search_btn.pack(side=RIGHT)

        search_bar.pack(side=LEFT, padx=5, pady=5)

        profile = Frame(nav_container)

        user = Canvas(profile, width=20, height=20)
        # img = ImageTk.PhotoImage(Image.open(self.user_img))
        # user.create_image(0, 0, image=img)
        user.pack()

        profile.pack(side=RIGHT)

        nav_container.pack(side=RIGHT, padx=5, pady=5)

        top_navbar.pack(side=TOP, fill=BOTH)
