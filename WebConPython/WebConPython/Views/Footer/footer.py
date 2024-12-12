import datetime
import reflex as rx

def footer()-> rx.Component:
    return rx.hstack(
        rx.icon("hand-metal"),
        rx.text(datetime.date.today().year),
        rx.link("PÁGINA DE RUBÉN GARCÍA", href="http://localhost:3001/")

    )