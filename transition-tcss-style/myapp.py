"""
Show how to use the rule transition to animate a style change.
"""

# Written with Textual 0.44.1
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class DisappearingButton(App[None]):
    CSS = """
    Button {
        transition: background 1s;
        transition: opacity 3s;
    }

    .changed {
        background: red;
        opacity: 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button()
        yield Button()
        yield Button()
        yield Button()

    @on(Button.Pressed)
    def make_button_disappear(self, event: Button.Pressed) -> None:
        event.control.add_class("changed")


app = DisappearingButton()
if __name__ == "__main__":
    app.run()
