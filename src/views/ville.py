from logging import PlaceHolder
from dominate.tags import *
from utils.tools import strftimestamp
from views.base import getBasePage, getTitle

def temperatureVille(temperature, ville):

    doc = getBasePage()
    title = getTitle()

    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="mb-3"):
                h2(f"La temperature dans la ville de {ville} est actuellement de {temperature}C")
                a("RETURN TO HOMEPAGE", href="/", style="font-family: 'Press Start 2P', cursive;")


    return doc.render()
