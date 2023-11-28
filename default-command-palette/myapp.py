# Written with Textual 0.42.0.

from textual.app import App, ComposeResult
from textual.widgets import Header


class MyApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Header()


app = MyApp()
if __name__ == "__main__":
    app.run()
