Show `Input` instances and the built-in validators:

 - `Function`
 - `Integer`
 - `Length`
 - `Number`
 - `Regex`
 - `URL`
 - mention video that shows how to work with validation in more detail, including other parameters, dealing with failures, etc

Start with:

```py
# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.widgets import Input


class ValidatorShowcaseApp(App[None]):
    def compose(self) -> ComposeResult:
        ...


app = ValidatorShowcaseApp()
if __name__ == "__main__":
    app.run()
```
