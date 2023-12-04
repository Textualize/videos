# Written with Textual 0.43.2

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Log, RichLog


class RichLogApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Click me!")
        yield RichLog()
        yield Log()

    def on_mount(self) -> None:
        self.query_one(RichLog).write("Mounted.")

    @on(Button.Pressed)
    def log_event(self, event) -> None:
        self.query_one(RichLog).write(event)
        self.query_one(Log).write_line(str(event))


app = RichLogApp()
if __name__ == "__main__":
    app.run()
