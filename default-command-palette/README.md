1. show there's a default command palette with a couple of commands;
2. show default binding <kbd>Ctrl</kbd> + <kbd>\</kbd>;
3. toggle dark mode a couple of times and quit; and
4. change the app to yield a `Header` which has a button for the palette.

Starting point:

```py
# Written with Textual 0.42.0.

from textual.app import App


class MyApp(App[None]):
    pass


app = MyApp()
if __name__ == "__main__":
    app.run()
```
