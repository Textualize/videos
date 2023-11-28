from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static


class TimeDisplay(Static):
    """Custom time display widget."""


class Stopwatch(Static):
    """Custom stopwatch widget."""

    def compose(self):
        yield Button("Start", variant="success")
        yield Button("Stop", variant="error")
        yield Button("Reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        """What widgets is the app composed of?"""
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch()
            yield Stopwatch()
            yield Stopwatch()

    # This is an ACTION method.
    # It's an action method because it starts with action_
    # It's associated with the action called toggle_dark_mode.
    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
