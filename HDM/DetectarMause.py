import asyncio
import flet as ft


def main(page: ft.Page):
    page.title = "Blocos na posição do mouse"
    page.padding = 0
    page.spacing = 0

    mouse_x = 0
    mouse_y = 0

    canvas = ft.Stack(expand=True)

    def on_hover(e):

        nonlocal mouse_x, mouse_y

        # Tenta e.x / e.y primeiro
        if hasattr(e, "x"):
            mouse_x = e.x
            mouse_y = e.y 
            print("eeeeeeeee") #essa ação não funciona nunca (esse if falha sempre.)
            
         # Se não, tenta e.local_position
        elif hasattr(e, "local_position"):
            pos = e.local_position
            if hasattr(pos, "x"):
                mouse_x = pos.x
                mouse_y = pos.y
            else:
                mouse_x = pos[0]
                mouse_y = pos[1]
            # local_position=Offset(x=1245.0, y=0...)

        # Fallback: tenta global_x / global_y (caso sua versão tenha)
        elif hasattr(e, "global_x"):
            mouse_x = e.global_x
            mouse_y = e.global_y
            # não há.

    detector = ft.GestureDetector(
        content=canvas,
        on_hover=on_hover,
        # hover_interval=50, # intervalo maximo de 50 milessimos
        expand=True,
    )

    async def adicionar_blocos():
        while True:
            await asyncio.sleep(0.1)

            bloco = ft.Container(
                width=40,
                height=40,
                bgcolor=ft.Colors.RED,
                border_radius=5,
                left=max(0, mouse_x - 20),
                top=max(0, mouse_y - 20),
            )

            canvas.controls.append(bloco)
            page.update()

    page.add(detector)

    page.run_task(adicionar_blocos)


ft.run(main)

#PointerEvent(name='hover', 
# data=None, 
# kind=<PointerDeviceType.MOUSE: 'mouse'>, 
# local_position=Offset(x=1245.0, y=0, transform_hit_tests=True, filter_quality=None), 
# global_position=Offset(x=1245.0, y=0, transform_hit_tests=True, filter_quality=None), 
# timestamp=Duration(microseconds=821, milliseconds=514, seconds=37, minutes=53, hours=14, days=0),
#  device=268435456, 
# pressure=0.0, 
# pressure_min=0.0, 
# pressure_max=0.0, 
# distance=0.0, 
# distance_max=0.0, 
# size=0.0, 
# radius_major=0.0, 
# radius_minor=0.0, 
# radius_min=0.0, 
# radius_max=0.0, 
# orientation=0.0, 
# tilt=0.0, 
# local_delta=Offset(x=-2.0, y=0, transform_hit_tests=True, filter_quality=None), global_delta=None)
