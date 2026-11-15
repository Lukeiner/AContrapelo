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

    show expression credito("{size=+20}ACTO 1{/size}") as cartel at truecenter with Dissolve(1.0)
    pause 2
    hide cartel with Dissolve(1.0)

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

        fran_int "Necesito un laburo fijo, ya basta de andar de changa en changa."

    #Acto 1 - Escena 2

    label acto1_escena2:

        hide fran_triste
        show fran_normal at center
        with dissolve

    label menu_habitacion:
        call screen objetos_escena(objetos_habitacion)

        if _return == "celular":
            $ celular_visto = True

            scene mensaje_alquiler with dissolve

            fran_int "Qué manera de joder. ¿No me puede dejar un día tranquilo?"

            scene hab_int
            show fran_normal at center
            with dissolve

            jump menu_habitacion

        elif _return == "boceto":
            $ boceto_visto = True
            scene boceto with dissolve

            fran_int "Algún día..."

            scene hab_int
            show fran_normal at center
            with dissolve

            jump menu_habitacion

        else:
            jump submenu_computadora

    label submenu_computadora:

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

    scene computadora with dissolve
    play sound mouse_tipeo

    label menu_trabajos:
        menu (screen="choice_pc"):
            "Buscar trabajo de mozo" if not mozo_visto:

                $ mozo_visto = True
                play sound mouse_tipeo

                "Requisito: dos años de experiencia en atención al público."
                "Su CV no muestra experiencia corroborable. Rechazado."

                fran_int "Si nadie te contrata, ¿cómo vas a juntar experiencia?"

                jump menu_trabajos

            "Buscar trabajo de repartidor" if not repartidor_visto:

                $ repartidor_visto = True
                play sound mouse_tipeo

                "Requisito: poseer vehículo propio y licencia de conducir."
                "No se encontró ningún vehículo a su nombre. Rechazado."

                fran_int "Y sí... Tampoco iba a repartir las pizzas corriendo."

                jump menu_trabajos

            "Buscar trabajo de ayudante de cocina" if not ayudante_visto:

                $ ayudante_visto = True
                play sound mouse_tipeo

                "Página saturada. Intente de nuevo más tarde."

                fran_int "Fua, ¿tanta gente anda buscando laburo?"

                jump menu_trabajos

        fran_int "Otra vez no hubo suerte. Tocará hacerse unos mates."

    #Acto 1 - Escena 4
    label acto1_escena4:

        scene cocina with dissolve

        label menu_cocina:
            call screen objetos_escena(objetos_cocina)

            if _return == "heladera":
                play sound heladera_puerta
                play ambiente heladera_zumbido fadein 0.5
                show vineta heladera at vineta_pos with dissolve
                fran_int "Tremendo banquete."
                stop ambiente fadeout 0.5
                play sound heladera_puerta
                hide vineta with dissolve

                jump menu_cocina

            elif _return == "taper":
                show fran_normal with dissolve
                fran_int "Si anoche comí, fue gracias a María."
                hide fran_normal with dissolve
                jump menu_cocina

            elif _return == "mate":
                jump sub_menu_mate

        label sub_menu_mate:
            menu:
                "Preparar mate":
                    play sound pava_silbido
                    show vineta yerba at vineta_pos with dissolve
                    fran_int "Uff, me alcanza para una última tanda nomás."
                    hide vineta
                    show fran_triste
                    with dissolve

                    play sound golpes_puerta

                    hide fran_triste
                    show fran_normal
                    with dissolve

                    hide fran_normal with dissolve

                    jump acto1_escena5

                "Todavía no":
                        jump menu_cocina    

    #Acto 1 - Escena 5

    label acto1_escena5:

        scene comedor_dia with dissolve

        label menu_conocer:
            call screen objetos_escena(objetos_comedor_acto1)

            if _return == "impuestos":
                show fran_normal with dissolve
                fran_int "Luz, gas, internet... no sé cómo voy a hacer para pagar todo esto."
                hide fran_normal with dissolve
                jump menu_conocer

            elif _return == "puerta":
                jump sub_menu_conocer

        label sub_menu_conocer:
            menu:
                "Atender la puerta":
                    play sound puerta_abre
                    show fran_normal at izq
                    show mar_alivio at der
                    with dissolve
                    ma "¡Buenos días, Fran!"

                    fran "¡Buenas, Mari!"
                    fran "Justo terminé de preparar unos mates. ¿Querés?"

                    hide mar_alivio
                    show mar_normal at der
                    with dissolve
                    ma "¡Ay, qué rico! Pero no puedo, mi turno arranca dentro de un rato. ¿Vos cómo venís con ese tema?"

                    hide fran_normal
                    show fran_triste at izq
                    with dissolve
                    fran "Mal. Todos los días lo mismo, que no tengo experiencia o siempre pasa algo."
                    fran "¿Y a vos cómo te va con esa panchería?"

                    hide mar_normal
                    show mar_preo at der
                    with dissolve
                    ma "No es lo que más me gusta, pero me alcanza para el tratamiento de mi papá."

                    hide mar_preo
                    show mar_alivio at der
                    with dissolve
                    ma "No te castigues tanto. Salí a dar una vuelta, despejate."
                    ma "¡Ah! Casi se me olvida, pasame el táper que te dejo una torta que cociné hoy temprano. ¡Nos vemos, Fran!"

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

        play sound mate_sorbido

    label acto1_escena6:

        play music tema_barrio fadeout 1.0 fadein 1.0

        scene calle with dissolve

        show fran_triste with dissolve

        fran_int "Capaz pueda vender algunas cosas..."

        play sound bocina_auto

        hide fran_triste with dissolve

        scene parada_gente with dissolve

        pause 2.0

        scene parada_vacia with Dissolve(1.5)

        pause 1.0

        show fran_sorpresa with dissolve
        fran_int "Justo cuando necesito plata..."

    label acto1_escena7:

        play sound puerta_golpe
        scene candidato with dissolve
        with hpunch

        cand "¡Pero ese tipo está loco! Nadie va a aceptar hacerse eso."

        scene centro
        show fran_triste
        with dissolve

        fran_int "¿Tan mala será la oferta?"

    label acto1_escena8:

        play music tema_clinica fadeout 1.0 fadein 1.0

        scene consultorio with dissolve

        show fran_normal at izq with dissolve

        fran "Buen día, vengo por el anuncio..."

        show doc_normal at der with dissolve

        doc "¡Ah! ¿Otro candidato? Qué bueno que llegaste. Completame esto."

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

        doc "Mmm, sí. ¡Perfecto!"
        doc "Escuchame bien, estoy desarrollando un tratamiento experimental y necesito conej... Digo, sujetos de prueba."

        hide doc_mani
        show doc_normal at der
        with dissolve

        doc "Son tres aplicaciones y cobrás después de cada una."
        doc "Por la primera, 6000 dólares, en efectivo y sin marcar."
        doc "Las condiciones a cumplir son que no te laves ni te cortes el pelo durante todo el tratamiento."
        doc "Y firmar un acuerdo de confidencialidad para no hablar del tema con nadie."

        hide doc_normal
        show doc_eno at der
        with dissolve

        doc "Esto es muy serio: si llegás a romper alguna de esas cláusulas, me tenés que devolver todos y cada uno de los dólares."
        doc "Y si ya te los gastaste... te embargo hasta la vida."
        doc "Dicho esto, ¿aceptás?"

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

        fran "Esto me parece una banda."
        fran "Mejor lo dejamos acá."

        doc "Te estás perdiendo una oportunidad única en la vida."

        stop music fadeout 2.0

        hide fran_normal
        hide doc_eno
        with dissolve

    label acto1_escena10:
        scene hab_noche with dissolve

        show fran_triste with dissolve

        fran_int "¿Hice bien? Con esa plata hacía de todo..."

        play sound celular_vibra
        scene mensaje_viernes with dissolve

        pause

        scene black with fade

        "Al día siguiente"

    label acto1_escena11:

        scene hab_int with dissolve

        play sound celular_vibra

        pause 1.0

        scene mensaje_changa with dissolve

        fran_int "Y bueno. Si no queda otra."

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
        doc "Y nada de agua ni tijeras."
        doc "Ni una palabra a nadie."

        hide fran_sorpresa
        show fran_normal at izq
        with dissolve

        fran "Sí, sí… entendido."

        fran_int "Con esto pago todo y me sobra."

    #Acto 2

    label acto2_escena13:

        scene black with fade

        show expression credito("{size=+20}ACTO 2{/size}") as cartel at truecenter with Dissolve(1.0)
        pause 2
        hide cartel with Dissolve(1.0)

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

        fran "¿Mi pelo? Nada, un poco de shampoo de manzana nomás."

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

        fran_int "Hace una banda no dormía tan bien."

    label menu_habitacion_2:
        call screen objetos_escena(objetos_habitacion_ordenada)

        if _return == "celular":

            scene mensaje_comprobante with dissolve

            fran_int "Uno diría que se pondría contento porque le pagué."

            scene hab_ordenada
            show fran_largo_normal at lado_der
            with dissolve

            jump menu_habitacion_2

        elif _return == "boceto":

            scene boceto with dissolve

            "Meta para el local: USD 4000 / USD 30000"

            fran_int "Tuve que gastar bastante para ponerme al día, pero el resto lo guardo para el local."

            scene hab_ordenada
            show fran_largo_normal at lado_der
            with dissolve

            jump menu_habitacion_2

        elif _return == "puerta":
            menu:
                "Ir al comedor":
                    jump acto2_escena16

                "Todavía no":
                    jump menu_habitacion_2

    label acto2_escena16:

        scene comedor_pagadas
        show fran_largo_normal at lado_der
        with dissolve

        fran_int "¿Y ahora qué hago con tanto tiempo libre?"

    label menu_escena16:
        call screen objetos_escena(objetos_comedor_pagadas)

        if _return == "impuestos":
            fran_int "Todos pagados. Qué lindo es no preocuparse."

            jump menu_escena16

        elif _return == "puerta":
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

        pause

    label acto2_escena19:

        scene black with fade

        play music tema_casa fadeout 1.0 fadein 1.0 volume 0.6
        play sound golpes_puerta
        queue sound puerta_abre

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "¡Bueenaas!"

        fran "¡Mari! Vení, pasá. Ya llegó el pedido."

        ma "Cuando me enteré del menú, se me ocurrió traer agua con gas."

        scene comedor_sushi
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "Uhh... Se ve rico… ¿probás vos primero?"

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

        ma "El de abajo queda fijo y el de arriba aprieta."
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

        fran "Ah, tenés razón. Hana siempre rezaba antes de comer."
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico y me hacían preparar las comidas todas las mañanas. Era lindo."

        jump acto2_escena22

    label acto2_escena21:

        play sound cajon_abre

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¡Nahh! ¡Comer este manjar con tenedor es una falta de respeto!"

        fran "Uh, es verdad. ¡Si Hana me viera, me agarraría las pestañas con los palillos!"
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico y me hacían preparar las comidas todas las mañanas. Era lindo."

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

        ma "¡Pará! ¡No seas bestia! El jengibre va entre pieza y pieza, para limpiar el gusto."
        ma "Y este arroz está frío, tiene que estar tibio y con un poco más de vinagre. La textura está media fofa."

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

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

        ma "Hice un curso de cocina japonesa hace unos años."
        ma "Mi sueño era ser itamae, chef de sushi, y tener mi propia barra."

        hide mar_alivio
        show mar_preo at der
        with dissolve

        ma "Después se enfermó mi papá y bueno, lo tuve que dejar. Nunca pude terminar el curso, pero la parte práctica siempre se me dio bien."

        hide fran_largo_sorpresa
        show fran_largo_triste at izq
        with dissolve

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

        fran "Mirá, te propongo algo: cuando tenga mi local, la chef sos vos. ¿Qué te parece?"

        ma "Mirá que los itamae no son baratos, eh. Pero te tomo la palabra."

        jump acto2_escena34

    #Ruta pizza

    label acto2_escena26:

        scene mensaje_pizza1 with dissolve

        pause

        scene mensaje_pizza2 with dissolve

        fran_int "Una buena muzza nunca falla."

    label acto2_escena27:

        scene black with fade

        play music tema_casa fadeout 1.0 fadein 1.0 volume 0.6

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "¡Hola, Fran!"

        fran "¡Hola, Mari! Vení, pasá, ponete cómoda."

        ma "Qué raro verte tan contento. Hacía rato que no te veía así."

        fran "Se me están acomodando un poco las cosas."

        ma "Che, ¿soy yo o te creció el pelo?"

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

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

        jump acto2_escena30

    label acto2_escena29:

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "Si querés te lo corto yo. Hice un curso de peluquería, algo me acuerdo."

        fran "¡No! Digo… no, gracias. Otro día. Se nos va a llenar de pelos la pizza, si no."

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

        ma "¡Bien ahí! ¿Pudiste conseguir un trabajo por fin?"

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

        fran "Me salió una changa bastante grosa, tengo que pintar una casa entera."

        hide mar_alivio
        show mar_normal at der
        with dissolve

        ma "¿Vos pintando? No te imagino, pero dale, metele, así capaz te dan más laburo con los vecinos y eso."

        jump acto2_escena33

    label acto2_escena32:

        hide fran_largo_sorpresa
        show fran_largo_normal at izq
        with dissolve

        fran "Robé un banco. Shh, no le digas a nadie."

        ma "¡Mirá vos, no te tenía como un ratero, eh! Bueno, no me cuentes si no querés."

    label acto2_escena33:

        scene comedor_pizza
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        fran "¿Y a vos cómo te va en la vida?"

        ma "En el laburo, como siempre. Mucho trabajo y poca plata."
        ma "Pero alcanza para lo de mi papá, así que me conformo con eso."

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

    label menu_ida_clinica:
        menu:
            "¿En qué ir a la clínica?"

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

        rem "Uf… ¿no sentís olor feo?"

        fran "Debe venir de afuera, por ahí se ponen a arreglar las cloacas y eso."

        fran_int "La verdad es que es mío. Ni yo me aguanto."

        jump acto2_escena37

    label acto2_escena36:

        scene black with fade

        scene parada
        show fran_semana_triste
        with fade

        pas "¿Sentiste el olor?"

        fran_int "No sé si fue buena idea venir en micro."

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

        doc "¡Increíble, estupendo! Siete centímetros en siete días. ¿Picazón? ¿Olor? ¿Sueños raros?"

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
        doc "Te lo expliqué mientras te secaba el pelo. ¿Que no me escuchaste?"

        hide doc_mani
        show doc_normal at der
        with dissolve

        doc "No importa. Las condiciones siguen igual. Y la última paga es mucho mayor."

        hide fran_semana_normal
        show fran_semana_triste at izq
        with dissolve

        fran "¿Y no hay algo para la picazón? Aunque sea un perfume, porque la gente…"

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

    label menu_vuelta_clinica:
        menu:
            "¿En qué volver a casa?"

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
        call screen objetos_escena(objetos_garita, botones_garita)

        if _return == "personas":
            fran "Disculpá, ¿pasó el 45?"

            per "No sé, no sé. Alejate, por favor."

            jump menu_garita

        elif _return == "asiento":
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

        scene black with fade

        play sound puerta_cierra

    label acto2_escena41:

        scene comedor_pagadas
        show fran_muy_triste
        with dissolve

    label menu_comedor_encierro:
        call screen objetos_escena(objetos_comedor_encierro, botones_comedor_encierro)

        if _return == "salida":
            fran_int "Ni loco salgo así."

            jump menu_comedor_encierro

        elif _return == "habitacion":
            jump acto2_escena42

        elif _return == "bano":
            jump acto2_escena43

    label acto2_escena42:

        scene hab_int
        show fran_muy_normal
        with dissolve

    label menu_habitacion_encierro:
        call screen objetos_escena(objetos_habitacion_encierro)

        if _return == "boceto":
            scene boceto with dissolve

            "Meta para el local: USD 15000 / USD 30000"

            fran_int "Por esto lo hago."

            scene hab_int
            show fran_muy_normal
            with dissolve

            jump menu_habitacion_encierro

        elif _return == "computadora":
            scene video_yeti with dissolve

            pause

            fran_int "¿Ese soy yo?"

            scene hab_int
            show fran_muy_normal
            with dissolve

            jump menu_habitacion_encierro

        elif _return == "puerta":
            jump acto2_escena41

    label acto2_escena43:

        scene bano
        show fran_muy_triste at lado_der
        with dissolve

    label menu_bano:
        call screen objetos_escena(objetos_bano)

        if _return == "espejo":
            fran_int "Ni yo me reconozco."

            jump menu_bano

        elif _return == "maquina":
            fran_int "Dos minutos y se termina todo. Vuelvo a ser yo…"

            play sound golpes_puerta

            jump acto2_escena44

        elif _return == "puerta":
            jump acto2_escena41

    label acto2_escena44:

        scene mensaje_maria_puerta with dissolve

        pause

        play sound puerta_abre

        scene comedor_pagadas
        show fran_muy_triste at izq_pelo
        show mar_preo at der
        with dissolve

        ma "¡Fran! Abrime, por favor."
        ma "¿Pero qué te pasó? Vení, dejame cortar esos pelos."

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

                jump acto3_escena46

    label acto2_escena45:

        play sound maquina_cortar

        ma "Quedate quieto, son solo unos segundos."

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


