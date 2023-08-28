from time import sleep

from textual import on, work
from textual.app import App, ComposeResult, events
from textual.widgets import Footer, RichLog


def long_blocking_process() -> None:
    print("Connecting")
    sleep(3)
    print("Searching")
    sleep(3)
    print("Creating")


class OutputLog(RichLog):
    @on(events.Print)
    def on_print(self, event: events.Print) -> None:
        # Prevent blank lines in the log
        if event.text.strip():
            self.write(event.text)


class WorkerWithCapturePrintApp(App):
    BINDINGS = [
        ("space", "run_long_blocking_process", "Run long blocking process"),
    ]

    def compose(self) -> ComposeResult:
        yield OutputLog()
        yield Footer()

    @work(exclusive=True, thread=True)
    def action_run_long_blocking_process(self) -> None:
        log = self.query_one(OutputLog)
        log.begin_capture_print()
        long_blocking_process()
        log.end_capture_print()


if __name__ == "__main__":
    app = WorkerWithCapturePrintApp()
    app.run()
