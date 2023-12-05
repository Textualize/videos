Show how to do logging inside an app with the widgets `Log` and `RichLog`.

 - Textual has two widgets to do logging
 - `Log` is a bit lower level and it's just for strings
 - Show `python -m textual` using `Log`
 - `RichLog` is for arbitrary renderables
 - `RichLog.write` vs `Log.write_line`
 - Stress that this is logging _visible in the app_

Start with:

```py
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class LogApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Click me!")

    @on(Button.Pressed)
    def log_press(self, event) -> None:
        pass


app = LogApp()
if __name__ == "__main__":
    app.run()
```