#Acto 3

label acto3_escena46:

    stop music fadeout 1.5

    scene black with fade

    show expression credito("{size=+20}ACTO 3{/size}") as cartel at truecenter with Dissolve(1.0)
    pause 2
    hide cartel with Dissolve(1.0)

    # TEMPORAL: falta el tema lento y grave (S3-01); hasta tenerlo, silencio

    "Siete días después"

    scene hab_deteriorada
    show fran_muy_triste
    with fade

    fran_int "Ya ni sé qué día es. Me cuesta hasta levantar los brazos."

label menu_habitacion_acto3:
    call screen objetos_escena(objetos_habitacion_acto3)

    if _return == "celular":
        # TEMPORAL: texto hasta tener la imagen de los mensajes (AR3-07)
        "Mensajes sin leer de María:"
        "«Perdón si me metí.»"
        "«¿Estás bien?»"
        "«Te dejé comida en la puerta.»"

        fran_int "Y yo le cerré la puerta en la cara."

        jump menu_habitacion_acto3

    elif _return == "computadora":
        # TEMPORAL: la computadora con texto hasta tener el foro (AR3-08)
        scene computadora with dissolve

        "«Dicen que vive en las vías.»"
        "«Es un experimento del gobierno, posta.»"

        scene hab_deteriorada
        show fran_muy_triste
        with dissolve

        jump menu_habitacion_acto3

    elif _return == "boceto":
        scene boceto with dissolve

        "Meta para el local: USD 15000 / USD 30000"

        scene hab_deteriorada
        show fran_muy_normal
        with dissolve

        fran_int "Ya casi."

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje (AR3-07)
    "Mensaje del Dr. Malandra: «Esta noche, tercera y última aplicación. Vení cuando oscurezca.»"

