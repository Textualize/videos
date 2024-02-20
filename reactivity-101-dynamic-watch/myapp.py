# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button, ProgressBar


class Counter(Widget):
    DEFAULT_CSS = "Counter { height: auto; }"
    counter = reactive(0)

    def compose(self) -> ComposeResult:
        yield Button("+10")

    @on(Button.Pressed)
    def increment_counter(self) -> None:
        self.counter += 10

    def validate_counter(self, new_value) -> int:
        return min(new_value, 100)


class DynamicWatchApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Counter()
        yield ProgressBar(total=100, show_eta=False)

    def on_mount(self):
        def update_progress(counter_value: int):
            self.query_one(ProgressBar).update(progress=counter_value)

        self.watch(self.query_one(Counter), "counter", update_progress)


if __name__ == "__main__":
    DynamicWatchApp().run()
