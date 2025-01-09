import reflex as rx

from WebConPython.Components.button_link import button_link

def links() -> rx.Component:
    return rx.vstack(

        button_link("IESNervion", "IESNervion","https://www.institutonervion.es/"),
        button_link("YouTube", "YouTube", "https://www.youtube.com/"),
        button_link("Twitch", "Twitch", "https://www.twitch.tv/"),
        align="center",

    )