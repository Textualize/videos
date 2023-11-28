from textual.app import App
from textual.widgets import Footer, Header


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        """What widgets is the app composed of?"""
        yield Header(show_clock=True)
        yield Footer()

    # This is an ACTION method.
    # It's an action method because it starts with action_
    # It's associated with the action called toggle_dark_mode.
    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
