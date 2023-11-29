# Written with Textual 0.43.0.

from textual.app import App


class NotificationApp(App[None]):
    BINDINGS = [
        ("n", "notification"),
        ("w", "warning"),
        ("e", "error"),
    ]

    def action_notification(self):
        self.notify("This is a notification!", title="Notification title")

    def action_warning(self):
        self.notify("This is a warning!", severity="warning")

    def action_error(self):
        self.notify("💣 this was an error!", severity="error", timeout=10)


if __name__ == "__main__":
    NotificationApp().run()