label acto3_escena47:

    scene black with fade

    scene calle_noche
    show fran_muy_triste at center, noche
    with fade

    # TEMPORAL: faltan los pasos lentos (S3-02)
    play sound perro_ladra

    pause 1.5

    vec "¡Es el monstruo! ¡Marta, cerrá todo!"

    # TEMPORAL: faltan las persianas que bajan (S3-02)

label acto3_escena48:

    scene black with fade

    play music tema_clinica fadein 1.0

    scene consultorio_noche
    show fran_muy_normal at izq_pelo, noche
    show doc_mani at der, noche
    with fade

    doc "¡Mirate! ¡Es perfecto! Ni en mis mejores cálculos podría haber previsto semejante maravilla."

    play sound crema_squish

    # TEMPORAL: texto hasta tener la imagen de la tercera crema (AR3-09)
    "(Tercera aplicación de la crema.)"

    hide fran_muy_normal
    show fran_muy_sorpresa at izq_pelo, noche
    with dissolve

    hide fran_muy_sorpresa
    show fran_monstruo_enojo at izq_pelo, noche
    with Dissolve(1.2)

    fran "¿Para qué es todo esto, doctor?"

    stop music fadeout 1.0

    # TEMPORAL: texto hasta tener la imagen del peluquín (AR3-09)
    "(El doctor se saca el peluquín: es pelado.)"

    hide doc_mani
    show doc_pelado_normal at der, noche
    with Dissolve(1.0)

    doc "Desde mi infancia ya estaba así. ¿Sabés lo que es que se rían de vos por tu aspecto?"

    hide fran_monstruo_enojo
    show fran_monstruo_sorpresa at izq_pelo, noche
    with dissolve

    hide doc_pelado_normal
    show doc_pelado_mani at der, noche
    with dissolve

    doc "Siete días más. Si llegás, cobrás USD 15000, todo lo que tengo."

