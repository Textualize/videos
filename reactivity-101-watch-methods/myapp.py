# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.color import Color, ColorParseError
from textual.containers import Grid
from textual.reactive import reactive
from textual.widgets import Input, Static


class WatchApp(App[None]):
    CSS_PATH = "myapp.tcss"

    color = reactive(Color.parse("transparent"))

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter a color")
        with Grid(id="colors"):
            yield Static(id="old")
            yield Static(id="new")

    def watch_color(self, old_color: Color, new_color: Color) -> None:
        self.query_one("#old").styles.background = old_color
        self.query_one("#new").styles.background = new_color

    @on(Input.Submitted)
    def update_color(self, event: Input.Submitted) -> None:
        try:
            input_color = Color.parse(event.value)
        except ColorParseError:
            pass
        else:
            event.input.value = ""
            self.color = input_color


if __name__ == "__main__":
    app = WatchApp()
    app.run()
