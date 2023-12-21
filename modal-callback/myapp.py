from textual import on
from textual.app import App
from textual.containers import Container, Grid, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Placeholder


class YesOrNo(ModalScreen):
    def compose(self):
        with Container():
            yield Label("Yes or no?")
            with Horizontal():
                yield Button.success("Yes", id="yes")
                yield Button.error("No", id="no")

    @on(Button.Pressed)
    def exit_screen(self, event):
        button_id = event.button.id
        self.dismiss(button_id == "yes")


class ModalScreenApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        with Grid():
            for _ in range(9):
                yield Placeholder(variant="text")

    def key_e(self):
        self.push_screen(YesOrNo(), callback=self.modal_callback_to_exit)

    def modal_callback_to_exit(self, should_exit):
        if should_exit:
            self.exit()


if __name__ == "__main__":
    ModalScreenApp().run()
