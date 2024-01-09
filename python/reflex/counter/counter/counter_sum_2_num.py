import reflex as rx

class SumState(rx.State):
    number1: str = ""
    number2: str = ""
    result: str = ""

    def sum_numbers(self):
        try:
            num1 = float(self.number1)
            num2 = float(self.number2)
            self.result = str(num1 + num2)
        except ValueError:
            self.result = "Error: Enter valid numbers"

def index():
    return rx.vstack(
        rx.input(
            placeholder="Enter number 1",
            value=SumState.number1,
            on_change=SumState.set_number1,
        ),
        rx.text(" + "),
        rx.input(
            placeholder="Enter number 2",
            value=SumState.number2,
            on_change=SumState.set_number2,
        ),
        rx.button(
            "Sum",
            on_click=SumState.sum_numbers,
        ),
        rx.text("="),
        rx.text(SumState.result),
    )

app = rx.App()
app.add_page(index)
