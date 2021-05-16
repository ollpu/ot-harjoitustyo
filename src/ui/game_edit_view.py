from tkinter import Button, Frame, Label, Entry, W, X, TOP, LEFT, BOTTOM, BOTH, StringVar

from services.game_service import default_game_service as game_service
from ui.round_edit_view import RoundEditView
from ui.scroll_box import ScrollBox

class GameEditView(Frame):
    def __init__(self, ui_root, game):
        super().__init__(master=ui_root)
        self._ui_root = ui_root
        self._game = game

        self._name_var = StringVar()
        self._name_var.set(self._game.name)
        name_entry = Entry(master=self, textvariable=self._name_var)
        name_entry.config(font=("TkDefaultFont", 20))
        name_entry.pack(fill=X, pady=8, padx=8)

        scrollbox = ScrollBox(self)
        self._rounds_list = scrollbox.contents
        self._rounds_list.grid_columnconfigure(0, weight=1)
        scrollbox.pack(fill=BOTH, expand=True)

        self._load_rounds()

        actions = Frame(master=self)

        new_button = Button(master=actions, text="Uusi kierros", command=self._new_round)
        new_button.config(font=("TkDefaultFont", 20))
        new_button.pack(side=TOP, padx=8, pady=8)

        delete_button = Button(master=actions, text="Poista peli", command=self._delete)
        delete_button.config(font=("TkDefaultFont", 20))
        delete_button.pack(side=LEFT, padx=8, pady=8)

        cancel_button = Button(master=actions, text="Peru", command=self._cancel)
        cancel_button.config(font=("TkDefaultFont", 20))
        cancel_button.pack(side=LEFT, padx=8, pady=8)

        save_button = Button(master=actions, text="Tallenna", command=self._save)
        save_button.config(font=("TkDefaultFont", 20))
        save_button.pack(side=LEFT, padx=8, pady=8)

        actions.pack(side=BOTTOM)

    def _delete(self):
        game_service.remove_game(self._game)
        self._ui_root.show_start_view()

    def _cancel(self):
        self._ui_root.show_start_view()

    def _save(self):
        self._game.name = self._name_var.get()
        game_service.save_game(self._game)
        self._ui_root.show_start_view()

    def _load_rounds(self):
        for child in self._rounds_list.winfo_children():
            child.destroy()
        for row, g_round in enumerate(self._game.rounds):
            pairs_count = len(g_round.pairs)
            pairs_human = "1 pari" if pairs_count == 1 else f"{pairs_count} paria"
            name_label = Label(master=self._rounds_list, text=f"Kierros {row+1}: {pairs_human}")
            name_label.grid(row=row, column=0, sticky=W, padx=(16, 8), pady=8)
            name_label.config(font=("TkDefaultFont", 20))

            play_button = Button(master=self._rounds_list, text="Muokkaa",
                                 command=lambda idx=row: self._edit_round(idx))
            play_button.config(font=("TkDefaultFont", 20))
            play_button.grid(row=row, column=1, padx=8, pady=8)

            edit_button = Button(master=self._rounds_list, text="Poista",
                                 command=lambda idx=row: self._remove_round(idx))
            edit_button.config(font=("TkDefaultFont", 20))
            edit_button.grid(row=row, column=2, padx=(8, 16), pady=8)

    def _new_round(self):
        game_service.add_round(self._game, [])
        self._edit_round(len(self._game.rounds)-1)

    def _edit_round(self, idx):
        editor = RoundEditView(self, self._game.rounds[idx])
        editor.place(x=0, y=0, relwidth=1, relheight=1)

    def finish_round_edit(self):
        self._load_rounds()

    def _remove_round(self, idx):
        self._game.rounds.pop(idx)
        self._load_rounds()
