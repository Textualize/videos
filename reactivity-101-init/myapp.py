# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.color import Color
from textual.containers import Horizontal
from textual.reactive import var
from textual.widgets import Input, Static


class ComputedApp(App[None]):
    CSS_PATH = "myapp.tcss"

    red = var(255)
    green = var(255)
    blue = var(255)
    color = var(Color.parse("transparent"))

    def compose(self) -> ComposeResult:
        with Horizontal(id="color-inputs"):
            yield Input(placeholder="Enter red 0-255", id="red")
            yield Input(placeholder="Enter green 0-255", id="green")
            yield Input(placeholder="Enter blue 0-255", id="blue")
        yield Static(id="color")

    def compute_color(self) -> Color:
        return Color(self.red, self.green, self.blue)

    def watch_color(self, color: Color) -> None:
        self.query_one(Static).styles.background = color

    @on(Input.Changed)
    def update_color_component(self, event: Input.Changed) -> None:
        try:
            component = int(event.value or "0")
        except ValueError:
            self.bell()
        else:
            if event.input.id == "red":
                self.red = component
            elif event.input.id == "green":
                self.green = component
            else:
                self.blue = component


if __name__ == "__main__":
    app = ComputedApp()
    app.run()
