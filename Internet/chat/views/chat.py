import flet as ft
from asyncio import create_task
cor_principal = ft.Colors.BLUE_400
cor_segundario = ft.Colors.WHITE
cor = ft.Colors.BLUE_400

lista_msg = [] #formato = ('Usuario', 'Olá'), ('Usuario2', 'Olá'), ('Você', ['a'])

async def scrollend():
        await rw.scroll_to(offset=-1,)

def mandar_msg(msg, nick):
    global lista_msg
    if msg:
        txt.value = None
        lista_msg.append((nick, [msg]))
        carregar_msg()
        create_task(scrollend())

def carregar_msg():
    containers = []
    def criar_container(alig, br, nick, msg):
        return ft.Container(expand=True, alignment=alig, content=ft.Column(
                            spacing=5,
                            controls=[
                                    ft.Container(expand=True, alignment=alig, content=
                                        ft.Container(width=250, height=20, bgcolor=cor, border_radius=ft.BorderRadius.only(top_left=br[4], bottom_left=br[5], bottom_right=br[6], top_right=br[7]), alignment=ft.Alignment.CENTER, content=
                                            ft.Text(nick, size=15, weight=ft.FontWeight.W_600,)
                                            )
                                        ),
                                    ft.Container(expand=True, alignment=alig, content=
                                        ft.Container(width=250, height=70, bgcolor=cor, border_radius=ft.BorderRadius.only(top_left=br[0], bottom_left=br[1], bottom_right=br[2], top_right=br[3]), content=
                                            ft.Stack(
                                                controls=[
                                                    ft.Container(expand=True, alignment=ft.Alignment.CENTER, content=ft.Text(msg, selectable=True)
                                                )
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
    for msg in lista_msg:
        usuario = msg[0]
        mensagem = msg[1]
        if type(mensagem) == list:
            containers.append(
                criar_container(ft.Alignment.TOP_RIGHT, [5, 30, 5, 5, 30, 5, 5, 5], usuario, mensagem[0]) 
            )
        else:
            containers.append( 
                criar_container(ft.Alignment.TOP_LEFT, [5, 5, 30, 5, 5, 5, 5, 30], usuario, mensagem)
            )
    containers.append(ft.Container(width=250, height=100))
    rw.controls = containers


txt = ft.TextField(
            expand=True,
            border_radius=30,
            border_color=cor_principal,
            cursor_color=cor_principal,
            color=cor_segundario,
            shift_enter=True,
            text_style=ft.TextStyle(
                size=12,
            ),
    )

bt = ft.FilledIconButton(icon=ft.Icons.SEND, bgcolor=cor, icon_color=cor_segundario)

rw = ft.Column(
    scroll=ft.ScrollMode.HIDDEN,
)

def chat(page, value):
    carregar_msg()

    bt.on_click=lambda e: mandar_msg(txt.value, value)

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == 'Enter':
            mandar_msg(txt.value, value)
        
    page.on_keyboard_event = on_keyboard

    principal = ft.Column(
        expand=True,
        controls=[
            ft.Container(expand=10, padding=10, content=rw),
            ft.Container(expand=1, padding=10, bgcolor=ft.Colors.with_opacity(0.04, ft.Colors.WHITE), alignment=ft.Alignment.CENTER, content=ft.Row(
                controls=[
                    txt,
                    bt
                ]
            ))
        ]
    )
    return ft.View(
                    route="/chat",
                    padding = 0,
                    controls=[
                        principal
                    ]
    )
