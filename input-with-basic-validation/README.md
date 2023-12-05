Show basic input validation that we can do.

 - set `type` to `integer` and `number`
 - set `max_length`
 - set `restrict` to allow numbers in binary only
 - stress that the regex applies to the WHOLE field

Start with:

```py
from textual.app import App, ComposeResult
from textual.widgets import Input


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()


app = ValidatedInputApp()
if __name__ == "__main__":
    app.run()
```
