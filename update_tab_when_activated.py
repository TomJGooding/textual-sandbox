from datetime import datetime

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, TabbedContent, TabPane


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Submitted", id="submitted"):
                yield Label("Last viewed: ...")
            with TabPane("In Progress", id="in-progress"):
                yield Label("Last viewed: ...")
            with TabPane("Completed", id="completed"):
                yield Label("Last viewed: ...")

    @on(TabbedContent.TabActivated)
    def on_tabbed_content_tab_activated(
        self, event: TabbedContent.TabActivated
    ) -> None:
        message: str = f"Last viewed: {datetime.now()}"
        pane = event.tabbed_content.query_one(
            f"TabPane#{event.tab.id}",
            TabPane,
        )
        pane.query_one(Label).update(message)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
