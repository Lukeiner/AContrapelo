# Definicion de los personajes #

define fran = Character ("Francisco")
define fran_int = Character("Francisco", what_prefix="- ")
define ma = Character ("María")
define doc = Character ("Doctor Malandra")
define cand = Character("Candidato")
define per = Character("Persona")
define vec = Character ("Vecinos")

# Posiciones para dos personajes en escena #

transform izq:
    xalign 0.15
    yalign 1.0

transform der:
    xalign 0.85
    yalign 1.0

# Sprites de Francisco #

image fran_normal = "images/Sprites/Francisco/Francisco_normal.png"
image fran_triste = "images/Sprites/Francisco/Francisco_bajon.png"
image fran_sorpresa = "images/Sprites/Francisco/Francisco_sorprendido.png"
image fran_enojo = "images/Sprites/Francisco/Francisco_serio.png"

# Sprites de Maria #

image mar_normal = "images/Sprites/Maria/Maria_normal.png"
image mar_preo = "images/Sprites/Maria/Maria_preocupada.png"
image mar_det = "images/Sprites/Maria/Maria_seria.png"
image mar_alivio = "images/Sprites/Maria/Maria_alivio.png"

# Sprites de Doctor Malandra #

image doc_normal = "images/Sprites/Malandra/malandra_normal.png"
image doc_mani = "images/Sprites/Malandra/malandra_maniaco.png"
image doc_shock = "images/Sprites/Malandra/malandra_sorprendido.png"
image doc_eno = "images/Sprites/Malandra/malandra_enojado.png"


# Backgrounds #

image hab_int = "images/Background/Habitacion_dia.jpg"
image hab_noche = "images/Background/Habitacion_noche.jpg"
image cocina = "images/Background/Cocina.jpg"
image comedor_dia = "images/Background/Comedor_dia.jpg"
image computadora = "images/Background/Computadora.jpg"
image calle = "images/Background/Calle.jpg"
image parada = "images/Background/Parada_micro.jpg"
image centro = "images/Background/Centro_Investigacion.jpg"
image sala = "images/Background/Clinica_Sala.jpg"
image consultorio = "images/Background/Clinica_consultorio.jpg"
image pizzeria = "images/Background/Pizzeria.jpg"
# Imagenes a pantalla completa #

image boceto = "images/Escenas/Boceto_local.jpg"
image mensaje_alquiler = "images/Escenas/Mensaje_alquiler.jpg"
image mensaje_viernes = "images/Escenas/Mensaje_viernes.jpg"
image mensaje_changa = "images/Escenas/Mensaje_changa.jpg"

# Viñetas del tratamiento: se muestran en un recuadro sobre el consultorio #

init python:
    def vineta(archivo):
        ancho, alto = 1240, 698
        return Composite(
            (ancho + 26, alto + 26),
            (0, 0), Solid("#111111", xysize=(ancho + 26, alto + 26)),
            (3, 3), Solid("#f4efe4", xysize=(ancho + 20, alto + 20)),
            (13, 13), Transform(archivo, xysize=(ancho, alto)),
        )

image vineta shampoo = vineta("images/Escenas/Tratamiento_shampoo.jpg")
image vineta secador = vineta("images/Escenas/Tratamiento_secador.jpg")
image vineta crema = vineta("images/Escenas/Tratamiento_crema.jpg")
image vineta medicion = vineta("images/Escenas/Tratamiento_medicion.jpg")

transform vineta_pos:
    xalign 0.5
    ypos 36
    yanchor 0.0

# Botones de la computadora (A1E3): resaltan sobre la pantalla blanca del monitor #

screen choice_pc(items):
    style_prefix "choice_pc"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_pc_vbox is vbox:
    xpos 977
    xanchor 0.5
    ypos 405
    yanchor 0.5
    spacing 30

style choice_pc_button is button:
    xsize 690
    padding (24, 20)
    background "#17324f"
    hover_background "#2f6aa8"

style choice_pc_button_text is button_text:
    xalign 0.5
    color "#ffffff"
    hover_color "#ffffff"


# Variables Booleanas

 #A1E2
default celular_visto = False
default boceto_visto = False

 #A1E3
default mozo_visto = False
default repartidor_visto = False
default ayudante_visto = False
