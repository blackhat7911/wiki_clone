from frontend.main_screen import *
from frontend.login import *

class Register(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Register"
        self.set_title(self.win_title)

        form_title = Label(root, text=self.win_title, font=(self.title_font, self.header_size, self.normal), bg=self.white)
        form_title.place(x=280, y=120)

        register_form = Frame(root, bg=self.gray)

        user_img = Button(register_form, text="add image", command=self.img_dialog)
        user_img.place(x=100, y=20, width=50, height=50)
        img_lbl = Label(register_form, textvariable=self.img_name, font=(self.plain_font, self.small_size, self.underline))
        img_lbl.place(x=95, y=60)

        name_label = Label(register_form, text="Username", font=(self.plain_font, self.plain_size, self.normal))
        name_label.place(x=20, y=80)
        name_ent = Entry(register_form, textvariable=self.username, font=(self.plain_font, self.plain_size, self.normal))
        name_ent.place(x=20, y=105, width=210, height=30)

        email_label = Label(register_form, text="Email", font=(self.plain_font, self.plain_size, self.normal))
        email_label.place(x=20, y=140)
        email_ent = Entry(register_form, textvariable=self.email, font=(self.plain_font, self.plain_size, self.normal))
        email_ent.place(x=20, y=165, width=210, height=30)

        pass_label = Label(register_form, text="Password", font=(self.plain_font, self.plain_size, self.normal))
        pass_label.place(x=20, y=200)
        pass_ent = Entry(register_form, textvariable=self.password, show="*",
                         font=(self.plain_font, self.plain_size, self.normal))
        pass_ent.place(x=20, y=225, width=210, height=30)

        register_btn = Button(register_form, text="Register", font=(self.plain_font, self.plain_size, self.normal),
                              bg=self.green, command=self.register_activity, fg=self.white)
        register_btn.place(x=20, y=265, width=210, height=30)

        or_lbl = Label(register_form, text="or", font=(self.plain_font, self.small_size, self.underline))
        or_lbl.place(x=120, y=295)

        back_btn = Button(register_form, text="Go Back", font=(self.plain_font, self.plain_size, self.normal), bg=self.navy, command=self.goback, fg=self.white)
        back_btn.place(x=20, y=310, width=210, height=30)

        register_form.place(x=280, y=170, width=250, height=350)

    def register_activity(self):
        username = self.username.get()
        email = self.email.get()
        password = self.password.get()

        select_query = "select * from users"

        self.backend.cur.execute(select_query)
        users = self.backend.cur.fetchall()
        users_record = []

        for user in users:
            users_record.append(user[0])

        if username == "" or email == "" or password == "":
            messagebox.showerror("Input Error", "All fields are required")

        elif username in users_record:
            messagebox.showerror("Registration Error", "Username already exists try another username")

        else:
            insert_query = "insert into users (username,email,image,password) values (%s,%s,%s,%s)"
            values = (username, email, password)
            self.backend.cur.execute(insert_query, values)
            self.backend.conn.commit()
            messagebox.showinfo("Registration Success", "User registered successfully")

    def goback(self):
        self.switch_frame(Login)