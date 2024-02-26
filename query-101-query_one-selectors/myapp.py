# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Label


class QueryOneApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Label("Type something:")
        yield Input()
        yield Label(id="to_be_updated")

    @on(Input.Submitted)
    def update_label(self, event: Input.Submitted) -> None:
        text_value = event.value
        self.query_one("Screen > Label#to_be_updated", Label).update(text_value)


if __name__ == "__main__":
    app = QueryOneApp()
    app.run()
