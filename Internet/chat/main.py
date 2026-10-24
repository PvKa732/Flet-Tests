import flet as ft
from asyncio import create_task
from views.chat import chat

def main(page: ft.Page):
    cor_principal = ft.Colors.BLUE_400
    cor_segundario = ft.Colors.WHITE
    value = None
    def proxima_pagina(route):
        create_task(page.push_route(route))

    def verificar(e):
        nonlocal value
        value = txt.value
        if not value:
            pass
        else:
            proxima_pagina('/chat')

    txt = ft.TextField(
            width=160,
            height=40,
            border_radius=30,
            autofocus=True,
            border_color=cor_principal,
            cursor_color=cor_principal,
            color=cor_segundario,
            text_style=ft.TextStyle(
                size=12,
            ),
    )

    bt = ft.Button(ft.Text('Enter', color=ft.Colors.BLUE_400), height=50, width=200, on_click=verificar)
    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                    route="/",
                    padding = 0,
                    controls=[
                       ft.Container(
                             expand=True,
                             alignment=ft.Alignment.CENTER,
                             content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(expand=7, alignment=ft.Alignment.BOTTOM_CENTER, content=ft.Column(alignment=ft.MainAxisAlignment.END, spacing=0, controls=[ft.Text('Welcome to chat', size=40, weight=ft.FontWeight.W_800, color=ft.Colors.BLUE_400)])),
                                    ft.Container(expand=10, alignment=ft.Alignment.CENTER, content=ft.Column(controls=[ft.Container(padding=10, bgcolor=ft.Colors.with_opacity(0.04, ft.Colors.WHITE), height=175, width=200, border_radius=30, content=ft.Column(controls=[
                                        ft.Container(expand=5, alignment=ft.Alignment.TOP_CENTER, content=ft.Text('Do type your nick', size=15, weight=ft.FontWeight.W_600, color=ft.Colors.BLUE_400)), 
                                        ft.Container(expand=10, alignment=ft.Alignment.TOP_CENTER, content=txt,)])), bt])),
                                ]
                             )
                        )
                    ]
            )
        )
        try:
            if page.route == '/chat':
                page.views.append(
                    chat(page, value)
                )
        except Exception as e:
            print(e)
    
    page.on_route_change = route_change

    route_change()
    create_task(page.push_route('/'))
    #proxima_pagina('/chat')
    page.add(ft.Stack())

ft.run(main)