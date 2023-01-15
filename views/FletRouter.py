
import flet as ft # dev purposes only

# Nav Bar to give to views
from user_controls.app_bar import NavBar

# views
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView



class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/profile": ProfileView(page),
            "/settings": SettingsView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
