# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class OnApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Exit", id="exit")
        yield Button("Bell", id="bell")

    @on(Button.Pressed, "#exit")
    def button_exit_app(self) -> None:
        self.exit()

    @on(Button.Pressed, "#bell")
    def button_ring_bell(self) -> None:
        self.bell()


if __name__ == "__main__":
    app = OnApp()
    app.run()
