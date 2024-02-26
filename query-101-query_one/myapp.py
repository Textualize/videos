# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Label


class QueryOneApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Label()
        yield Input()

    @on(Input.Submitted)
    def update_label(self, event: Input.Submitted) -> None:
        text_value = event.value
        self.query_one(Label).update(text_value)


if __name__ == "__main__":
    app = QueryOneApp()
    app.run()
