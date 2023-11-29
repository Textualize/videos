1. Show that `TextArea` supports syntax highlighting via the parameter `language`;
2. create a `Select` to allow changing the language used for highlighting;
3. hook the two up so that the `Select` updates the reactive attribute `TextArea.language`; and
4. mention it only works in 3.8+ and requires `pip install textual[syntax]`.

Starting point:

```py
# Written with Textual 0.43.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import TextArea


class SyntaxHighlightingApp(App):
    def compose(self) -> ComposeResult:
        yield TextArea(language="python")


app = SyntaxHighlightingApp()
if __name__ == "__main__":
    app.run()
```
