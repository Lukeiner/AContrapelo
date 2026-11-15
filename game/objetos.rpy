## Objetos clicables del escenario
##
## Prueba en la habitación de A1E2: en lugar del menú de texto, el jugador
## hace clic sobre el objeto del fondo. Cada objeto es un rectángulo
## (x, y, ancho, alto) medido sobre el fondo de 1920x1080. Si cambia el
## fondo, hay que volver a medir los rectángulos.

init python:
    def recuadro(ancho, alto, borde, relleno, grosor=3):
        return Fixed(
            Solid(relleno, xysize=(ancho, alto)),
            Solid(borde, xysize=(ancho, grosor)),
            Solid(borde, xysize=(ancho, grosor), ypos=alto - grosor),
            Solid(borde, xysize=(grosor, alto)),
            Solid(borde, xysize=(grosor, alto), xpos=ancho - grosor),
            xysize=(ancho, alto),
        )

# Nombre que se muestra, valor que devuelve y rectángulo sobre el fondo
define objetos_habitacion = [
    ("Celular", "celular", (628, 492, 94, 44)),
    ("Computadora", "computadora", (1322, 342, 202, 146)),
    ("Boceto", "boceto", (1432, 488, 100, 50)),
]

screen objetos_escena(objetos):

    for nombre, valor, (x, y, ancho, alto) in objetos:
        button:
            pos (x, y)
            xysize (ancho, alto)
            idle_background recuadro(ancho, alto, "#f4efe455", "#ffffff0d")
            hover_background recuadro(ancho, alto, "#f4efe4", "#ffffff2e")
            action Return(valor)
            tooltip (nombre, x + ancho // 2, y)
            null

    $ globo = GetTooltip()

    if globo:
        frame:
            style "objeto_nombre_frame"
            xpos globo[1]
            ypos globo[2] - 10
            text globo[0] style "objeto_nombre_text"

    frame:
        style "objeto_ayuda_frame"
        text "Hacé clic en un objeto" style "objeto_ayuda_text"

style objeto_nombre_frame is frame:
    xanchor 0.5
    yanchor 1.0
    padding (18, 8)
    background "#111111dd"

style objeto_nombre_text is text:
    color "#f4efe4"
    size 30

style objeto_ayuda_frame is frame:
    xalign 0.5
    ypos 24
    padding (22, 10)
    background "#111111aa"

style objeto_ayuda_text is text:
    color "#f4efe4"
    size 26
