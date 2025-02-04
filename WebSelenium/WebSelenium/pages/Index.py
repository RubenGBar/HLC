import reflex as rx

from WebSelenium.Routes import Routes
from WebSelenium.views.Headers.Header import header

@rx.page(
    route=Routes.INDEX.value,
)
def index() -> rx.Component:
    return header()
