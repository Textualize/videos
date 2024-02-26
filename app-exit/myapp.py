# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class ExitApp(App[int]):
    def compose(self) -> ComposeResult:
        yield Button("Exit")

    @on(Button.Pressed)
    def button_exit_app(self) -> None:
        self.exit(42, message="Hello, world!")


if __name__ == "__main__":
    app = ExitApp()
    number = app.run()
    print(number)
