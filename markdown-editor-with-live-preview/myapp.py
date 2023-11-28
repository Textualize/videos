# Written with Textual 0.43.0.

from textual import on
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

    @on(TextArea.Changed)
    async def update_preview(self, event: TextArea.Changed) -> None:
        await self.query_one(Markdown).update(event.text_area.text)


if __name__ == "__main__":
    MDEditor().run()
