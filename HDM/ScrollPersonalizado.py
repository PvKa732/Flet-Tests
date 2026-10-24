import flet as ft
import asyncio
import flet.canvas as cn

def main(page: ft.Page):
    page.title = 'Scroll Personalizado'
    page.padding = 0
    limite = None
    fps = 60
    valor = None
    maxscroll = None

    def drag_started(e: ft.DragStartEvent):
        print("Começou a arrastar")

    def On_residseCanvas(e: cn.CanvasResizeEvent):
        nonlocal limite
        limite = e.height
        
    def rw_scroll(e):
        nonlocal maxscroll
        maxscroll = e.max_scroll_extent

    def acao_rwscroll(porcentagem):
            DCS =  maxscroll * 0.01 # 1% do maxscroll
            return DCS * porcentagem

    def dragupdate(e: ft.DragEndEvent):
        nonlocal valor
        valor = e.local_delta.y + botaoScroll.top
        maximo = limite - botaoScroll.content.height
        parado = max(0, min(valor, maximo))
        UPCP = maximo * 0.01
        porcentagem = parado / UPCP
        botaoScroll.top = parado
        botaoScroll.update()
        asyncio.create_task(ScrollAcao(acao_rwscroll(porcentagem))) 

    def drag_ended(e: ft.DragEndEvent):
        print("Soltou o botão depois de arrastar")

    async def Scroll(e):
            await rw.scroll_to(delta=-0.1, duration=200)

    async def ScrollAcao(valor):
            await rw.scroll_to(offset=valor)

    botaoScroll = ft.GestureDetector(
                    drag_interval=int(1000 / fps),
                    on_pan_update=dragupdate,
                    #on_pan_end=drag_ended,
                    #on_pan_start=drag_started, 
                    top=0,
                    content=ft.Container(
                        width=45,
                        height=90,
                        bgcolor=ft.Colors.with_opacity(0.8, "#F5B400"),
                        border_radius=10,
                        animate_offset=ft.Animation(
                            duration=600,
                            curve=ft.AnimationCurve.EASE_IN_OUT
                        ),
                )
            )

    scroll = ft.Container(
        expand=True,
        padding=10,
        alignment=ft.Alignment.TOP_CENTER,
        bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
        border_radius=20,
        content=ft.Stack(
            expand=True,
            alignment=ft.Alignment.TOP_CENTER,
            controls=[
                 ft.Container(
                      content=cn.Canvas(
                           on_resize=On_residseCanvas,
                           expand=True,
                      )
                 ),
                 botaoScroll
            ]
        )
    )

    rw = ft.Row(
        wrap=True,
        scroll=ft.ScrollMode.HIDDEN,
        on_scroll=rw_scroll,
        controls=[
            ft.Container(
                width=225,
                height=100,
                bgcolor=ft.Colors.LIME_300,
            ) for num in range(100)
        ]
    )
    asyncio.create_task(Scroll(None))
    elementos = ft.Stack(
        expand=True,
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        expand=16,
                        padding=ft.Padding.only(top=80, left=80, bottom=80),
                        content=rw
                    ),
                    ft.Container(
                        expand=1,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    expand=4,
                                ),
                                ft.Container(
                                    expand=5,
                                    padding=ft.Padding(right=23, left=23),
                                    content=scroll
                                ),
                                ft.Container(
                                    expand=4,
                                )
                            ]
                        )
                    )
                ]
            )
    ])

    principal = ft.Container(padding=5, expand=True, content=elementos)
    page.add(principal)

ft.run(main)

# Ação --------------------

# Primeiro, criar um front-end para o scroll personalizado (bordas arrendodas, cores vibrantes, etc) e obrigatóriamente um botão para segurar V
    # Segurou o botão: V
        # Detectar se o úsuario desceu ou subiu o mause (mas especificamente, a variável "Y" indicando cordenada do mause) V
            # Dá ação á um sistema que faça o botão de scroll subir ou descer de acordo com a movimentação e a posição do mause, e não subir ou descer, caso esteja no limite (mas especificamente na borda do container personalizado) V
# Criar um layout usando column/row V
    # Após o usuário segurar o botão, descer ou subir o layout com os elementos dentro de acordo com o tanto que o mause desceu ou subiu. V
        # (O SISTEMA TEM QUE ESTÁ FIEL AOS LIMITES DO SCROLL, se chegar no final, o row/column tem que está no final obrigatóriamente dependendo o tamanho do elemento, talvez usando algum calculo matemático.) V