label acto3_escena49:

    scene black with fade

    "Día 3 de 7"

    scene bano_noche
    show fran_monstruo_triste at lado_der, noche
    with fade

    # TEMPORAL: faltan el rascado y la respiración agitada (S3-02)

    fran_int "Me pica hasta los huesos. No puedo dormir."

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje (AR3-07)
    "Mensaje de María: «No sé qué te pasa, pero si necesitás ayuda, estoy acá. Siempre.»"

    # TEMPORAL: texto hasta tener la imagen de la mano con la máquina (AR3-09)
    "(Francisco agarra la máquina y la prende.)"

    play sound maquina_cortar


label menu_decision10:

    $ vuelta_final_malo = "menu_decision10"

    scene bano_noche
    show fran_monstruo_triste at lado_der, noche
    with dissolve

    menu:
        "Cortarse el pelo":
            jump acto3_escena50

        "Apagar la máquina y aguantar":
            jump acto3_escena51

label acto3_escena50:

    play sound maquina_cortar

    show pelo_pantalla with Dissolve(1.5)

    pause 1.5

    stop sound fadeout 1.0
    scene black with fade

    jump final_malo_mensaje

label acto3_escena51:

    stop sound

    fran_int "No. Llegué hasta acá. Puedo aguantar un poco más."

    scene black with fade

    scene hab_deteriorada
    show fran_monstruo_triste
    with fade

    "Día 4"

    scene hab_deteriorada_noche
    show fran_monstruo_triste at center, noche
    with Dissolve(1.0)

    pause 1.0

    scene hab_deteriorada
    show fran_monstruo_triste
    with Dissolve(1.0)

    "Día 5"

    scene hab_deteriorada_noche
    show fran_monstruo_triste at center, noche
    with Dissolve(1.0)

    pause 1.0

    scene hab_deteriorada
    show fran_monstruo_triste
    with Dissolve(1.0)

    "Día 6"

    scene hab_deteriorada_noche
    show fran_monstruo_triste at center, noche
    with Dissolve(1.0)

    pause 1.0

    scene hab_deteriorada
    show fran_monstruo_triste
    with Dissolve(1.0)

    "Día 7"

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje (AR3-07)
    "Mensaje del Dr. Malandra: «La prueba terminó. Vení cuanto antes.»"

