# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.widgets import Input


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(max_length=3, restrict=r"[01]*")


app = ValidatedInputApp()
if __name__ == "__main__":
    app.run()
