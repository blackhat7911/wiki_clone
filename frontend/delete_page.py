from frontend.main_screen import *
from frontend.home_page import *

class Delete(Main):
    def __init__(self, root):
        Main.__init__(self, root)

        self.win_title = "Delete Page"
        self.set_title(self.win_title)

        self.status = StringVar()

        title = Label(root, text=self.win_title, bg=self.white, font=(self.header_font, self.header_size, self.normal))
        title.place(x=300, y=200)

        del_lbl = Label(root, text="Post Title", bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        del_lbl.place(x=300, y=250)

        title_ent = Entry(root, textvariable=self.title, font=(self.plain_font, self.plain_size, self.normal))
        title_ent.place(x=300, y=270, width=210, height=30)

        del_btn = Button(root, text="Delete", command=self.delete_info, fg=self.white, bg=self.green, font=(self.plain_font, self.plain_size, self.normal))
        del_btn.place(x=300, y=310, width=210, height=30)

        cancel_btn = Button(root, text="Cancel", command=lambda: self.switch_frame(HomePage), fg=self.white, bg=self.red, font=(self.plain_font, self.plain_size, self.normal))
        cancel_btn.place(x=300, y=350, width=210, height=30)

        status = Label(root, textvariable=self.status, bg=self.white, font=(self.plain_font, self.plain_size, self.normal))
        status.place(x=300, y=400)

    def delete_info(self):
        query = "select * from posts"
        self.backend.cur.execute(query)
        records = self.backend.cur.fetchall()

        title = self.title.get().lower()
        value = (title,)

        post_records = []

        for row in records:
            post_records.append(row[1])

        if title == "":
            messagebox.showerror("Input Error", "Entry can't be empty")

        elif title not in post_records:
            messagebox.showerror("Error", "Data not found")

        else:
            del_query = "delete from posts where title=%s"
            self.backend.cur.execute(del_query, value)
            self.backend.conn.commit()
            self.status.set("Data deleted successfully")
