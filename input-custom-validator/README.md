Show how to create a custom validator:

 - subclass `Validator`
 - override `validate`
 - return `self.failure(description)` if it fails
 - return `self.success` if it passes

Start with:

```py
# Written with Textual 0.44.1

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, RichLog


class ValidatedInputApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(
            validators=[],
            validate_on=["submitted"],
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
```
