import reflex as rx

def button_row(symbols: list[str]) -> rx.component:
    return rx.hstack(
        rx.button(symbols[0]),
        rx.button(symbols[1]),
        rx.button(symbols[2]),
        rx.button(symbols[3])
    )
