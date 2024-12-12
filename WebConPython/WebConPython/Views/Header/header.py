import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="RG", variant="solid"),
            rx.text("@rubengarcia")
        ),
        rx.text("Hola mi nombre es Rubén García")
    )
