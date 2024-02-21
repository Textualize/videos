# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input


class Name(Widget):
    """Generates a greeting."""

    who = reactive("name")

    def render(self) -> str:
        return f"Hello, {self.who}!"


class NameApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter your name")
        yield Name()

    @on(Input.Changed)
    def update_who(self, event: Input.Changed) -> None:
        self.query_one(Name).who = event.value


if __name__ == "__main__":
    NameApp().run()
