# Written with Textual 0.52.1

from decimal import Decimal
import operator

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import var
from textual.widgets import Button, Digits


class CalculatorApp(App[None]):
    CSS_PATH = "myapp.tcss"

    num_displayed = var("0")
    value = var("0")
    result = var(0)
    right = var(0)
    show_ac = var(True)
    operator = operator.add

    def compose(self) -> ComposeResult:
        yield Digits(id="display")
        with Grid(id="buttons"):
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

    @on(Button.Pressed, ".number")
    def update_number_displayed(self, event: Button.Pressed) -> None:
        _, _, num = event.button.id.partition("-")
        self.num_displayed = self.value = self.value.lstrip("0") + num

    def _do_math(self) -> None:
        self.result = self.operator(self.result, self.right)
        self.value = ""
        self.num_displayed = str(self.result)

    @on(Button.Pressed, ".operator")
    def operator_pressed(self, event: Button.Pressed) -> None:
        self.right = Decimal(self.value or "0")
        self._do_math()
        self.operator = getattr(operator, event.button.id)

    @on(Button.Pressed, "#equals")
    def equals_pressed(self) -> None:
        if self.value:
            self.right = Decimal(self.value)
        self._do_math()

    @on(Button.Pressed, "#point")
    def add_decimal_place(self) -> None:
        if "." in self.value:
            self.bell()
            return
        self.value = self.num_displayed = (self.value or "0") + "."

    @on(Button.Pressed, "#negate")
    def negate_number(self) -> None:
        if self.value.startswith("-"):
            self.value = self.num_displayed = self.value[1:]
        else:
            self.value = self.num_displayed = "-" + self.value

    @on(Button.Pressed, "#percent")
    def percent_pressed(self) -> None:
        self.value = self.num_displayed = str(Decimal(self.value or "0") / 100)

    def watch_num_displayed(self, displayed: str) -> None:
        self.query_one(Digits).update(displayed)

    @on(Button.Pressed, "#c")
    def clear_displayed(self) -> None:
        self.value = ""
        self.num_displayed = "0"

    @on(Button.Pressed, "#ac")
    def all_clear(self) -> None:
        self.value = ""
        self.num_displayed = "0"
        self.result = 0
        self.right = 0
        self.operator = operator.add

    def compute_show_ac(self) -> None:
        return self.value in ("", "0") and self.num_displayed == "0"

    def watch_show_ac(self, show_ac) -> None:
        self.query_one("#c").display = not show_ac
        self.query_one("#ac").display = show_ac


if __name__ == "__main__":
    CalculatorApp().run()
