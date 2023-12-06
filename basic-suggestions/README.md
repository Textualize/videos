Show how to create an `Input` field with auto-completion suggestions.
Show that case-sensitivity can be turned off.


Start with:

```py
from textual.app import App, ComposeResult
from textual.widgets import Input


class SuggestionsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()


app = SuggestionsApp()
if __name__ == "__main__":
    app.run()
```
