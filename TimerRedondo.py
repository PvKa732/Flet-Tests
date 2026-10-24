import flet as ft

def main(page: ft.Page):
    page.window.width = 1080
    page.window.height = 720
    page.window.resizable = False
    page.window.maximizable = False
    page.title = 'SLimites'
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale("pt", "BR")], current_locale=ft.Locale("pt", "BR"))
    page.padding = 0
    principal = ft.Container(
        expand=True,
        content=ft.Stack(
            alignment=ft.Alignment.CENTER,
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor='red',
                    width=110,
                    height=110,
                    border_radius=100
                ),
                ft.ProgressRing(value=0.6, width=100, height=100),
            ]
        )
    )

    page.add(principal)

ft.run(main)