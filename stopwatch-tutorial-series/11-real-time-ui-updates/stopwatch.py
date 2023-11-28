from time import monotonic

from textual import on
from textual.app import App
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static


class TimeDisplay(Static):
    """Custom time display widget."""

    accumulated_time = 0
    start_time = monotonic()
    time_elapsed = reactive(0)

    def on_mount(self):
        self.update_timer = self.set_interval(
            1 / 60,
            self.update_time_elapsed,
            pause=True,
        )

    def update_time_elapsed(self):
        self.time_elapsed = self.accumulated_time + (monotonic() - self.start_time)

    def watch_time_elapsed(self):
        time = self.time_elapsed
        time, seconds = divmod(time, 60)
        hours, minutes = divmod(time, 60)
        time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"
        self.update(time_string)

    def start(self):
        """Start keeping track of the time elapsed."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        """Stop keeping track of the time elapsed."""
        self.accumulated_time = self.time_elapsed
        self.update_timer.pause()

    def reset(self):
        """Reset the time elapsed."""
        self.accumulated_time = 0
        self.time_elapsed = 0


class Stopwatch(Static):
    """Custom stopwatch widget."""

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")
        self.query_one(TimeDisplay).start()

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed, "#reset")
    def reset_stopwatch(self):
        self.query_one(TimeDisplay).reset()

    def compose(self):
        yield Button("Start", variant="success", id="start")
        yield Button("Stop", variant="error", id="stop")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    CSS_PATH = "stopwatch.tcss"

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
