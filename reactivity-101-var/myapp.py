# Written with Textual 0.52.1

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widget import Widget
from textual.widgets import Button, Log, ProgressBar


class Counter(Widget):
    DEFAULT_CSS = "Counter { height: auto; }"
    counter = var(0)

    def compose(self) -> ComposeResult:
        yield Button("+10")

    @on(Button.Pressed)
    def increment_counter(self) -> None:
        self.counter += 10

    def validate_counter(self, new_value) -> int:
        return min(new_value, 100)

    def render(self):
        self.app.query_one(Log).write_line("Rendering.")
        return super().render()


class DynamicWatchApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Counter()
        yield ProgressBar(total=100, show_eta=False)
        yield Log()

    def on_mount(self) -> None:
        def update_progress_bar(counter_value: int) -> None:
            self.query_one(ProgressBar).progress = counter_value

        self.watch(
            self.query_one(Counter),
            "counter",
            update_progress_bar,
        )


if __name__ == "__main__":
    DynamicWatchApp().run()
