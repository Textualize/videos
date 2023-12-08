"""
Show how to create a basic countdown timer with `Digits`, `set_interval`, and reactives.
"""

# Written with Textual 0.44.1.

from textual.app import App, ComposeResult
from textual.containers import Center, Middle
from textual.reactive import reactive
from textual.widgets import Digits


class CountdownApp(App[None]):
    CSS = """
    Digits {
        width: auto;
    }
    """

    time_left = reactive(15, init=False)

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield Digits()

    def tick(self) -> None:
        self.time_left -= 1
        if not self.time_left:
            self.tick_timer.stop()

    def watch_time_left(self, time_left: int) -> None:
        time, seconds = divmod(time_left, 60)
        hours, minutes = divmod(time, 60)
        self.query_one(Digits).update(f"{hours:02}:{minutes:02}:{seconds:02}")

    def on_mount(self) -> None:
        self.tick_timer = self.set_interval(1, self.tick)


app = CountdownApp()
if __name__ == "__main__":
    app.run()
