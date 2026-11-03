# Definicion de los personajes #

define fran = Character ("Francisco")
define fran_int = Character("Francisco", what_prefix="(", what_suffix=")")
define ma = Character ("María")
define doc = Character ("Doctor Malandra")
define cand = Character("Candidato")

# Sprites de Francisco #

image fran_normal = "images/Sprites/Francisco/Francisco_normal.png"
image fran_triste = "images/Sprites/Francisco/Francisco_triste.png"
image fran_sorpresa = "images/Sprites/Francisco/Francisco_sorpresa.png"
image fran_enojo = "images/Sprites/Francisco/Francisco_enojo.png"

# Sprites de Maria #

image mar_normal = "images/Sprites/Maria/Maria_normal.png"
# TEMPORAL: mar_preo y mar_alivio usan el sprite neutral hasta tener los completos (A-11).
image mar_preo = "images/Sprites/Maria/Maria_normal.png"
image mar_det = "images/Sprites/Maria/Maria_determinada.png"
image mar_alivio = "images/Sprites/Maria/Maria_normal.png"

# Sprites de Doctor Malandra #

# TEMPORAL: doc_mani y doc_eno usan el sprite neutral hasta tener los completos (A-11).
image doc_normal = "images/Sprites/Malandra/Doctor_Normal.png"
image doc_mani = "images/Sprites/Malandra/Doctor_Normal.png"
image doc_shock = "images/Sprites/Malandra/Doctor_shock.png"
image doc_eno = "images/Sprites/Malandra/Doctor_Normal.png"


# Backgrounds #

image hab_int = "images/Background/Habitacion_interior.jpg"
image cocina = "images/Background/Cocina.jpg"
image calle = "images/Background/Calle.jpg"
image centro = "images/Background/Centro_Investigacion.jpg"
image sala = "images/Background/Clinica_Sala.jpg"
image consultorio = "images/Background/Clinica_consultorio.jpg"



# Variables Booleanas

 #A1E2
default celular_visto = False
default boceto_visto = False

 #A1E3
default mozo_visto = False
default repartidor_visto = False
default ayudante_visto = False
