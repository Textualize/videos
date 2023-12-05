# Written with Textual 0.44.1

from pathlib import Path

from textual.app import App, ComposeResult
from textual.suggester import Suggester
from textual.widgets import Input


class FileSuggester(Suggester):
    async def get_suggestion(self, value: str) -> str | None:
        path = next(Path().glob(f"{value}*"), None)
        return str(path) if path else None


class SuggestionsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(suggester=FileSuggester(use_cache=False))


app = SuggestionsApp()
if __name__ == "__main__":
    app.run()
