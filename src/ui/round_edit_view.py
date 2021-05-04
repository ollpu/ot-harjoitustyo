from tkinter import Button, Frame, Label, Entry, W, X, LEFT, BOTTOM, StringVar
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, UnidentifiedImageError

from entities.image import Image
from ui.flash_message import FlashMessage

class RoundEditView(Frame):
    def __init__(self, game_edit_view, g_round):
        super().__init__(master=game_edit_view)
        self._game_edit_view = game_edit_view

        self._round = g_round

        self._pairs_list = Frame(master=self)
        self._pairs_list.grid_columnconfigure(0, weight=1)
        self._pairs_list.pack(fill=X)

        self._name_vars = []
        self._image_refs = []

        self._load_pairs()

        actions = Frame(master=self)

        new_button = Button(master=actions, text="Avaa kuva", command=self._new_pair)
        new_button.config(font=("TkDefaultFont", 20))
        new_button.pack(side=LEFT, padx=8, pady=8)

        finish_button = Button(master=actions, text="Valmis", command=self._finish)
        finish_button.config(font=("TkDefaultFont", 20))
        finish_button.pack(side=LEFT, padx=8, pady=8)

        actions.pack(side=BOTTOM)

    def _load_pairs(self):
        for child in self._pairs_list.winfo_children():
            child.destroy()
        self._name_vars.clear()
        self._image_refs.clear()
        for row, pair in enumerate(self._round.pairs):
            text_var = StringVar()
            text_var.set(pair[0])
            self._name_vars.append(text_var)
            text_entry = Entry(master=self._pairs_list, textvariable=text_var)
            text_entry.config(font=("TkDefaultFont", 20))
            text_entry.grid(row=row, column=0, sticky=W, padx=(16, 8), pady=8)

            # TODO: Use thumbnail
            img = ImageTk.PhotoImage(pair[1].loaded_image)
            label = Label(master=self._pairs_list, image=img)
            self._image_refs.append(img)
            label.grid(row=row, column=1, padx=8, pady=6)

            delete_button = Button(master=self._pairs_list, text="Poista",
                                   command=lambda idx=row: self._remove_pair(idx))
            delete_button.config(font=("TkDefaultFont", 20))
            delete_button.grid(row=row, column=2, padx=(8, 16), pady=8)

    def _update_names(self):
        for idx, var in enumerate(self._name_vars):
            pair = self._round.pairs[idx]
            pair = (var.get(), pair[1])
            self._round.pairs[idx] = pair

    def _remove_pair(self, idx):
        self._update_names()
        self._round.pairs.pop(idx)
        self._load_pairs()

    def _new_pair(self):
        self._update_names()
        filename = askopenfilename()
        try:
            image = Image.load_from_file(filename)
            self._round.pairs.append(("Uusi kuva", image))
            self._load_pairs()
        except UnidentifiedImageError:
            msg = FlashMessage(self, "Kuvan avaaminen ei onnistunut", "#a00612", "#c8abb6")
            msg.show_timer(None, 800)

    def _finish(self):
        self._update_names()
        self._game_edit_view.finish_round_edit()
        self.destroy()
