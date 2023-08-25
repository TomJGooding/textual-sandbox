from textual.app import App, ComposeResult
from textual.widgets import Static


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Hello, World!")


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
