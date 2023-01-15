import flet as ft

from views.FletRouter import Router
from user_controls.app_bar import NavBar

def main(page: ft.Page):

    page.appbar = NavBar(page, ft)
    myRouter = Router(page, ft)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )
    page.update()


ft.app(target=main)