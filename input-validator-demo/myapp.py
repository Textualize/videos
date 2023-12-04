# Written with Textual 0.44.1

from textual import on
from textual.app import App, ComposeResult
from textual.validation import Function, Length, Regex
from textual.widgets import Input, RichLog


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(
            validators=[
                Function(
                    lambda x: int(x) % 9 == 0,
                    failure_description="Not a multiple of 9...",
                ),
                Length(minimum=10, maximum=15),
                Regex("[0123]*", failure_description="Can only use digits 0123."),
            ],
            validate_on=["submitted"],
            valid_empty=True,
        )
        yield RichLog()

    @on(Input.Submitted)
    def handle_input_submission(self, event: Input.Submitted) -> None:
        rich_log = self.query_one(RichLog)
        rich_log.write(event.validation_result.is_valid)
        rich_log.write(event.validation_result.failure_descriptions)


app = ValidatedInputApp()
if __name__ == "__main__":
    app.run()
