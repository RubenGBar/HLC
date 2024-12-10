import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola buenos días", size="9", weight="bold")

app = rx.App()
app.add_page(index)
app._compile()