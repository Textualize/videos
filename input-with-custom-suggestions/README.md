Show an `Input` that gets custom auto-completion suggestions.

 - subclass `Suggester`
 - override `get_suggestion` (explain its signature)
 - use `Path.glob` to look for a file with that name
 - show how it works
 - disable cache


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
