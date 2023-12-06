Show basic screen manipulation.

 - Method `push_screen` pushes screens on the stack
 - Method `pop_screen` pops screens from the stack
 - Popping the base screen will blow the universe up
 - You can also swap the top of the stack for another screen with `switch_screen`

Start with:

```py
from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label


class ScreenA(Screen):
    def compose(self) -> ComposeResult:
        yield Label("This is screen A")
        yield Button("Push A", id="a")
        yield Button("Push B", id="b")
        yield Button("Pop", id="pop")


class ScreensApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Label("This is the base screen!")
        yield Button("Push A", id="a")
        yield Button("Push B", id="b")


app = ScreensApp()
if __name__ == "__main__":
    app.run()
```
