from textual.app import App
from textual.containers import Grid
from textual.widgets import Placeholder


class ModalScreenApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        with Grid():
            for letter in "abcdefghij":
                yield Placeholder(id=letter)


if __name__ == "__main__":
    ModalScreenApp().run()
