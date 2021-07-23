from dominate.tags import *
from dominate import document

def getBasePage():

    doc = document(title=getTitle())

    with doc.head:
        link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css')
        link(rel='preconnect', href='https://fonts.googleapis.com')
        link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=True)
        link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap', crossorigin=True)
        script(type='text/javascript', src='https://code.jquery.com/jquery-3.2.1.slim.min.js')
        script(type='text/javascript', src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js')
        script(type='text/javascript', src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js', crossorigin="anonymous")
        script(type='text/javascript', src='https://kit.fontawesome.com/fa3537a8a2.js', crossorigin="anonymous")

    return doc

def getTitle()->str:
    return "Ultimate sensors UI premium deluxe day one master edition standard".upper()