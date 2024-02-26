# Written with Textual 0.52.1

from textual.app import App, ComposeResult
from textual.widgets import Input, Label


class TooltipApp(App[None]):
    def compose(self) -> ComposeResult:
        label = Label("This is a regular widget.")
        label.tooltip = "This is a tooltip."
        yield label
        inp = Input()
        inp.tooltip = "Another tooltip!"
        yield inp


if __name__ == "__main__":
    app = TooltipApp()
    app.run()
