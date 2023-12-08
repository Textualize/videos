"""
Show how to use styles.animate to animate a style.
"""

# Written with Textual 0.44.1
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class DisappearingButton(App[None]):
    def compose(self) -> ComposeResult:
        yield Button()
        yield Button()
        yield Button()
        yield Button()

    @on(Button.Pressed)
    def make_button_disappear(self, event: Button.Pressed) -> None:
        event.control.styles.animate("opacity", 0, duration=3)


app = DisappearingButton()
if __name__ == "__main__":
    app.run()
