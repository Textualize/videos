from textual.app import App
from textual.containers import Container, Grid, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Placeholder


class YesOrNo(ModalScreen):
    def compose(self):
        with Container():
            yield Label("Yes or no?")
            with Horizontal():
                yield Button.success("Yes")
                yield Button.error("No")


class ModalScreenApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        with Grid():
            for _ in range(9):
                yield Placeholder(variant="text")

    def key_m(self):
        self.push_screen(YesOrNo())


if __name__ == "__main__":
    ModalScreenApp().run()
