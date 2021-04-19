from tkinter import Tk, Button, X, CENTER
from default_game import load_test_game

from game_service import GameService
from ui.game_view import GameView

class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Lukemisen harjoittelu")
        self.geometry("900x700")
        self._view = None
        self._game = load_test_game()
        self.show_start_view()

    def destroy_current_view(self):
        if self._view:
            self._view.destroy()
        self._view = None

    def show_start_view(self):
        self.destroy_current_view()

        self._view = Button(self, text="Aloita peli", command=self.show_game_view)
        self._view.config(font=("TkDefaultFont", 24))
        self._view.place(relx=0.5, rely=0.5, anchor=CENTER)

    def show_game_view(self):
        self.destroy_current_view()

        self._view = GameView(self, GameService())
        self._view.pack(fill=X)
        self._view.start(self._game)
