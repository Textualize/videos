# Written with Textual 0.43.2

from textual import log
from textual.app import App


class LogApp(App[None]):
    def key_l(self) -> None:
        log.info("Pressed L")
        log.warning("WATCH OUT!")
        log.error("💣")


app = LogApp()
if __name__ == "__main__":
    app.run()
