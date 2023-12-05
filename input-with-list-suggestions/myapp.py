# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.suggester import SuggestFromList
from textual.widgets import Input


countries = [
    "Portugal",
    "Scotland",
    "Spain",
]


class SuggestionsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(suggester=SuggestFromList(countries, case_sensitive=False))


app = SuggestionsApp()
if __name__ == "__main__":
    app.run()
