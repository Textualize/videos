"""
Show what happens if you set .loading = True.
"""

# Written with Textual 0.44.1

from textual.app import App, ComposeResult
from textual.widgets import DataTable


class AutoFocusApp(App[None]):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        dt = self.query_one(DataTable)
        dt.add_columns("Name", "Based in")
        dt.add_rows(
            [
                ["Rodrigo", "Portugal"],
                ["Will", "Scotland"],
            ]
        )
        dt.loading = True
        # Pretend data will take 3s to load.
        self.set_timer(3, self.done_loading)

    def done_loading(self) -> None:
        dt = self.query_one(DataTable)
        dt.add_rows(
            [
                ["Dave", "<redacted>"],
                ["Darren", "<redacted>"],
            ]
        )
        dt.loading = False


app = AutoFocusApp()
if __name__ == "__main__":
    app.run()
