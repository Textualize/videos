"""
Show how to create a sidebar that you can easily show/hide.
For this example, use it for logging.
"""

# Written with Textual 0.44.1

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Log


class Sidebar(Container):
    def compose(self) -> ComposeResult:
        yield Log()

    def log_to_sidebar(self, msg: str) -> None:
        self.query_one(Log).write_line(msg)


class AppWithSidebar(App[None]):
    CSS = """
    Screen {
        layers: sidebar;
    }

    Sidebar {
        width: 30;
        height: 100%;
        dock: left;
        layer: sidebar;
    }

    Sidebar.-hidden {
        display: none;
    }
    """

    BINDINGS = [("ctrl+s", "toggle_sidebar")]

    def compose(self) -> ComposeResult:
        yield Sidebar(classes="-hidden")
        yield Button.success("Yes!")
        yield Button.error("No...")

    def action_toggle_sidebar(self) -> None:
        self.query_one(Sidebar).toggle_class("-hidden")

    @on(Button.Pressed)
    def log_button_press(self, event: Button.Pressed) -> None:
        self.query_one(Sidebar).log_to_sidebar(str(event.button.label))


app = AppWithSidebar()
if __name__ == "__main__":
    app.run()
