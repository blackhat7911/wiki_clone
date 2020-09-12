from frontend.login import *
from frontend.main_screen import *
from frontend.login import *

class Register(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Register"
        self.set_title(self.win_title)

        form_title = Label(root, text=self.win_title, font=(self.title_font, self.header_size, self.normal), bg=self.white)
        form_title.place(x=280, y=50)

        register_form = Frame(root, bg=self.gray)

        self.img = PhotoImage(file="//home//bishal//Desktop//sem2-assignments//algoanddb//wiki_clone//static//user_icon.png")
        self.user_img = Label(register_form, image=self.img)
        self.user_img.place(x=100, y=10, width=55, height=55)
        img_lbl = Label(register_form, textvariable=self.image_name, font=(self.plain_font, self.small_size, self.underline))
        img_lbl.place(x=15, y=60)

        name_label = Label(register_form, text="Username", font=(self.plain_font, self.plain_size, self.normal))
        name_label.place(x=20, y=80)
        name_ent = Entry(register_form, textvariable=self.username, font=(self.plain_font, self.plain_size, self.normal))
        name_ent.place(x=20, y=105, width=210, height=30)

        email_label = Label(register_form, text="Email", font=(self.plain_font, self.plain_size, self.normal))
        email_label.place(x=20, y=140)
        email_ent = Entry(register_form, textvariable=self.email, font=(self.plain_font, self.plain_size, self.normal))
        email_ent.place(x=20, y=165, width=210, height=30)

        image_label = Label(register_form, text="Image", font=(self.plain_font, self.plain_size, self.normal))
        image_label.place(x=20, y=200)
        add_btn = Button(register_form, text="Add", command=self.image_browser, font=(self.plain_font, self.plain_size, self.normal))
        add_btn.place(x=20, y=225, width=100, height=30)

        image_label = Label(register_form, text="Image Value", font=(self.plain_font, self.plain_size, self.normal))
        image_label.place(x=20, y=265)
        image_val = Entry(register_form, textvariable=self.image_value, state=DISABLED, font=(self.plain_font, self.plain_size, self.normal))
        image_val.place(x=20, y=290, width=210, height=30)

        pass_label = Label(register_form, text="Password", font=(self.plain_font, self.plain_size, self.normal))
        pass_label.place(x=20, y=320)
        pass_ent = Entry(register_form, textvariable=self.password, show="*", font=(self.plain_font, self.plain_size, self.normal))
        pass_ent.place(x=20, y=345, width=210, height=30)

        register_btn = Button(register_form, text="Register", font=(self.plain_font, self.plain_size, self.normal), bg=self.green, command=self.register_activity, fg=self.white)
        register_btn.place(x=20, y=380, width=210, height=30)

        or_lbl = Label(register_form, text="or", font=(self.plain_font, self.small_size, self.underline))
        or_lbl.place(x=120, y=410)

        back_btn = Button(register_form, text="Go Back", font=(self.plain_font, self.plain_size, self.normal), bg=self.navy, command=lambda: self.switch_frame(Login), fg=self.white)
        back_btn.place(x=20, y=430, width=210, height=30)

        register_form.place(x=280, y=90, width=250, height=480)

    def register_activity(self):
        username = self.username.get()
        email = self.email.get()
        password = self.password.get()
        image_value = self.image_value.get()

        select_query = "select * from users"

        self.backend.cur.execute(select_query)
        users = self.backend.cur.fetchall()
        users_record = []

        for user in users:
            users_record.append(user[0])

        if username == "" or email == "" or image_value == "" or password == "":
            messagebox.showerror("Input Error", "All fields are required")

        elif username in users_record:
            messagebox.showerror("Registration Error", "Username already exists try another username")

        else:
            insert_query = "insert into users (username,email,image,password) values (%s,%s,%s,%s)"
            values = (username, email, image_value, password)
            self.backend.cur.execute(insert_query, values)
            self.backend.conn.commit()
            messagebox.showinfo("Registration Success", "User registered successfully")

