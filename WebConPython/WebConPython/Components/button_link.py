import reflex as rx

from WebConPython.styles.styles import button_title_style, button_body_style


def button_link(texto1, texto2, url) -> rx.Component:
    return rx.button(
        rx.link(
            rx.vstack(
              rx.text(texto1, style= button_title_style),
                rx.text(texto2, style= button_body_style)
            ),
            href=url,
            is_external=True,
            color_scheme="mint"
        ),
        color_scheme="tomato",
    )