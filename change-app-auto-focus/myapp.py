"""
Show how to disable and change AUTO_FOCUS.
Show that it doesn't break if the selector doesn't match.
"""

# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.widgets import Button, Input


class AutoFocusApp(App[None]):
    AUTO_FOCUS = "#second"

    def compose(self) -> ComposeResult:
        yield Input()
        yield Button()
        yield Input(id="second")


app = AutoFocusApp()
if __name__ == "__main__":
    app.run()
