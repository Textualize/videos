# Written with Textual 0.43.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Input


class TitlesApp(App[None]):
    TITLE = "App title"
    SUB_TITLE = "App subtitle"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="title", id="title")
        yield Input(placeholder="subtitle", id="sub_title")

    @on(Input.Changed)
    def update_title(self, event: Input.Changed) -> None:
        # self.sub_title = event.value
        setattr(self, event.input.id, event.value)


if __name__ == "__main__":
    TitlesApp().run()
