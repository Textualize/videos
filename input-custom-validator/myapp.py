# Written with Textual 0.44.1

from textual import on
from textual.app import App, ComposeResult
from textual.validation import ValidationResult, Validator
from textual.widgets import Input, RichLog


class LongBinary(Validator):
    def validate(self, value: str) -> ValidationResult:
        if len(value) < 10:
            return self.failure("Too short...")

        if set(value) - set("01"):
            return self.failure("Can only use digits 0 and 1.")

        return self.success()


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(
            validators=[LongBinary()],
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
