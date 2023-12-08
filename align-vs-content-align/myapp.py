"""
Show the difference between align and content-align:
 - using align on #outer moves the label around
 - using content-align on #outer moves the text of the static around
 - using align on #inner does nothing
 - using content-align on #inner moves the label text
"""

# Written with Textual 0.45.0

from textual.app import App, ComposeResult
from textual.widgets import Static, Label


class AlignmentApp(App[None]):
    CSS_PATH = "myapp.tcss"

    def compose(self) -> ComposeResult:
        with Static("Some text!", id="outer"):
            yield Label("oi", id="inner")


app = AlignmentApp()
if __name__ == "__main__":
    app.run()
