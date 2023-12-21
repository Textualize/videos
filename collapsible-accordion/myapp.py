# Written with Textual 0.46.0

from textual import on
from textual.app import App
from textual.containers import Container
from textual.widgets import Collapsible, Markdown


class Accordion(Container):
    def __init__(self):
        self._currently_expanded = None
        super().__init__()

    @on(Collapsible.Expanded)
    def collapse_other_expanded(self, event):
        if event.collapsible is self._currently_expanded:
            return
        if self._currently_expanded is not None:
            self._currently_expanded.collapsed = True
        self._currently_expanded = event.collapsible

    @on(Collapsible.Collapsed)
    def clear_currently_expanded(self):
        self._currently_expanded = None


class CollapsiblesApp(App):
    def compose(self):
        with Accordion():
            with Collapsible(title="min"):
                yield Markdown(
                    "**min**:\n\nUse `min` to get the minimum value of an iterable."
                )
            with Collapsible(title="max"):
                yield Markdown(
                    "**max**:\n\nUse `max` to get the maximum value of an iterable."
                )
            with Collapsible(title="sum"):
                yield Markdown(
                    "**sum**:\n\nUse `sum` to get sum the values inside an iterable."
                )


app = CollapsiblesApp()
if __name__ == "__main__":
    app.run()
