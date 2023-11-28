# Written with Textual 0.43.0.

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import TextArea, Markdown


class MDEditor(App[None]):
    CSS = """
    #ui > * {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="ui"):
            yield TextArea()
            yield Markdown()

    def on_mount(self) -> None:
        self.set_interval(5, self.update_preview)

    async def update_preview(self) -> None:
        await self.query_one(Markdown).update(self.query_one(TextArea).text)


if __name__ == "__main__":
    MDEditor().run()
