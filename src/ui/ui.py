from tkinter import Tk, Button

class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Lukemisen harjoittelu')
        self._view = None
        self.show_start_view()

    def destroy_current_view(self):
        if self._view:
            self._view.destroy()
        self._view = None

    def show_start_view(self):
        self.destroy_current_view()

        self._view = Button(self, text="Aloita peli", command=self.show_game_view)
        self._view.pack()

    def show_game_view(self):
        self.destroy_current_view()

        # TODO
