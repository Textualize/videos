from textual.app import App
from textual.containers import Grid
from textual.widgets import Placeholder


class GridApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        with Grid():
            yield Placeholder(id="a")
            yield Placeholder(id="b")
            yield Placeholder(id="c")
            yield Placeholder(id="d")


if __name__ == "__main__":
    GridApp().run()
