from tkinter import Tk, Button, X, BOTH, CENTER

from services.game_service import default_game_service as game_service
from services.play_service import PlayService
from ui.game_view import GameView
from ui.game_list import GameList
from ui.game_edit_view import GameEditView

class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Lukemisen harjoittelu")
        self.geometry("900x700")
        self._view = None
        game_service.load_test_game_if_empty()
        self._games = game_service.get_all_games()
        self.show_start_view()

    def destroy_current_view(self):
        if self._view:
            self._view.destroy()
        self._view = None

    def show_start_view(self):
        self.destroy_current_view()

        self._view = GameList(self)
        self._view.pack(fill=BOTH)

    def show_game_view(self, game):
        self.destroy_current_view()

        self._view = GameView(self, PlayService())
        self._view.pack(fill=X)
        self._view.start(game)

    def show_edit_view(self, game):
        self.destroy_current_view()

        self._view = GameEditView(self, game)
        self._view.pack(fill=BOTH, expand=1)