label acto3_escena52:

    scene black with fade

    # TEMPORAL: falta el tema lento y grave (S3-01); hasta tenerlo, solo los murmullos
    play ambiente murmullos fadein 1.5

    scene calle
    show fran_monstruo_normal
    with fade

    # TEMPORAL: faltan los pasos lentos y el pelo que se arrastra (S3-02)

    # TEMPORAL: texto hasta tener la imagen de los adolescentes (AR3-09)
    "(Desde la esquina, un grupo de adolescentes lo sigue, filmándolo con el celular.)"

    ado "¡Salió el yeti! ¡Grabalo, grabalo! ¡Che, monstruo, mirá para acá!"

    veca "¡Andá a bañarte, sucio! ¡Das asco!"

    vec "¡Volvete a las vías!"

    # TEMPORAL: faltan las risas y el aplauso (S3-02)

    menu:
        "Seguir caminando":
            pass

    hide fran_monstruo_normal
    show fran_monstruo_triste
    with dissolve

    menu:
        "Seguir caminando":
            pass

    stop ambiente fadeout 2.0

    scene black with fade

    scene centro with fade

    pause 1.5

label acto3_escena53:

    play music tema_clinica fadein 1.0

    scene consultorio
    show fran_monstruo_normal at izq_pelo
    show doc_pelado_normal at der
    with fade

    doc "El efecto ya se fijó. Ahora la parte más importante. Tengo que tomar todas las muestras que pueda, así que quedate quieto."

    play sound tijera

    scene black with fade

    # TEMPORAL: falta el agua cayendo (S3-02)
    pause 2.0

    scene consultorio
    show fran_sorpresa at izq
    show doc_pelado_normal at der
    with fade

    fran "Soy yo. Volví a ser yo."

    doc "Ahora andá y pegate una ducha que no te aguanto el olor."

    scene black with fade

    # TEMPORAL: falta el sonido de la ducha (S3-02)
    pause 2.0

    scene consultorio
    show fran_normal at izq
    show doc_pelado_normal at der
    with fade

    doc "Lo prometido. Ahora largate."

    hide fran_normal
    hide doc_pelado_normal
    play sound cajon_abre
    show vineta sobre at vineta_pos
    with dissolve

    "Recibiste USD 15000 — Meta para el local: USD 30000 / USD 30000"

    hide vineta
    with dissolve

    # TEMPORAL: texto hasta tener la imagen del espejo (AR3-09)
    "(Antes de que se cierre la puerta, Francisco ve al doctor frente al espejo, untándose la crema en la pelada. Después tira los frascos que sobran y rompe sus anotaciones.)"

    show doc_pelado_mani
    with dissolve

    doc "¡Nadie más va a tener esto! ¡Voy a ser el único calvo que recuperó su pelo!"

    stop music fadeout 1.5

