from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.screen import ModalScreen
from textual.widgets import Input, Label


class PwdScreen(ModalScreen):
    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Type your password:")
            yield Input(password=True)

    @on(Input.Submitted)
    def exit_app_with_password(self, event: Input.Submitted) -> None:
        self.app.exit(event.value)


class PwdApp(App[str]):
    CSS_PATH = "myapp.tcss"

    def on_mount(self) -> None:
        self.push_screen(PwdScreen())
