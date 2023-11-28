from textual.app import App
from textual.widgets import Footer, Header


class StopwatchApp(App):
    def compose(self):
        """What widgets is the app composed of?"""
        yield Header(show_clock=True)
        yield Footer()


if __name__ == "__main__":
    StopwatchApp().run()
