Show how to do logging into the console with `textual.log`.

 - What you write ends up in the console
 - Several (pre-defined) log groups
 - The log groups can then be excluded in the console

Start with:

```py
from textual.app import App


class LogApp(App[None]):
    def key_l(self, event) -> None:
        pass


app = LogApp()
if __name__ == "__main__":
    app.run()
```
