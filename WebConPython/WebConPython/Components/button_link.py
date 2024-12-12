import reflex as rx

def button_link(texto, url) -> rx.Component:
    return rx.button(
        rx.link(
            texto,
            href=url,
            is_external=True,
            color_scheme="mint"
        ),
        color_scheme="tomato"
    )