label acto3_escena54:

    scene black with fade

    play music tema_barrio fadein 1.0

    scene parada_vacia
    show fran_normal
    with fade

    per "¡Buen día! ¿Esperás el 45? Ya está por pasar. ¿Viste lo del monstruo del barrio? Qué locura."

    fran_int "Hace un rato la gente se cruzaba de vereda para no tenerme cerca."

    fran "Sí, algo escuché."

label acto3_escena55:

    stop music fadeout 1.5

    scene black with fade

    play music tema_casa fadein 2.0

    scene casa_maria with fade

    # TEMPORAL: falta el timbre (S3-02)
    play sound puerta_abre

    show fran_triste at izq
    show mar_preo at der
    with dissolve

    ma "¿Fran…?"

    fran "Te debo una explicación. Y un perdón enorme."

    # Francisco le cuenta todo (D3-05): fundido hasta tener la imagen (AR3-09)
    scene black with fade

    pause 1.5

    scene casa_maria
    show fran_triste at izq
    show mar_det at der
    with fade

    ma "¿Por qué no me dijiste nada? Te podría haber pasado cualquier cosa."

    fran "Porque firmé un acuerdo de confidencialidad, pero ya está, se terminó."

    hide mar_det
    show mar_alivio at der
    with dissolve

    ma "Eso fue muy idiota de tu parte, Fran. Pero estás bien, y eso es lo que importa."

    stop music fadeout 1.5

    if cena_sushi:
        jump acto3_escena57
    else:
        jump acto3_escena56

