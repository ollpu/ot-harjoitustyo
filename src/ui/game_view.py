from tkinter import StringVar, Text
from tkinter import Label as ImgLabel
from tkinter.ttk import Frame, Label
from PIL import ImageTk

class GameView(Frame):
    def __init__(self, root, game_service):
        super().__init__(master=root)
        # self._root = root
        self._game_service = game_service
        self._current_word_var = StringVar(self)
        self._current_word_label = Label(master=self, textvariable=self._current_word_var)
        self._current_word_label.pack()
        #self._images_container = Text(self, wrap="char", borderwidth=0,
        #                              highlightthickness=0, state="disabled")
        self._images_container = Frame(master=self)
        self._images_container.pack(expand=True)
        self._images = []

    def start(self, game):
        self._game_service.start_game(game)
        self._start_round()

    def _start_round(self):
        for label, index, _ in self._images:
            label.destroy()
        self._images = []
        for image, index in self._game_service.get_images():
            img = ImageTk.PhotoImage(image.image)
            label = ImgLabel(master=self._images_container, image=img)
            label.bind("<Button-1>", lambda e,index=index,ctx=self: ctx._guess(index))
            label.pack()
            self._images.append((label, index, img))

        self._update()

    def _update(self):
        self._current_word_var.set(self._game_service.get_text())

    def _guess(self, index):
        self._game_service.submit_guess(index)
        # TODO: clean up images, advance round, etc
        self._update()
