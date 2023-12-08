Brief `Collapsible` demo.

Start with:

```py
from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Markdown


class CollapsiblesApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Markdown("**min**:\n\nUse `min` to get the minimum value of an iterable.")
        yield Markdown("**max**:\n\nUse `max` to get the maximum value of an iterable.")
        yield Markdown(
            "**sum**:\n\nUse `sum` to get sum the values inside an iterable."
        )


app = CollapsiblesApp()
if __name__ == "__main__":
    app.run()
```
