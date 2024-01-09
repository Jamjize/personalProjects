import reflex as rx

class State(rx.State):
    counter: int = 0

    def decrement(self):
        self.counter -= 1

    def increment(self):
        self.counter += 1


def index():
    return rx.hstack(
        rx.button(
            rx.icon(tag="moon"),
            on_click=rx.toggle_color_mode,
        ),
        rx.button(
            "Decrement",
            on_click=State.decrement,
        ),
        rx.text(State.counter),
        rx.button(
            "Increment",
            on_click=State.increment,
        ),
    )

app = rx.App()
app.add_page(index)
