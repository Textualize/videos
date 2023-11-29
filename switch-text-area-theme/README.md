Very similar to the video where we change `TextArea` syntax highlighting language.

1. Show that `TextArea` supports syntax highlighting theming via the parameter `theme`;
2. create a `Select` to allow changing the theme used for highlighting;
3. source the values from `text_area.available_themes`;
4. hook the two up so that the `Select` updates the reactive attribute `TextArea.theme`; and
5. mention it only works in 3.8+ and requires `pip install textual[syntax]`.

Starting point:

```py
# Written with Textual 0.43.0.

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import TextArea


class ThemeApp(App):
    def compose(self) -> ComposeResult:
        yield TextArea(language="python")


app = ThemeApp()
if __name__ == "__main__":
    app.run()
```