label acto3_escena56:

    scene black with fade

    "Un mes después"

    # TEMPORAL: tema de barrio hasta tener el tema alegre (S3-01)
    play music tema_barrio fadein 1.0

    scene boceto with fade

    pause 1.0

    scene local_pizza with Dissolve(2.0)

    pause 1.5

    # TEMPORAL: falta la campanita de la puerta (S3-02)
    scene local_pizza_int
    show fran_normal at izq
    show mar_alivio at der
    with fade

    ma "¿Y? ¿Ya está abierto? ¡Quiero ser tu primer cliente!"

    fran "Para vos, la casa invita. Te debo como mil tápers."

    # TEMPORAL: texto hasta tener la imagen de la noticia (AR3-02)
    "Noticia en el celular: «El médico del conurbano que venció la calvicie: el Dr. Malandra luce una melena impecable y asegura que la fórmula se perdió para siempre. \"Fue un milagro, y es solo mío\"»."
    "(En la foto, el doctor sonríe… y se rasca la cabeza.)"

    scene black with fade

    "FINAL BUENO"
    "FIN"

    jump creditos

label acto3_escena57:

    scene black with fade

    "Un mes después"

    # TEMPORAL: tema de barrio hasta tener el tema alegre (S3-01)
    play music tema_barrio fadein 1.0

    scene boceto with fade

    pause 1.0

    scene local_sushi with Dissolve(2.0)

    pause 1.5

    # TEMPORAL: falta la campanita de la puerta (S3-02)
    scene local_sushi_int
    show fran_normal at izq
    show mar_normal at der
    with fade

    ma "¿Para qué me hiciste venir tan temprano?"

    # TEMPORAL: texto hasta tener la imagen del delantal (AR3-09)
    "(Francisco le señala la barra y le da un delantal.)"

    fran "Te dije que cuando tuviera el local, la chef ibas a ser vos."

    hide mar_normal
    show mar_alivio at der
    with dissolve

    ma "¡Pensé que era una joda! ¡Muchas gracias, Fran!"

    # TEMPORAL: texto hasta tener la imagen de la noticia (AR3-02)
    "Noticia en el celular: «El médico del conurbano que venció la calvicie: el Dr. Malandra luce una melena impecable y asegura que la fórmula se perdió para siempre. \"Fue un milagro, y es solo mío\"»."
    "(En la foto, el doctor sonríe… y se rasca la cabeza.)"

    scene black with fade

    "FINAL BUENO — CON MARÍA"
    "FIN"

    jump creditos

