Show how to work with validators and `Input`:

 - show that validators can stack
 - show `valid_empty`
 - show `validate_on`
 - check if the validation succeeded with `is_valid` on the event
 - add failure descriptions
 - check failure descriptions with `failure_descriptions`


Start with:

```py
# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.widgets import Input


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()


app = ValidatedInputApp()
if __name__ == "__main__":
    app.run()
```
