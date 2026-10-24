import flet as ft
import asyncio

def main(page: ft.Page):
    block1 = ft.Container(
        data='block1',
        width=100,
        height=100,
        offset=ft.Offset(x=-0),
        animate_offset=ft.Animation(duration=250),
        bgcolor='red'
    )
    block2 = ft.Container(
        data='block2',
        width=100,
        height=100,
        offset=ft.Offset(x=-0),
        animate_offset=ft.Animation(duration=250),
        bgcolor='yellow'
    )

    async def animation(item_leave, item_join):
        # 1. slide the current block out to the left
        item_leave.offset = ft.Offset(x=-0.3)
        item_leave.update()
        await asyncio.sleep(0.3)

        # 2. jump the new block to the right side, no animation
        item_join.animate_offset = None
        item_join.offset = ft.Offset(x=0.3)
        Column.controls = [item_join]
        Column.update()
        await asyncio.sleep(0.05)

        # 2b. turn the animation back on while it's still sitting on the right
        item_join.animate_offset = ft.Animation(duration=250)
        item_join.update()
        await asyncio.sleep(0.05)

        # 3. now only the offset changes, so it animates in
        item_join.offset = ft.Offset(x=0)
        item_join.update()

    def next(e):
        data = Column.controls[0].data
        if data == 'block1':
            page.run_task(animation, block1, block2)
        else:
            page.run_task(animation, block2, block1)
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    Column := ft.Column(
                        controls=[block1]
                    ),
                    ft.Button('Next Block', on_click=next)
                ]
            )
        )
    )

ft.run(main)