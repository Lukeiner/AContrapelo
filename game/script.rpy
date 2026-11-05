label start:

    #A1E0

    scene black
    play music tema_principal fadein 1.0
    show text "GRUPO PENTANILO PRESENTA" at truecenter with Dissolve(1.0)
    pause 5
    hide text with Dissolve(1.0)
    show text "A CONTRAPELO" at truecenter with Dissolve(1.0)
    pause 2
    hide text with Dissolve(1.0)


    #Acto 1 - Escena 1

    label acto1_escena1:

        stop music fadeout 1.0

        scene hab_int with dissolve

        play sound celular_vibra

        pause 1.0

        play music tema_casa fadein 2.0

        scene mensaje_alquiler with dissolve

        fran_int "¿Antes del viernes? Si apenas llego a mañana."

        scene hab_int
        show fran_triste
        with dissolve

        fran_int "¿Hasta cuándo voy a estar así?"
        fran_int "Necesito un laburo fijo, algo en serio."

    #Acto 1 - Escena 2

    label acto1_escena2:

        hide fran_triste
        show fran_normal at center
        with dissolve

        "Elegí un objeto para interactuar."

    label menu_habitacion:
        menu:
            "Ver el celular":
                $ celular_visto = True

                scene mensaje_alquiler with dissolve

                fran_int "Qué manera de ser molesto. ¿No me puede dejar un día tranquilo?"

                scene hab_int
                show fran_normal at center
                with dissolve

                jump menu_habitacion

            "Examinar el boceto":
                $ boceto_visto = True
                scene boceto with dissolve

                fran_int "Ojalá algún día se haga realidad. Solo necesito juntar para arrancar; lo demás viene solo."

                scene hab_int
                show fran_normal at center
                with dissolve

                jump menu_habitacion

            "Usar la computadora":
                jump submenu_computadora

    label submenu_computadora:
    fran_int "Tengo que ponerme a buscar laburo."

    menu:
        "¿Qué querés hacer frente a la computadora?"

        "Buscar trabajo":
            # Avanza hacia la escena A1E3 (Página 6)
            jump acto1_escena3

        "Todavía no":
            # Te regresa al bucle de exploración de la habitación
            jump menu_habitacion
    return

    #Acto 1 - Escena 3

    label acto1_escena3:

    fran_int "A ver si hay algo en gastronomía para arrancar tranqui."

    scene computadora with dissolve
    play sound mouse_tipeo

    label menu_trabajos:
        menu (screen="choice_pc"):
            "Buscar trabajo de mozo" if not mozo_visto:

                $ mozo_visto = True
                play sound mouse_tipeo

                "Requisito: dos años de experiencia."
                "Rechazado."

                show fran_normal with dissolve

                fran_int "Si nadie te contrata, ¿cómo vas a juntar experiencia?"

                hide fran_normal with dissolve

                jump menu_trabajos

            "Buscar trabajo de repartidor" if not repartidor_visto:

                $ repartidor_visto = True
                play sound mouse_tipeo

                "Requisito: moto propia."
                "Rechazado."

                show fran_normal with dissolve

                fran_int "Era obvio. Tampoco iba a repartir las pizzas corriendo."

                hide fran_normal with dissolve

                jump menu_trabajos

            "Buscar trabajo de ayudante de cocina" if not ayudante_visto:

                $ ayudante_visto = True
                play sound mouse_tipeo

                "Página saturada. Todas las postulaciones fueron rechazadas."

                show fran_normal with dissolve

                fran_int "Y eso que algo me había enseñado Hana."
                fran_int "Se ve que todos buscan laburo."

                hide fran_normal with dissolve

                jump menu_trabajos


        show fran_triste with dissolve

        fran_int "Por más que intente, nada."
        fran_int "Me voy a hacer unos mates."

    #Acto 1 - Escena 4
    label acto1_escena4:

        scene cocina with dissolve

        label menu_cocina:
            menu:
                "Heladera":
                    play sound heladera_puerta
                    play ambiente heladera_zumbido fadein 0.5
                    show vineta heladera at vineta_pos with dissolve
                    fran_int "Tremendo banquete."
                    stop ambiente fadeout 0.5
                    play sound heladera_puerta
                    hide vineta with dissolve

                    jump menu_cocina

                "Táper de María":
                    show fran_normal with dissolve
                    fran_int "Si anoche comí, fue gracias a María."
                    fran_int "Tengo que devolverle el táper."
                    hide fran_normal with dissolve
                    jump menu_cocina

                "Mate":
                    jump sub_menu_mate

        label sub_menu_mate:
            menu:
                "Preparar mate":
                    play sound pava_silbido
                    show vineta yerba at vineta_pos with dissolve
                    fran_int "Ya ni para la yerba me alcanza."
                    hide vineta
                    show fran_triste
                    with dissolve
                    fran_int "Si no fuera por María, me moría de hambre."

                    play sound golpes_puerta

                    hide fran_triste
                    show fran_normal
                    with dissolve

                    fran_int "¿Quién golpea?"

                    hide fran_normal with dissolve

                    jump acto1_escena5

                "Todavía no":
                        jump menu_cocina    

    #Acto 1 - Escena 5

    label acto1_escena5:

        scene comedor_dia with dissolve

        label menu_conocer:
            menu:
                "Impuestos":
                    show fran_normal with dissolve
                    fran_int "Luz, gas, internet... se me juntan todos."
                    hide fran_normal with dissolve
                    jump menu_conocer

                "Puerta de salida":
                    jump sub_menu_conocer

        label sub_menu_conocer:
            menu:
                "Atender la puerta":
                    play sound puerta_abre
                    show fran_normal at izq
                    show mar_alivio at der
                    with dissolve
                    ma "¡Hola, Fran! Vengo a buscar el táper."

                    fran "Hola Mari. Gracias por la cena, de verdad. ¿Pasás?"
                    fran "Hice unos mates."

                    hide mar_alivio
                    show mar_normal at der
                    with dissolve
                    ma "Dale. ¿Cómo andás con la búsqueda?"

                    hide fran_normal
                    show fran_triste at izq
                    with dissolve
                    fran "Mal. No sale nada y los impuestos se me apilan."
                    fran "¿Y vos en el laburo?"

                    hide mar_normal
                    show mar_preo at der
                    with dissolve
                    ma "No es lo que más me gusta, pero me alcanza para el tratamiento de mi papá."

                    hide mar_preo
                    show mar_alivio at der
                    with dissolve
                    ma "No te castigues tanto. Salí a dar una vuelta, despejate."
                    ma "Y te dejo torta para después."

                "Todavía no":
                    jump menu_conocer

        hide fran_triste
        hide mar_alivio
        show vineta taper at vineta_pos
        with dissolve

        pause 3.0

        play sound puerta_cierra

        hide vineta
        show fran_normal at izq
        with dissolve

        fran_int "Bueno, debería hacerle caso a Mari, después de terminarme el termo."

        play sound mate_sorbido

    label acto1_escena6:

        play music tema_barrio fadeout 1.0 fadein 1.0

        scene calle with dissolve

        show fran_triste with dissolve

        fran_int "Capaz pueda vender algo de ropa."
        fran_int "Ya no se me ocurre nada."

        play sound bocina_auto

        fran_int "¿Eh? ¿Qué hace tanta gente amontonada ahí?"

        hide fran_triste with dissolve

        scene parada_gente with dissolve

        pause 2.0

        scene parada_vacia with Dissolve(1.5)

        pause 1.0

        show fran_sorpresa with dissolve
        fran_int "Justo cuando necesito plata..."
        fran_int "Queda a unas cuadras."
        fran_int "Paso a ver."

    label acto1_escena7:

        play sound puerta_golpe
        scene candidato with dissolve
        with hpunch

        cand "¡Está loco ese tipo! Nadie va a aceptar hacerse eso."

        scene centro
        show fran_triste
        with dissolve

        fran_int "¿Tan mala será la oferta? Bueno, ya que estoy acá, entro a preguntar."

    label acto1_escena8:

        play music tema_clinica fadeout 1.0 fadein 1.0

        scene consultorio with dissolve

        show fran_normal at izq with dissolve

        fran "Buen día, vengo por el anuncio..."

        show doc_normal at der with dissolve

        doc "Qué bueno que llegaste. Completame esto."

        hide fran_normal
        hide doc_normal
        show vineta cuestionario at vineta_pos
        with dissolve

        menu (screen="choice_pc"):
            "¿Vivís solo?"
            "Sí, vivo solo":
                pass
            "Sí, hace rato":
                pass

        menu (screen="choice_pc"):
            "¿Alguien notaría si no te ve por un tiempo?"
            "Nadie lo notaría":
                pass
            "Casi nadie":
                pass

        menu (screen="choice_pc"):
            "Del 1 al 10, ¿cuánto te importa lo que piense la gente?"
            "1":
                pass
            "2":
                pass

        hide vineta
        show fran_normal at izq
        show doc_mani at der
        with dissolve

        doc "¡Perfecto! Sos la persona ideal."
        doc "Estoy desarrollando un producto para el crecimiento capilar."

        hide doc_mani
        show doc_normal at der
        with dissolve

        doc "Son tres aplicaciones y cobrás en cada una."
        doc "Por la primera, 6000 dólares."
        doc "Las condiciones a cumplir son que no te laves ni te cortes el pelo durante todo el tratamiento."
        doc "Y firmar un acuerdo de confidencialidad para no hablar del tema con nadie."

        hide doc_normal
        show doc_eno at der
        with dissolve

        doc "Si no cumplís, devolvés la plata o te embargo los bienes."
        doc "Así de fácil es la cosa."
        doc "¿Aceptás?"

        hide fran_normal
        show fran_triste at izq
        with dissolve

        fran_int "Ahora entiendo al que se fue corriendo."

        label menu_trato:
            menu:
                "Rechazar el trato":
                    jump acto1_escena9

                "Aceptar el trato":
                    jump acto1_escena12

    label acto1_escena9:

        hide fran_triste
        show fran_normal at izq
        with dissolve

        fran "Es demasiado para mí."
        fran "Mejor lo dejamos acá."

        doc "Te estás perdiendo una oportunidad única en la vida."

        stop music fadeout 2.0

        hide fran_normal
        hide doc_eno
        with dissolve

    label acto1_escena10:
        scene hab_noche with dissolve


        show fran_triste with dissolve

        fran_int "¿Hice bien? Con esa plata pagaba todo..."
        fran_int "y hasta capaz invitaba a María a comer algo."

        play sound celular_vibra
        scene mensaje_viernes with dissolve

        fran_int "Otra vez. No se cansa."

        scene black with fade

        "Al día siguiente"

    label acto1_escena11:

        scene hab_int with dissolve

        play sound celular_vibra

        pause 1.0

        scene mensaje_changa with dissolve

        fran_int "Y bueno."
        fran_int "Si no queda otra."

        scene mensaje_respuesta with dissolve

        pause 3.0

        scene hab_int
        show fran_triste
        with dissolve

        "FINAL NORMAL — TODO SIGUE IGUAL"
        "FIN"

        label menu_normal:
            menu:
                "Volver a la última decisión":
                    play music tema_clinica fadein 1.0
                    scene consultorio
                    show fran_triste at izq
                    show doc_eno at der
                    with dissolve
                    jump menu_trato


                "Salir al menú":
                    return

    label acto1_escena12:

        hide fran_triste
        hide doc_eno
        show vineta firma at vineta_pos
        with dissolve

        pause 3.0

        hide vineta
        show fran_normal at izq
        show doc_mani at der
        with dissolve

        doc "¡Perfecto!"
        doc "Primero, lavate la cabeza con esto."
        doc "No desperdicies ni una gota."

        hide fran_normal
        hide doc_mani
        show vineta shampoo at vineta_pos
        with dissolve

        fran_int "Shampoo de manzana... qué científicamente avanzado."

        play ambiente secadora fadein 0.3
        show vineta secador at vineta_pos with dissolve

        doc "Mirá, al oxidarse, el péptido reacciona con la queratina del folículo..."
        doc "...lo que acelera la mitosis capilar en un cuatrocientos por ciento, según mis cálculos..."
        fran_int "Con tanta palabrería y el secador no escuché nada."

        stop ambiente fadeout 0.5

        hide vineta
        show fran_normal at izq
        show doc_mani at der
        with dissolve

        doc "Ahora la crema. Solo se aplica acá, en ambiente estéril."

        play sound crema_squish

        hide fran_normal
        hide doc_mani
        show vineta crema at vineta_pos
        with dissolve

        doc "¿Te pica?"
        doc "¿Sentís algo raro?"

        fran "Nada."
        fran "¿Debería?"

        hide vineta
        show fran_normal at izq
        show doc_normal at der
        with dissolve

        doc "No, no. Dejame anotar algunas cosas primero."

        hide fran_normal
        hide doc_normal
        show vineta medicion at vineta_pos
        with dissolve

        pause 3.0

        doc "Ok, todo listo. Acá tenés tu primera paga."

        play sound cajon_abre
        show vineta sobre at vineta_pos with dissolve

        "Recibiste USD 6000"

        hide vineta
        show fran_sorpresa at izq
        show doc_normal at der
        with dissolve

        fran "¿Todo esto es para mí?"

        doc "Sí, todo tuyo. Nos vemos en una semana."
        doc "Y acordate: nada de agua ni tijeras."
        doc "Y ni una palabra a nadie."

        hide fran_sorpresa
        show fran_normal at izq
        with dissolve

        fran "Sí, sí… entendido."

        fran_int "Con esto pago todo y me sobra."
        fran_int "Mejor vuelvo en colectivo."

    #Acto 2

    label acto2_escena13:

        scene black with fade

        play music tema_barrio fadeout 1.0 fadein 1.0

        scene parada
        show fran_normal
        with dissolve

        fran "Disculpá, ¿pasó hace mucho el 45?"

        per "Ya debe estar por venir."
        per "Che, qué pelo brilloso tenés."
        per "¿Qué te ponés?"

        hide fran_normal
        show fran_sorpresa
        with dissolve

        fran "¿Mi pelo? Shampoo de manzana."

        hide fran_sorpresa
        show fran_normal
        with dissolve

        fran_int "Si supiera…"
        fran_int "Antes de volver paso por el súper. Esa heladera necesita algo más que un limón."

        scene black with fade

    label acto2_escena14:

        play music tema_casa fadeout 1.0 fadein 1.0

        scene comedor_apagado
        show fran_normal
        with dissolve

        pause 1.0

        scene comedor_noche
        show fran_normal
        with dissolve

        fran_int "Qué lindo es poder comprar comida."

        play sound heladera_puerta

        hide fran_normal
        show vineta heladera_llena at vineta_pos
        with dissolve

        fran_int "La heladera se va a asustar."

        scene black with fade

        "Al día siguiente"

    label acto2_escena15:

        scene hab_ordenada
        show fran_largo_normal at lado_der
        with fade

        fran_int "Hace rato no dormía tan bien."
        fran_int "Hasta me dieron ganas de ordenar la cama."

    label menu_habitacion_2:
        menu:
            "Ver el celular":

                scene mensaje_comprobante with dissolve

                fran_int "Uno diría que se pondría contento porque le pagué."

                scene hab_ordenada
                show fran_largo_normal at lado_der
                with dissolve

                jump menu_habitacion_2

            "Examinar el boceto":

                scene boceto with dissolve

                "Meta para el local: USD 4000 / USD 30000"

                fran_int "Tuve que gastar bastante para ponerme al día, pero el resto lo guardo para el local."
                fran_int "Por fin este sueño no parece tan lejano."

                scene hab_ordenada
                show fran_largo_normal at lado_der
                with dissolve

                jump menu_habitacion_2

            "Puerta al comedor":
                menu:
                    "Ir al comedor":
                        jump acto2_escena16

                    "Todavía no":
                        jump menu_habitacion_2

    label acto2_escena16:

        scene comedor_pagadas
        show fran_largo_normal
        with dissolve

        fran_int "¿Y ahora qué hago con tanto tiempo libre?"
        fran_int "Tendría que aprovechar el día y salir a pasear un rato."

    label menu_escena16:
        menu:
            "Impuestos pagados":
                fran_int "Todos pagados. Qué lindo es no preocuparse."

                jump menu_escena16

            "Puerta de salida":
                menu:
                    "Salir a pasear":
                        jump acto2_escena17

                    "Todavía no":
                        jump menu_escena16

    label acto2_escena17:

        scene black with fade

        play music tema_barrio fadeout 1.0 fadein 1.0

        scene calle
        show fran_largo_normal
        with fade

        pause 2.0

        fran_int "No lavarse ni cortarse el pelo..."
        fran_int "¿Y el cuerpo?"
        fran_int "Mejor no arriesgarme."

        scene black with fade

        scene calle
        show fran_largo_normal
        with fade

        fran_int "Tendría que invitar a María a cenar algo. Le tengo que devolver como mil tápers."
        fran_int "Pero ¿qué podríamos cenar?"
        fran_int "¿Sushi, como el que me hacía Hana de chico? ¿O una buena pizza, que no falla nunca?"

    label menu_comida:
        menu:
            "Sushi":
                $ cena_sushi = True
                jump acto2_escena18

            "Pizza":
                $ cena_sushi = False
                jump acto2_escena26

    #Ruta sushi

    label acto2_escena18:

        scene mensaje_sushi1 with dissolve

        pause

        scene mensaje_sushi2 with dissolve

        pause

        scene mensaje_pedido with dissolve

        fran_int "¡Bien! Vuelvo a casa así ordeno un poco."

    label acto2_escena19:

        scene black with fade

        play music tema_casa fadeout 1.0 fadein 1.0 volume 0.6
        play sound golpes_puerta
        queue sound puerta_abre

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "¡Hola, Fran! ¿Cómo andás?"

        fran "¡Hola, Mari! Bien, pasá. Ya llegó el pedido."

        ma "Traje agua con gas."

        scene comedor_sushi
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "Se ve rico… ¿probás vos primero?"

    label menu_cena:
        menu:
            "Pedirle ayuda a María":
                jump acto2_escena20

            "Ir a buscar un tenedor":
                jump acto2_escena21

    label acto2_escena20:

        fran "Hasta partir los palitos me acuerdo. Después, ni idea."

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "El de abajo queda fijo; el de arriba aprieta."
        ma "Y antes de comer se dice \"itadakimasu\"."

        hide fran_largo_normal
        hide mar_alivio
        show vineta rezo at vineta_pos
        with dissolve

        pause 3.0

        hide vineta
        show fran_largo_normal at izq
        show mar_alivio at der
        with dissolve

        fran "Hana siempre me lo decía."
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico."

        jump acto2_escena22

    label acto2_escena21:

        play sound cajon_abre

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¡Jaja! ¡Comer esta obra de arte con tenedor es una falta de respeto!"

        fran "Tenés razón. Si Hana me viera..."
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico."

        ma "Con más razón. Agarrá el palillo, dale."
        ma "El de abajo fijo, el de arriba aprieta."
        ma "Y antes de comer se dice \"itadakimasu\"."

        hide fran_largo_normal
        hide mar_alivio
        show vineta rezo at vineta_pos
        with dissolve

        pause 3.0

    label acto2_escena22:

        hide fran_largo_normal
        hide mar_alivio
        show vineta jengibre at vineta_pos
        with dissolve

        pause 3.0

        hide vineta
        show fran_largo_normal at izq
        show mar_det at der
        with dissolve

        ma "¡Pará! El jengibre va entre pieza y pieza, para limpiar el gusto."
        ma "Y este arroz está frío, tiene que estar tibio y con vinagre."

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

        fran_int "¿Desde cuándo María sabe tanto de esto?"

    label menu_pregunta_sushi:
        menu:
            "¿Cómo sabés tanto?":
                jump acto2_escena23

            "¿Por qué no lo hacés vos?":
                jump acto2_escena24

    label acto2_escena23:

        hide mar_det
        show mar_alivio at der
        with dissolve

        ma "Hice un curso de cocina japonesa."
        ma "Mi sueño era ser itamae, chef de sushi, y tener mi barra."

        hide mar_alivio
        show mar_preo at der
        with dissolve

        ma "Después se enfermó mi papá y lo tuve que dejar."

        hide fran_largo_sorpresa
        show fran_largo_triste at izq
        with dissolve

        fran_int "Y yo quejándome todo el día."

        jump acto2_escena25

    label acto2_escena24:

        hide mar_det
        show mar_normal at der
        with dissolve

        ma "Estudié para ser itamae, chef de sushi, pero comprar diferentes ingredientes para hacer una buena variedad de piezas es muy caro."
        ma "No me dan los números."

        hide fran_largo_sorpresa
        show fran_largo_normal at izq
        with dissolve

        fran "Como yo con el local."

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "Estamos los dos en la misma, Fran."

    label acto2_escena25:

        scene comedor_sushi
        show fran_largo_normal at izq
        show mar_alivio at der
        with dissolve

        fran "Te propongo algo: cuando tenga mi local, la chef sos vos."

        ma "Mirá que los itamae no son baratos, eh."

        fran_int "Lo dije en joda… pero capaz no tanto."

        jump acto2_escena34

    #Ruta pizza

    label acto2_escena26:

        scene mensaje_pizza1 with dissolve

        pause

        scene mensaje_pizza2 with dissolve

        fran_int "Una buena muzza nunca falla."
        fran_int "Vuelvo a casa así ordeno un poco."

    label acto2_escena27:

        scene black with fade

        play music tema_casa fadeout 1.0 fadein 1.0 volume 0.6

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "¡Hola, Fran! Traje la gaseosa, como te prometí."

        fran "¡Hola, Mari! Pasá, ponete cómoda."

        ma "Qué raro verte tan contento. Hacía rato que no te veía así."

        fran "Se me están acomodando un poco las cosas."

        ma "Che, ¿te hiciste algo en el pelo?"

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

        fran_int "No puedo decirle nada. Tengo que mentirle."

    label menu_pelo_pizza:
        menu:
            "Me lo estoy dejando crecer, quería probar algo distinto":
                jump acto2_escena28

            "No tuve tiempo de ir a la peluquería":
                jump acto2_escena29

    label acto2_escena28:

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¿Vos, algo distinto? Si usás la misma campera desde que te conozco."
        ma "Igual te queda bien."

        jump acto2_escena30

    label acto2_escena29:

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "Si querés te lo corto yo. Hice un curso de peluquería, algo me acuerdo."

        fran "¡No! Digo… no, gracias. Otro día."

    label acto2_escena30:

        scene comedor_pizza
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "¿Y a qué se debe este manjar culinario?"

        fran "Estoy juntando para abrir mi local de comida."

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¡Qué bueno, Fran! ¿Pudiste conseguir un trabajo por fin?"

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

        fran_int "\"Ni una palabra a nadie\". No le puedo contar."

    label menu_plata_pizza:
        menu:
            "Mentir":
                jump acto2_escena31

            "Esquivar con un chiste":
                jump acto2_escena32

    label acto2_escena31:

        hide fran_largo_sorpresa
        show fran_largo_normal at izq
        with dissolve

        fran "Me salió una changa: pintar una casa entera."

        hide mar_alivio
        show mar_normal at der
        with dissolve

        ma "¿Vos pintando? No te imagino."

        jump acto2_escena33

    label acto2_escena32:

        hide fran_largo_sorpresa
        show fran_largo_normal at izq
        with dissolve

        fran "Robé un banco. Shh, no le digas a nadie."

        ma "Ay, tarado. Bueno, no me cuentes."

    label acto2_escena33:

        scene comedor_pizza
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        fran "¿Y a vos cómo te va en la vida?"

        ma "En el laburo, como siempre. Mucho trabajo y poca plata."
        ma "Pero alcanza para lo de mi papá así que estamos bien."

        hide fran_largo_normal
        hide mar_normal
        show vineta charla_pizza at vineta_pos
        with dissolve

        pause 3.0

    #Rutas juntas

    label acto2_escena34:

        scene black with fade

        "Terminaron de comer y María se fue a su casa."

        scene hab_ordenada_noche
        show fran_largo_normal at lado_der
        with dissolve

        fran_int "Hacía mucho que no la pasaba tan bien."
        fran_int "¿Qué tan difícil puede ser aguantar un tiempo sin bañarse? La paga es muy buena."

        stop music fadeout 2.0

        scene black with fade

        "6 días después"

        scene hab_int
        show vineta rascarse at vineta_pos
        with fade

        pause 3.0

        hide vineta
        show fran_semana_triste
        with dissolve

        fran_int "No aguanto esta picazón. Al final es más difícil de lo que creía."
        fran_int "Bueno, a la clínica. ¿Cómo voy?"

    label menu_ida_clinica:
        menu:
            "En remís":
                jump acto2_escena35

            "En colectivo":
                jump acto2_escena36

    label acto2_escena35:

        scene black with fade

        # Provisorio: no hay sonido de auto, se usa el del colectivo que pasa
        play sound auto_movimiento

        pause 2.0

        scene remis_aromatizante with dissolve

        rem "Uf… ¿no sentís olor a algo?"

        fran "Debe venir de afuera."

        fran_int "La verdad es que es mío. Ni yo me aguanto."

        jump acto2_escena37

    label acto2_escena36:

        scene black with fade

        scene parada
        show fran_semana_triste
        with fade

        pas "¿Sentiste el olor?"

        fran_int "¿Lo dicen por mí?"

        scene black with fade

        "Francisco se tomó el colectivo y llegó a la clínica."

    label acto2_escena37:

        play music tema_clinica fadein 1.0

        scene consultorio
        show vineta medicion at vineta_pos
        with dissolve

        pause 2.0

        hide vineta
        show fran_semana_normal at izq
        show doc_mani at der
        with dissolve

        doc "¡Siete centímetros en siete días! ¿Picazón? ¿Olor? ¿Sueños raros?"

        fran "Todo eso, sí."

        play sound crema_squish

        hide fran_semana_normal
        hide doc_mani
        show vineta crema at vineta_pos
        with dissolve

        pause 2.0

        hide vineta
        show fran_semana_normal at izq
        show doc_normal at der
        with dissolve

        fran "Doctor, ¿y cómo sabe que no me mojé el pelo?"

        hide doc_normal
        show doc_mani at der
        with dissolve

        doc "El producto reacciona violentamente al contacto con el agua y con cualquier objeto afilado."
        doc "Te lo expliqué mientras te secaba el pelo."

        hide doc_mani
        show doc_normal at der
        with dissolve

        doc "Las condiciones siguen igual. Y la última paga es mucho mayor."

        hide fran_semana_normal
        show fran_semana_triste at izq
        with dissolve

        fran "Doctor, ¿no hay algo para la picazón? Aunque sea un perfume, porque la gente…"

        hide doc_normal
        show doc_shock at der
        with dissolve

        doc "¿Perfume? ¿Querés arruinar meses de trabajo? ¡Nada de nada!"
        doc "Tomá tu plata y andate, que me apestás el consultorio."

        hide fran_semana_triste
        hide doc_shock
        play sound cajon_abre
        show vineta sobre at vineta_pos
        with dissolve

        "Recibiste USD 11000"

        stop music fadeout 1.5

        scene black with fade

        scene centro
        show fran_semana_triste
        with fade

        fran_int "Me pica más que nunca. ¿Cómo vuelvo?"

    label menu_vuelta_clinica:
        menu:
            "En colectivo":
                jump acto2_escena38

            "En remís":
                jump acto2_escena39

    label acto2_escena38:

        scene black with fade

        scene parada
        show fran_semana_triste
        with fade

    label menu_garita:
        menu:
            "Personas":
                fran "Disculpá, ¿pasó el 45?"

                per "No sé, no sé. Alejate, por favor."

                jump menu_garita

            "Asiento de la garita":
                scene black with fade

                scene parada
                show fran_semana_triste
                with fade

                col "No, no. Así no subís, recién limpiamos."

                jump acto2_escena40

    label acto2_escena39:

        per "¡Qué asco, bañate!"

        rem "No, maestro. Tengo el auto recién tapizado."

    label acto2_escena40:

        scene calle
        show fran_semana_triste
        with dissolve

        fran_int "Bueno. Caminando, entonces."

        hide fran_semana_triste
        show fran_cintura
        with Dissolve(1.2)

        hide fran_cintura
        show fran_muy_sorpresa
        with Dissolve(1.2)

        fran_int "¿Qué…? ¡¿Qué me está pasando?!"

        ado "¡Miralo! ¡Parece un yeti! ¡Grabalo!"

        fran_int "¡Oh, no! Esto me va a traer problemas."
        fran_int "¡Tengo que volver a casa!"

        scene black with fade

        play sound puerta_cierra

    label acto2_escena41:

        scene comedor_pagadas
        show fran_muy_triste
        with dissolve

    label menu_comedor_encierro:
        menu:
            "Puerta de salida":
                fran_int "Ni loco salgo así."

                jump menu_comedor_encierro

            "Puerta a la habitación":
                jump acto2_escena42

            "Puerta al baño":
                jump acto2_escena43

    label acto2_escena42:

        scene hab_int
        show fran_muy_normal
        with dissolve

    label menu_habitacion_encierro:
        menu:
            "Boceto":
                scene boceto with dissolve

                "Meta para el local: USD 15000 / USD 30000"

                fran_int "Por esto lo hago. Ya junté 15000 dólares y me faltan otros 15000."

                scene hab_int
                show fran_muy_normal
                with dissolve

                jump menu_habitacion_encierro

            "Computadora":
                scene video_yeti with dissolve

                pause

                fran_int "¿Ese soy yo?"

                scene hab_int
                show fran_muy_normal
                with dissolve

                jump menu_habitacion_encierro

            "Puerta al comedor":
                jump acto2_escena41

    label acto2_escena43:

        scene bano
        show fran_muy_triste at lado_der
        with dissolve

    label menu_bano:
        menu:
            "Espejo":
                fran_int "Ni yo me reconozco. Y el olor… y la picazón."

                jump menu_bano

            "Máquina de cortar pelo":
                fran_int "Dos minutos y se termina todo. Vuelvo a ser yo…"

                play sound golpes_puerta

                jump acto2_escena44

            "Puerta al comedor":
                jump acto2_escena41

    label acto2_escena44:

        scene mensaje_maria_puerta with dissolve

        pause

        play sound puerta_abre

        scene comedor_pagadas
        show fran_muy_triste at izq_pelo
        show mar_preo at der
        with dissolve

        ma "¡Vi un monstruo entrando a tu departamento, pero te reconocí por la campera!"
        ma "¿Qué te pasó? Vení, dejame que te ayude a cortar ese pelo."

        ma "¿Tenés una máquina de cortar o unas tijeras por acá?"

        fran_int "No le puedo contar nada. Si le cuento, rompo el trato."

    label menu_decision9:

        $ vuelta_final_malo = "menu_decision9"

        scene comedor_pagadas
        show fran_muy_triste at izq_pelo
        show mar_preo at der
        with dissolve

        menu:
            "Aceptar la ayuda":
                jump acto2_escena45

            "No decir nada y cerrarle la puerta":
                play sound puerta_cierra

                # Provisorio hasta que exista A3E46
                scene black with fade

                "Continúa en el Acto 3."

                return

    label acto2_escena45:

        play sound maquina_cortar

        ma "Quedate quieto, es un segundo."

        hide fran_muy_triste
        show fran_monstruo_sorpresa at izq_pelo
        with Dissolve(0.5)

        show pelo_pantalla with Dissolve(1.5)

        ma "¡Fran! ¡Fran, contestame!"

        stop sound fadeout 1.0
        scene black with fade

    # A3E50 tiene que entrar por aca: el guion retoma desde el mensaje del abogado
    label final_malo_mensaje:

        scene mensaje_abogado with dissolve

        pause

        scene black with dissolve

        "FINAL MALO — EL YETI BONAERENSE"
        "FIN"

    label menu_final_malo:
        menu:
            "Volver a la última decisión":
                jump expression vuelta_final_malo

            "Salir al menú":
                return
