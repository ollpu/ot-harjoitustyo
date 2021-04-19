from tkinter import Frame, Label, CENTER

DELAY = 1000

class FlashMessage(Frame):
    def __init__(self, master, text, fg_color, bg_color):
        super().__init__(master=master, bg=bg_color)
        label = Label(self, text=text, fg=fg_color, bg=bg_color)
        label.config(font=("TkDefaultFont", 24))
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self._after_callback = None

    def show_timer(self, after_callback, delay=DELAY):
        self._after_callback = after_callback
        self.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8, anchor=CENTER)
        self.after(delay, self._after)

    def _after(self):
        if self._after_callback:
            self._after_callback()
        self.destroy()
