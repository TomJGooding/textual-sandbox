import httpx
from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Static


class WorkerWithIntervalApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Europe/Amsterdam")
        yield Static(id="time")

    def on_mount(self) -> None:
        self.set_interval(1, self.update_time)  # type: ignore[arg-type]

    @work(exclusive=True)
    async def update_time(self) -> None:
        time_widget = self.query_one("#time", Static)
        url = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            time_str = f"{data['hour']:02}:{data['minute']:02}:{data['seconds']:02}"
            time_widget.update(time_str)


if __name__ == "__main__":
    app = WorkerWithIntervalApp()
    app.run()
