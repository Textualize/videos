Show how to create a custom `CommandPalette`.

1. start with a set of colours and an app with a method that accepts a colour name, builds a Static with that background colour, and mounts it dynamically;
3. create an instance of `Provider`;
4. implement `Provider.search`;
5. set `COMMANDS = {Provider}` in the app;
6. show the default commands disappeared; and
7. show how to update `COMMANDS` to preserve defaults.

Start with:

```py
# Written with Textual 0.43.1.

from textual.app import App
from textual.widgets import Static

COLOURS = {
    "red",
    "green",
    "blue",
    "white",
    "black",
}


class MyApp(App[None]):
    def on_mount(self) -> None:
        self.add_strip("white")
        self.add_strip("blue")

    def add_strip(self, colour: str) -> None:
        static = Static()
        static.styles.background = colour
        self.mount(static)


app = MyApp()
if __name__ == "__main__":
    app.run()
```
