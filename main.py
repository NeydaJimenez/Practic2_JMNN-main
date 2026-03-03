import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO  

    titulo = ft.Text(
        "Formulario de Registro de Evento",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej: Congreso Empresarial 2026",
        width=420
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        width=420,
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        value="Presencial",
        content=ft.Row(
            [
                ft.Radio(value="Presencial", label="Presencial"),
                ft.Radio(value="Virtual", label="Virtual"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    requiere_inscripcion = ft.Checkbox(
        label="Requiere inscripción previa",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1,
        width=420
    )

    resumen = ft.Text(
        value="",
        size=15,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.GREY_800,
        text_align=ft.TextAlign.CENTER
    )

    def mostrar_resumen(e):
        if nombre_evento.value.strip() == "":
            resumen.value = "Debe ingresar un nombre de evento."
            resumen.color = ft.Colors.RED_400
        else:
            resumen.value = (
                f"Evento: {nombre_evento.value}\n"
                f"Tipo: {tipo_evento.value}\n"
                f"Modalidad: {modalidad.value}\n"
                f"Inscripción previa: {'Sí' if requiere_inscripcion.value else 'No'}\n"
                f"Duración: {int(duracion.value)} horas"
            )
            resumen.color = ft.Colors.GREY_800

        page.update()

    boton_resumen = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.PINK_200,
        color=ft.Colors.GREY_900
    )

    tarjeta = ft.Container(
        content=ft.Column(
            [
                titulo,
                subtitulo,
                ft.Divider(),
                nombre_evento,
                tipo_evento,
                ft.Text("Modalidad:", weight=ft.FontWeight.BOLD),
                modalidad,
                requiere_inscripcion,
                ft.Text("Duración estimada (horas):", weight=ft.FontWeight.BOLD),
                duracion,
                boton_resumen,
                ft.Divider(),
                resumen
            ],
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=500,
        padding=30,
        border_radius=15,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(0, 4)
        )
    )

    page.add(tarjeta)


if __name__ == "__main__":
    ft.app(target=main)