# Creditos de los finales buenos (D3-06, D3-07): terminan en el menu principal, sin botones

label creditos:

    scene black with fade

    play music tema_principal fadein 1.0

    show expression credito("{size=+30}A CONTRAPELO{/size}\n\nBasado en \"Piel de Oso\", de los hermanos Grimm") as cred at truecenter with Dissolve(1.0)
    pause 4
    hide cred with Dissolve(1.0)

    show expression credito("CREADO POR PENTANILO\n\nMejías, Fabricio — Producción\nGómez, Ignacio — Guion y sonido\nFernández, Lucas — Programación\nBrusadin, Bruno — Arte\nBoc-Ho, Gerardo — Programación") as cred at truecenter with Dissolve(1.0)
    pause 6
    hide cred with Dissolve(1.0)

    show expression credito("MÚSICA\n\nKevin MacLeod (incompetech.com)\nScheming Weasel (slower version) · Teller of the Tales\nCattails · Investigations\n\nLicensed under Creative Commons: By Attribution 4.0\nhttps://creativecommons.org/licenses/by/4.0/") as cred at truecenter with Dissolve(1.0)
    pause 6
    hide cred with Dissolve(1.0)

    show expression credito("EFECTOS DE SONIDO\n\nGómez, Ignacio\nFreesound.org (CC0): beansqueso31, sethlind, HunteR4708,\nwesleywestmusic, krnash, lucaslara, DeVern, Breviceps, lartti") as cred at truecenter with Dissolve(1.0)
    pause 5
    hide cred with Dissolve(1.0)

    show expression credito("Narrativa y Guiones para Videojuegos — UPSO, 2026\n\n¡Gracias por jugar!") as cred at truecenter with Dissolve(1.0)
    pause 4
    hide cred with Dissolve(1.0)

    stop music fadeout 2.0
    pause 2.0

    return
