# pylint käyttäytyy tässä eri tavalla kuin python itse, jotain on varmaankin
# pielessä moduulihierarkiassa
from ui import UI # pylint: disable=no-name-in-module

def main():
    window = UI()
    window.mainloop()

if __name__ == "__main__":
    main()
