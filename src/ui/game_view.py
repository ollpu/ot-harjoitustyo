from tkinter import StringVar, RIGHT
from tkinter import Label as ImgLabel
from tkinter.ttk import Frame, Label
from PIL import ImageTk

from services.play_service import GuessResult
from ui.flash_message import FlashMessage

IMAGES_PER_ROW = 5

class GameView(Frame):
    def __init__(self, ui_root, play_service):
        super().__init__(master=ui_root)
        self._ui_root = ui_root
        self._play_service = play_service
        self._current_word_var = StringVar(self)
        self._current_word_label = Label(master=self, textvariable=self._current_word_var)
        self._current_word_label.config(font=("TkDefaultFont", 24))
        self._current_word_label.pack(pady=6)
        #self._images_container = Text(self, wrap="char", borderwidth=0,
        #                              highlightthickness=0, state="disabled")
        self._images_container = Frame(master=self)
        self._images_container.pack(expand=True)
        self._images = []

    def start(self, game):
        self._play_service.start_game(game)
        self._start_round()

    def _start_round(self):
        self._images_container.destroy()
        self._images_container = Frame(master=self)
        self._images_container.pack(expand=True)
        self._images = []
        row = Frame(master=self._images_container)
        row.pack(pady=3)
        row_count = 0
        for image, index in self._play_service.get_images():
            if row_count >= IMAGES_PER_ROW:
                row = Frame(master=self._images_container)
                row.pack(pady=3)
                row_count = 0
            row_count += 1
            img = ImageTk.PhotoImage(image.loaded_image)
            label = ImgLabel(master=row, image=img)
            label.bind("<Button-1>", lambda e,index=index,ctx=self: ctx.guess(index))
            label.pack(side=RIGHT, padx=3)
            self._images.append((label, index, img))

        self._update()

    def _update(self):
        self._current_word_var.set(self._play_service.get_text())

    def _end_game(self):
        self._play_service.reset()
        self._ui_root.show_start_view()

    def guess(self, index):
        result = self._play_service.submit_guess(index)
        if result == GuessResult.INCORRECT:
            msg = FlashMessage(self, "Väärin", "#a00612", "#c8abb6")
            msg.show_timer(None)
        elif result == GuessResult.CORRECT_ONE:
            msg = FlashMessage(self, "Oikein!", "#06a012", "#ABC8B6")
            msg.show_timer(self._update)
        elif result == GuessResult.CORRECT_ROUND_COMPLETE:
            if self._play_service.next_round():
                msg = FlashMessage(self, "Oikein!\nSeuraava kierros", "#068010", "#ABC8B6")
                msg.show_timer(self._start_round, 2000)
            else:
                msg = FlashMessage(self, "Oikein!\nPeli loppu", "#068010", "#ABC8B6")
                msg.show_timer(self._end_game, 4000)
