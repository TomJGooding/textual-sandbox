from datetime import datetime

from rich.text import Text
from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Header
from textual.widgets._header import HeaderClock, HeaderClockSpace
from typing_extensions import override


class CustomHeaderClock(HeaderClock):
    DEFAULT_CSS = """
    CustomHeaderClock {
        width: auto;
    }
    """

    def __init__(self, time_format: str = "%X") -> None:
        """Initialize a custom header clock.

        Args:
            time_format: strftime format codes to format the time.
        """
        super().__init__()
        self.time_format = time_format

    @override
    def render(self) -> RenderResult:
        return Text(datetime.now().strftime(self.time_format))


class CustomHeaderClockApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

    # Example of 12hr clock with AM/PM
    # def on_mount(self) -> None:
    #     header = self.query_one(Header)
    #     header.query_one(HeaderClockSpace).remove()
    #     header.mount(
    #         CustomHeaderClock(time_format="%I:%M:%S %p"),
    #     )

    # Example including the weekday and date
    def on_mount(self) -> None:
        header = self.query_one(Header)
        header.query_one(HeaderClockSpace).remove()
        header.mount(
            CustomHeaderClock(time_format="%a, %b %d | %I:%M%p"),
        )


if __name__ == "__main__":
    app = CustomHeaderClockApp()
    app.run()
