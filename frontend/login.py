from frontend.main_screen import *
from frontend.home_page import *
from frontend.register import *

class Login(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Login"
        self.set_title(self.win_title)

        form_title = Label(root, text=self.win_title, font=(self.title_font, self.header_size, self.normal), bg=self.white)
        form_title.place(x=280, y=160)

        login_form = Frame(root, bg=self.gray)

        name_lbl = Label(login_form, text="Email", font=(self.title_font, self.plain_size, self.normal))
        name_lbl.place(x=20, y=20)
        name_ent = Entry(login_form, textvariable=self.username, font=(self.plain_font, self.plain_size, self.normal), bg=self.white)
        name_ent.place(x=20, y=45, width=210, height=30)

        pass_lbl = Label(login_form, text="Password", font=(self.title_font, self.plain_size, self.normal))
        pass_lbl.place(x=20, y=90)
        pass_ent = Entry(login_form, textvariable=self.password, show="*", font=(self.plain_font, self.plain_size, self.normal),
                         bg=self.white)
        pass_ent.place(x=20, y=115, width=210, height=30)

        login_btn = Button(login_form, text="Login", font=(self.plain_font, self.plain_size, self.normal), command=self.login_activity, bg=self.green, fg=self.white)
        login_btn.place(x=20, y=160, width=210, height=30)

        acc_lbl = Label(login_form, text="Don't have an account.", font=(self.plain_font, self.small_size, self.underline))
        acc_lbl.place(x=70, y=190)

        register_btn = Button(login_form, text="Register", font=(self.plain_font, self.plain_size, self.normal), bg=self.navy, command=lambda: self.switch_frame(Register), fg=self.white)
        register_btn.place(x=20, y=210, width=210, height=30)

        login_form.place(x=280, y=210, width=250, height=250)

    def login_activity(self):
        user = self.username.get()
        passwd = self.password.get()

        if user == "user" and passwd == "123":
            self.switch_frame(HomePage)
        else:
            self.invalid_msg()

if __name__ == '__main__':
    master = Tk()
    app = Login(master)
    mainloop()