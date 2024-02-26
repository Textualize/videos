# Written with Textual 0.52.1

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Label


class MarginVsPaddingApp(App[None]):
    CSS_PATH = "myapp.tcss"

    def compose(self) -> ComposeResult:
        with Container():
            yield Label("x")
            yield Label("y")
            yield Label("z")


if __name__ == "__main__":
    app = MarginVsPaddingApp()
    app.run()
