# Written with Textual 0.42.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Input


class TitlesApp(App[None]):
    BINDINGS = [("t", "change_title")]

    TITLE = "App title"
    SUB_TITLE = "App subtitle"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Title", id="title")
        yield Input(placeholder="Subtitle", id="sub_title")

    @on(Input.Changed)
    def update_header(self, event: Input.Changed):
        setattr(self, event.input.id, event.value)


if __name__ == "__main__":
    TitlesApp().run()
