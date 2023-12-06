# Written with Textual 0.44.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Log, RichLog


class LogApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Click me!")
        yield RichLog()
        yield Log()

    @on(Button.Pressed)
    def log_press(self, event: Button.Pressed) -> None:
        self.query_one(RichLog).write(event)
        self.query_one(Log).write_line(str(event))


app = LogApp()
if __name__ == "__main__":
    app.run()
