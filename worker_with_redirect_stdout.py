import contextlib
from time import sleep

from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Footer, RichLog


def long_blocking_process() -> None:
    print("Connecting")
    sleep(3)
    print("Searching")
    sleep(3)
    print("Creating")


class OutputLog:
    def __init__(self, log: RichLog) -> None:
        self.log = log

    def write(self, text: str) -> None:
        if text.strip():
            app = self.log.app
            app.call_from_thread(self.log.write, text)

    def flush(self) -> None:
        pass


class WorkerWithRedirectStdoutApp(App):
    BINDINGS = [
        ("space", "run_long_blocking_process", "Run long blocking process"),
    ]

    def compose(self) -> ComposeResult:
        yield RichLog()
        yield Footer()

    @work(exclusive=True, thread=True)
    def action_run_long_blocking_process(self) -> None:
        log = self.query_one(RichLog)
        with contextlib.redirect_stdout(OutputLog(log)):  # type: ignore[type-var]
            long_blocking_process()


if __name__ == "__main__":
    app = WorkerWithRedirectStdoutApp()
    app.run()
