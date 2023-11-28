# Written with Textual 0.42.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Select, TextArea


class TextAreaExample(App):
    def compose(self) -> ComposeResult:
        yield Select(
            [
                ("Python", "python"),
                ("Markdown", "markdown"),
            ],
            prompt="Language",
            allow_blank=False,
        )
        yield TextArea(language="python")

    @on(Select.Changed)
    def update_syntax_highlighting(self, event: Select.Changed) -> None:
        self.query_one(TextArea).language = event.value


app = TextAreaExample()
if __name__ == "__main__":
    app.run()
