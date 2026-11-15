## Objetos clicables del escenario
##
## En las escenas de exploración, el jugador hace clic sobre el objeto del
## fondo en lugar de elegirlo de un menú de texto. Cada objeto es un
## rectángulo (x, y, ancho, alto) medido sobre el fondo de 1920x1080.
## Si cambia el fondo, hay que volver a medir sus rectángulos.
##
## Lo que no se ve en el fondo (gente fuera de cuadro, puertas que no
## entran en la imagen) va como botón abajo a la derecha.

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

# A1E2 (Habitacion_dia.jpg)
define objetos_habitacion = [
    ("Celular", "celular", (628, 492, 94, 44)),
    ("Computadora", "computadora", (1322, 342, 202, 146)),
    ("Boceto", "boceto", (1432, 488, 100, 50)),
]

# A1E4 (Cocina.jpg). No hay táper ni mate dibujados: provisorio, el frasco y la pava
define objetos_cocina = [
    ("Heladera", "heladera", (1265, 60, 435, 900)),
    ("Táper de María", "taper", (15, 715, 165, 250)),
    ("Mate", "mate", (200, 355, 185, 195)),
]

# A1E5 (Comedor_dia.jpg)
define objetos_comedor_acto1 = [
    ("Impuestos", "impuestos", (785, 525, 420, 70)),
    ("Puerta de salida", "puerta", (190, 20, 205, 780)),
]

# A2E15 (Habitacion_ordenada.jpg)
define objetos_habitacion_ordenada = [
    ("Celular", "celular", (622, 492, 100, 42)),
    ("Boceto", "boceto", (1432, 488, 100, 48)),
    ("Puerta al comedor", "puerta", (1735, 40, 185, 960)),
]

# A2E16 (Comedor_pagadas.jpg)
define objetos_comedor_pagadas = [
    ("Impuestos pagados", "impuestos", (898, 498, 145, 85)),
    ("Puerta de salida", "puerta", (190, 20, 205, 780)),
]

# A2E38 (Parada_micro.jpg). La gente está fuera de cuadro
define objetos_garita = [
    ("Asiento de la garita", "asiento", (428, 590, 195, 195)),
]
define botones_garita = [("Personas", "personas")]

# A2E41 (Comedor_pagadas.jpg). Solo se ve la puerta de salida
define objetos_comedor_encierro = [
    ("Puerta de salida", "salida", (190, 20, 205, 780)),
]
define botones_comedor_encierro = [
    ("Puerta a la habitación", "habitacion"),
    ("Puerta al baño", "bano"),
]

# A2E42 (Habitacion_dia.jpg)
define objetos_habitacion_encierro = [
    ("Boceto", "boceto", (1432, 488, 100, 50)),
    ("Computadora", "computadora", (1322, 342, 202, 146)),
    ("Puerta al comedor", "puerta", (1735, 40, 185, 960)),
]

# A2E43 (Bano.jpg)
define objetos_bano = [
    ("Espejo", "espejo", (80, 0, 460, 500)),
    ("Máquina de cortar pelo", "maquina", (522, 665, 285, 140)),
    ("Puerta al comedor", "puerta", (1655, 380, 140, 500)),
]

# A3E46. TEMPORAL: la habitación deteriorada usa Habitacion_dia.jpg (AR3-10); con la imagen nueva hay que volver a medir
define objetos_habitacion_acto3 = [
    ("Celular", "celular", (628, 492, 94, 44)),
    ("Computadora", "computadora", (1322, 342, 202, 146)),
    ("Boceto", "boceto", (1432, 488, 100, 50)),
]

screen objetos_escena(objetos, botones=[]):

    for nombre, valor, (x, y, ancho, alto) in objetos:
        button:
            pos (x, y)
            xysize (ancho, alto)
            idle_background recuadro(ancho, alto, "#f4efe455", "#ffffff0d")
            hover_background recuadro(ancho, alto, "#f4efe4", "#ffffff2e")
            action Return(valor)
            # El nombre va arriba del objeto, sin salirse de la pantalla
            tooltip (nombre, x + ancho // 2, max(y, 82))
            null

    $ globo = GetTooltip()

    if globo:
        frame:
            style "objeto_nombre_frame"
            xpos globo[1]
            ypos globo[2] - 10
            text globo[0] style "objeto_nombre_text"

    if botones:
        vbox:
            style "objeto_botones_vbox"
            for nombre, valor in botones:
                textbutton nombre:
                    style "objeto_boton"
                    text_style "objeto_boton_text"
                    action Return(valor)

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

style objeto_botones_vbox is vbox:
    xalign 0.97
    yalign 0.88
    spacing 14

style objeto_boton is button:
    xalign 1.0
    padding (22, 10)
    background "#111111aa"
    hover_background "#111111ee"

style objeto_boton_text is text:
    color "#d8d2c6"
    hover_color "#ffffff"
    size 28
