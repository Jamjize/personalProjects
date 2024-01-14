import reflex as rx
from components.buttons import button_row

class State(rx.State):
    None


def index():
    return rx.box(
        rx.vstack(
            rx.input(),
            button_row(["C", "()", "%", "/"]),
            button_row(["7", "8", "9", "x"]),
            button_row(["4", "5", "6", "-"]),
            button_row(["1", "2", "3", "+"]),
            button_row(["+/-", "0", ".", "="]),
        )
    )

app = rx.App()
app.add_page(index)
