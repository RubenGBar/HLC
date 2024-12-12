import reflex as rx

from WebConPython.Views.Footer.footer import footer
from WebConPython.Views.Header.header import header
from WebConPython.Views.Links.links import links
from WebConPython.Views.NavBar.navbar import navbar

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        align="center"
    )

app = rx.App()
app.add_page(index)
app._compile()