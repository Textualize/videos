# Written with Textual 0.43.1.

from functools import partial

from textual.app import App
from textual.command import Hit, Hits, Provider
from textual.widgets import Static


COLOURS = {
    "red",
    "green",
    "blue",
    "white",
    "black",
}


class ColourCommandProvider(Provider):
    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)

        for colour in COLOURS:
            score = matcher.match(colour)
            if score > 0:
                yield Hit(
                    score,
                    matcher.highlight(colour),
                    partial(self.app.add_strip, colour),
                    help=f"Create a {colour} strip.",
                )


class MyApp(App[None]):
    COMMANDS = App.COMMANDS | {ColourCommandProvider}

    def add_strip(self, colour: str) -> None:
        static = Static()
        static.styles.background = colour
        self.mount(static)


app = MyApp()
if __name__ == "__main__":
    app.run()
