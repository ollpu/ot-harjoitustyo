from tkinter import Button, W
from tkinter.ttk import Frame, Label

from services.game_service import default_game_service as game_service

class GameList(Frame):
    def __init__(self, ui_root):
        super().__init__(master=ui_root)
        self._ui_root = ui_root

        games = game_service.get_all_games()
        self.grid_columnconfigure(0, weight=1)
        for row, game in enumerate(games):
            name_label = Label(master=self, text=game.name)
            name_label.grid(row=row, column=0, sticky=W, padx=(16, 8), pady=8)
            name_label.config(font=("TkDefaultFont", 20))
            play_button = Button(master=self, text="Pelaa", command=lambda: self._play_game(game))
            play_button.config(font=("TkDefaultFont", 20))
            play_button.grid(row=row, column=1, padx=8, pady=8)
            edit_button = Button(master=self, text="Muokkaa", command=lambda: self._edit_game(game))
            edit_button.config(font=("TkDefaultFont", 20))
            edit_button.grid(row=row, column=2, padx=(8, 16), pady=8)

        new_button = Button(master=self, text="Luo uusi peli", command=self._new_game)
        new_button.config(font=("TkDefaultFont", 20))
        new_button.grid(columnspan=3, sticky=W, padx=16, pady=16)

    def _play_game(self, game):
        self._ui_root.show_game_view(game)

    def _edit_game(self, game):
        self._ui_root.show_edit_view(game)

    def _new_game(self):
        game = game_service.new_game("Uusi peli")
        self._edit_game(game)
