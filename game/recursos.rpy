# Definicion de los personajes #

define fran = Character ("Francisco")
define fran_int = Character("Francisco", what_prefix="- ")
define ma = Character ("María")
define doc = Character ("Doctor Malandra")
define cand = Character("Candidato")
define per = Character("Persona")
define vec = Character ("Vecino")
define rem = Character("Remisero")
define pas = Character("Pasajera")
define col = Character("Colectivero")
define ado = Character("Adolescentes")

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

# Pelo largo: desde la primera dosis #

image fran_largo_normal = "images/Sprites/Francisco/Francisco_pelo_normal.png"
image fran_largo_triste = "images/Sprites/Francisco/Francisco_pelo_bajon.png"
image fran_largo_sorpresa = "images/Sprites/Francisco/Francisco_pelo_sorprendido.png"
image fran_largo_enojo = "images/Sprites/Francisco/Francisco_pelo_serio.png"

# Pelo muy largo: provisorio con el pelo normal hasta tener el sprite (AR2-02) #

image fran_muy_normal = "images/Sprites/Francisco/Francisco_normal.png"
image fran_muy_triste = "images/Sprites/Francisco/Francisco_bajon.png"
image fran_muy_sorpresa = "images/Sprites/Francisco/Francisco_sorprendido.png"

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
image comedor_noche = "images/Background/Comedor_noche.jpg"
image bano = "images/Background/Bano.jpg"
image computadora = "images/Background/Computadora.jpg"
image calle = "images/Background/Calle.jpg"
image calle_atardecer = Transform("images/Background/Calle.jpg", matrixcolor=TintMatrix("#ffbe8c"))
image parada = "images/Background/Parada_micro.jpg"
image parada_gente = "images/Background/Parada_gente.jpg"
image parada_vacia = "images/Background/Parada_vacia.jpg"
image centro = "images/Background/Centro_Investigacion.jpg"
image candidato = "images/Background/Candidato.jpg"
image sala = "images/Background/Clinica_Sala.jpg"
image consultorio = "images/Background/Clinica_consultorio.jpg"
image pizzeria = "images/Background/Pizzeria.jpg"

# Imagenes a pantalla completa #

image boceto = "images/Escenas/Boceto_local.jpg"
image mensaje_alquiler = "images/Escenas/Mensaje_alquiler.jpg"
image mensaje_viernes = "images/Escenas/Mensaje_viernes.jpg"
image mensaje_changa = "images/Escenas/Mensaje_changa.jpg"
image mensaje_comprobante = "images/Escenas/Mensaje_comprobante.jpg"
image mensaje_respuesta = "images/Escenas/Mensaje_respuesta.jpg"

# Provisorio hasta tener la imagen del pelo (AR2-10) #

image pelo_pantalla = Solid("#1c120b")

# Viñetas de acciones: se muestran en un recuadro sobre el fondo #

init python:
    def vineta(archivo):
        ancho, alto = 1240, 698
        return Composite(
            (ancho + 26, alto + 26),
            (0, 0), Solid("#111111", xysize=(ancho + 26, alto + 26)),
            (3, 3), Solid("#f4efe4", xysize=(ancho + 20, alto + 20)),
            (13, 13), Transform(archivo, xysize=(ancho, alto)),
        )

image vineta heladera = vineta("images/Escenas/Heladera.jpg")
image vineta yerba = vineta("images/Escenas/Yerba.jpg")
image vineta taper = vineta("images/Escenas/Taper.jpg")
image vineta cuestionario = vineta("images/Escenas/Cuestionario.jpg")
image vineta firma = vineta("images/Escenas/Firma.jpg")
image vineta sobre = vineta("images/Escenas/Sobre.jpg")
image vineta shampoo = vineta("images/Escenas/Tratamiento_shampoo.jpg")
image vineta secador = vineta("images/Escenas/Tratamiento_secador.jpg")
image vineta crema = vineta("images/Escenas/Tratamiento_crema.jpg")
image vineta medicion = vineta("images/Escenas/Tratamiento_medicion.jpg")

transform vineta_pos:
    xalign 0.5
    ypos 36
    yanchor 0.0

# Botones que resaltan sobre una imagen: computadora (A1E3) y cuestionario (A1E8) #

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


# Audio #

init python:
    renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

define audio.tema_barrio = "audio/musica/tema_barrio.ogg"
define audio.tema_casa = "audio/musica/tema_casa.ogg"
define audio.tema_clinica = "audio/musica/tema_clinica.ogg"
define audio.tema_principal = "audio/musica/tema_principal.ogg"

define audio.bocina_auto = "audio/sfx/bocina_auto.ogg"
define audio.cajon_abre = "audio/sfx/cajon_abre.ogg"
define audio.celular_vibra = "audio/sfx/celular_vibra.ogg"
define audio.crema_squish = "audio/sfx/crema_squish.ogg"
define audio.golpes_puerta = "audio/sfx/golpes_puerta.ogg"
define audio.heladera_puerta = "audio/sfx/heladera_puerta.ogg"
define audio.heladera_zumbido = "audio/sfx/heladera_zumbido.ogg"
define audio.mate_sorbido = "audio/sfx/mate_sorbido.ogg"
define audio.mouse_tipeo = "audio/sfx/mouse_tipeo.ogg"
define audio.pava_silbido = "audio/sfx/pava_silbido.ogg"
define audio.puerta_abre = "audio/sfx/puerta_abre.ogg"
define audio.puerta_cierra = "audio/sfx/puerta_cierra.ogg"
define audio.puerta_golpe = "audio/sfx/puerta_golpe.ogg"
define audio.secadora = "audio/sfx/secadora.ogg"


# Variables Booleanas

 #A1E2
default celular_visto = False
default boceto_visto = False

 #A2E17: el final del Acto 3 depende de esta eleccion
default cena_sushi = False

 #A2E45: a que decision vuelve el final malo
default vuelta_final_malo = "menu_decision9"

 #A1E3
default mozo_visto = False
default repartidor_visto = False
default ayudante_visto = False
