# Written with Textual 0.52.1

from decimal import Decimal
import operator

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import reactive
from textual.widgets import Button, Digits


class CalculatorApp(App[None]):
    CSS_PATH = "myapp.tcss"

    result = reactive(0)
    last_typed = reactive(0)
    number_displayed = reactive("0")
    value = reactive("")
    show_ac = reactive(True)
    operator = operator.add

    def compose(self) -> ComposeResult:
        yield Digits(id="display")
        with Grid():
            yield Button("AC", id="ac", classes="top")
            yield Button("C", id="c", classes="top")
            yield Button("+/-", id="negate", classes="top")
            yield Button("%", id="percent", classes="top")
            yield Button.warning("/", id="truediv", classes="operator")
            yield Button("7", id="number-7", classes="number")
            yield Button("8", id="number-8", classes="number")
            yield Button("9", id="number-9", classes="number")
            yield Button.warning("*", id="mul", classes="operator")
            yield Button("4", id="number-4", classes="number")
            yield Button("5", id="number-5", classes="number")
            yield Button("6", id="number-6", classes="number")
            yield Button.warning("-", id="sub", classes="operator")
            yield Button("1", id="number-1", classes="number")
            yield Button("2", id="number-2", classes="number")
            yield Button("3", id="number-3", classes="number")
            yield Button.warning("+", id="add", classes="operator")
            yield Button("0", id="number-0", classes="number")
            yield Button(",", id="point")
            yield Button.warning("=", id="equals")

    def compute_show_ac(self) -> None:
        return self.value in ("", "0")

    def watch_show_ac(self, show_ac: bool) -> None:
        self.query_one("#ac").display = show_ac
        self.query_one("#c").display = not show_ac

    @on(Button.Pressed, ".number")
    def update_number_displayed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        _, _, digit = button_id.partition("-")
        if digit == self.value == "0":
            return
        self.number_displayed = self.value = self.value + digit

    def watch_number_displayed(self, new_value: str) -> None:
        self.query_one(Digits).update(new_value)

    def _do_math(self) -> None:
        self.result = self.operator(self.result, self.last_typed)
        self.number_displayed = str(self.result).rstrip("0.-") or "0"
        self.value = ""

    @on(Button.Pressed, ".operator")
    def handle_operator_button(self, event: Button.Pressed) -> None:
        self.last_typed = Decimal(self.value or "0")
        self._do_math()
        op_name = event.button.id
        self.operator = getattr(operator, op_name)

    @on(Button.Pressed, "#equals")
    def handle_equals_press(self) -> None:
        if self.value:
            self.last_typed = Decimal(self.value)
        self._do_math()

    @on(Button.Pressed, "#point")
    def add_decimal_point(self) -> None:
        if "." in self.value:
            self.bell()
            return

        self.number_displayed = self.value = (self.value or "0") + "."

    @on(Button.Pressed, "#percent")
    def divide_by_hundred(self) -> None:
        self.number_displayed = self.value = str(Decimal(self.value or "0") / 100)

    @on(Button.Pressed, "#negate")
    def negate(self) -> None:
        if self.value:
            self.number_displayed = self.value = str(-1 * Decimal(self.value or "0"))

    @on(Button.Pressed, "#c")
    def clear_typed(self) -> None:
        self.value = ""
        self.number_displayed = "0"

    @on(Button.Pressed, "#ac")
    def clear_all(self) -> None:
        self.clear_typed()
        self.operator = operator.add
        self.last_typed = self.result = 0


if __name__ == "__main__":
    CalculatorApp().run()
