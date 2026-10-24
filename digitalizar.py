import flet as ft
import asyncio

def main(page: ft.Page):
    value = 'Texto digital'
    texto = ft.Text(value, size=40, weight=ft.FontWeight.W_600)

    async def digitalizar1(e):
        string = ''
        for letra in texto.value:
            if not letra.split():
                string = string + letra
            else:
                string = string + letra
                print(string)
                texto.value = string
                texto.update()
                await asyncio.sleep(0.1)
    
    async def digitalizar2(e):
        string = texto.value
        
        while len(texto.value) > 0:
            texto.value = texto.value[:-1]
            texto.update()
            await asyncio.sleep(0.05)

        # Parte 2: Escrever (usando o mesmo texto ou um novo)
        novo_conteudo = "Novo Texto!"
        for i in range(len(novo_conteudo) + 1):
            texto.value = novo_conteudo[:i]
            texto.update()
            await asyncio.sleep(0.1)
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    texto,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Button(
                                'Digitalizar 1',
                                on_click=digitalizar1
                            ),
                            ft.Button(
                                'Digitalizar 1',
                                on_click=digitalizar2
                            )
                        ]
                    )
                ]
            )
        ),
    )


ft.run(main)
