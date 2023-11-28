# Written with Textual 0.42.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Select, TextArea


class ThemeApp(App):
    def compose(self) -> ComposeResult:
        text_area = TextArea(theme="dracula", language="python")
        yield Select(
            [(theme, theme) for theme in sorted(text_area.available_themes)],
            prompt="Language",
            allow_blank=False,
        )
        yield text_area

    @on(Select.Changed)
    def update_syntax_highlighting(self, event: Select.Changed) -> None:
        self.query_one(TextArea).theme = event.value


app = ThemeApp()
if __name__ == "__main__":
    app.run()
