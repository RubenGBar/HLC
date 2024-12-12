import reflex as rx

from WebJuegitos.Components.navbar_link import navbar_link

def navBar() -> rx.Component:
    return rx.hstack(
        navbar_link("Principal | ", "/#"),
        navbar_link("Juegitos | ", "/#"),
        position="sticky",
        padding_x="16px",
        padding_y="8px",
        z_index=999,

    )