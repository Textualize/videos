# Written with Textual 0.52.1

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.screen import ModalScreen
from textual.widgets import Label, Footer


class HelpScreen(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    DEFAULT_CSS = """
    HelpScreen {
        align: center middle;
    }

    #help-screen-container {
        width: auto;
        max-width: 70%;
        height: auto;
        max-height: 80%;
        background: $panel;
        align: center middle;
        padding: 2 4;

        & > Label#exit {
            margin-top: 1;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id="help-screen-container"):
            yield Label("This is the help screen.")
            yield Label("You've been helped.")
            yield Label("Press ESC to exit.", id="exit")


class MyApp(App[None]):
    BINDINGS = [("f1", "get_help", "Help")]

    def compose(self) -> ComposeResult:
        yield Label("This is my app.")
        yield Footer()

    def action_get_help(self) -> None:
        self.push_screen(HelpScreen())


if __name__ == "__main__":
    app = MyApp()
    app.run()
