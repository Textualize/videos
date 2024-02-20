Show that `watch` methods are called when the value is set.
They take zero, one, or two, parameters.

```py
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
            yield Static()

    def watch_color(self, color: Color) -> None:
        self.query_one(Static).styles.background = color

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
```
