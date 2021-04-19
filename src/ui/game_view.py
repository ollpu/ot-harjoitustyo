from tkinter import StringVar, Text, RIGHT
from tkinter import Label as ImgLabel
from tkinter.ttk import Frame, Label
from PIL import ImageTk

from game_service import GuessResult

IMAGES_PER_ROW = 5

class GameView(Frame):
    def __init__(self, root, game_service):
        super().__init__(master=root)
        # self._root = root
        self._game_service = game_service
        self._current_word_var = StringVar(self)
        self._current_word_label = Label(master=self, textvariable=self._current_word_var)
        self._current_word_label.config(font=("TkDefaultFont", 22))
        self._current_word_label.pack(pady=6)
        #self._images_container = Text(self, wrap="char", borderwidth=0,
        #                              highlightthickness=0, state="disabled")
        self._images_container = Frame(master=self)
        self._images_container.pack(expand=True)
        self._images = []

    def start(self, game):
        self._game_service.start_game(game)
        self._start_round()

    def _start_round(self):
        self._images_container.destroy()
        self._images_container = Frame(master=self)
        self._images_container.pack(expand=True)
        self._images = []
        row = Frame(master=self._images_container)
        row.pack(pady=3)
        row_count = 0
        for image, index in self._game_service.get_images():
            if row_count >= IMAGES_PER_ROW:
                row = Frame(master=self._images_container)
                row.pack(pady=3)
                row_count = 0
            row_count += 1
            img = ImageTk.PhotoImage(image.image)
            label = ImgLabel(master=row, image=img)
            label.bind("<Button-1>", lambda e,index=index,ctx=self: ctx._guess(index))
            label.pack(side=RIGHT, padx=3)
            self._images.append((label, index, img))

        self._update()

    def _update(self):
        self._current_word_var.set(self._game_service.get_text())

    def _guess(self, index):
        result = self._game_service.submit_guess(index)
        if result == GuessResult.INCORRECT:
            pass
        elif result == GuessResult.CORRECT_ONE:
            self._update()
        elif result == GuessResult.CORRECT_ROUND_COMPLETE:
            if self._game_service.next_round():
                self._start_round()
            else:
                # TODO: lopeta peli
                pass
