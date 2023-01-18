
import flet as ft

def SettingsView(page):

    def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else: 
            page.theme_mode = "dark"
            page.update()

    def exit_app(e):
        page.window_destroy()
    
    content = ft.Column(
               
            [
                ft.Row(
                [
                    ft.Text("My Settings", size=30), 
                    ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                    ],
                ),
                ft.Row(
                    [
                        ft.TextButton("Exit Application", icon=ft.icons.CLOSE, on_click=exit_app, icon_color="red")
                    ]
                ),
            ]
        )
    
    
    return content
