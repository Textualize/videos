# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.validation import Function, Integer, Length, Number, Regex, URL
from textual.widgets import Input


class ValidatorShowcaseApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(
            placeholder=".py",
            validators=[Function(lambda s: s.endswith(".py"))],
        )
        yield Input(placeholder="integer", validators=[Integer()])
        yield Input(
            placeholder="long, but not too long",
            validators=[Length(minimum=5, maximum=10)],
        )
        yield Input(placeholder="number", validators=[Number()])
        yield Input(placeholder="regex", validators=[Regex("(ha)*")])
        yield Input(placeholder="url", validators=[URL()])


app = ValidatorShowcaseApp()
if __name__ == "__main__":
    app.run()
