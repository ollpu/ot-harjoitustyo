from tkinter import Tk, Button, X, CENTER
from default_game import load_test_game

from repositories.game_repository import default_game_repository as game_repository
from services.game_service import GameService
from ui.game_view import GameView

class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Lukemisen harjoittelu")
        self.geometry("900x700")
        self._view = None
        if len(game_repository.all()) == 0:
            game_repository.store(load_test_game())
        self._games = game_repository.all()
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
        self._view.start(self._games[0])
