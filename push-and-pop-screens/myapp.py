# Written with Textual 0.43.2

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
        yield Button("Switch to B", id="switch")


class ScreenB(Screen):
    def compose(self) -> ComposeResult:
        yield Label("This is screen B")
        yield Button("Push A", id="a")
        yield Button("Push B", id="b")
        yield Button("Pop", id="pop")


class ScreensApp(App[None]):
    SCREENS = {
        "a": ScreenA(),
        "b": ScreenB(),
    }

    def compose(self) -> ComposeResult:
        yield Label("This is the base screen!")
        yield Button("Push A", id="a")
        yield Button("Push B", id="b")

    @on(Button.Pressed, "#pop")
    def pop_top_screen(self) -> None:
        self.pop_screen()
        print(self.screen_stack)

    @on(Button.Pressed, "#a, #b")
    def push(self, event: Button.Pressed) -> None:
        self.push_screen(event.button.id)
        print(self.screen_stack)

    @on(Button.Pressed, "#switch")
    def switch(self) -> None:
        self.switch_screen("b")
        print(self.screen_stack)


app = ScreensApp()
if __name__ == "__main__":
    app.run()
