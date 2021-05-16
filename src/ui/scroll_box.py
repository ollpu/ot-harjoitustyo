from tkinter import Frame, Canvas, Scrollbar, NW, LEFT, RIGHT, BOTH, Y

class ScrollBox(Frame):
    def __init__(self, master):
        super().__init__(master)
        canvas = Canvas(self, height=10)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.contents = Frame(self)

        self.contents.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        key = canvas.create_window((0, 0), window=self.contents, anchor=NW)
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(key, width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
