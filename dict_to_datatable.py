from itertools import zip_longest

from textual.app import App, ComposeResult
from textual.widgets import DataTable

DATA = {
    "lane": [4, 2, 5, 6, 3, 8, 7, 1, 10],
    "swimmer": [
        "Joseph Schooling",
        "Michael Phelps",
        "Chad le Clos",
        "László Cseh",
        "Li Zhuhao",
        "Mehdy Metella",
        "Tom Shields",
        "Aleksandr Sadovnikov",
        "Darren Burns",
    ],
    "country": [
        "Singapore",
        "United States",
        "South Africa",
        "Hungary",
        "China",
        "France",
        "United States",
        "Russia",
        "Scotland",
    ],
    "time": [50.39, 51.14, 51.14, 51.14, 51.26, 51.58, 51.73, 51.84, 51.84],
}


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)

        columns = DATA.keys()
        rows = [
            [value for value in row]
            for row in zip_longest(  # type: ignore[call-overload]
                *[DATA[column] for column in columns],
                fillvalue=None,
            )
        ]

        table.add_columns(*columns)
        table.add_rows(rows)


app = TableApp()
if __name__ == "__main__":
    app.run()
