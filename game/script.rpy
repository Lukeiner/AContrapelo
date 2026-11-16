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
                    with Dissolve(1.0)

                    pause 1.0

                    play sound golpes_puerta

                    pause 0.8

                    hide fran_triste
                    show fran_sorpresa
                    with dissolve

                    fran_int "¿Y ahora quién será?"

                    hide fran_sorpresa with Dissolve(1.0)

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

        show parada_vacia at zoom_cartel

        pause 3.0

        fran_int "Justo cuando necesito plata..."

        scene black with fade

        "Unos minutos después"

    label acto1_escena7:

        play sound puerta_golpe
        scene candidato with dissolve
        with hpunch

        cand "¡Pero ese tipo está loco! Nadie va a aceptar hacerse eso."

        scene centro
        show fran_normal
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

        scene parada_gente2
        show fran_normal at lado_der
        with dissolve

        fran "Disculpá, ¿pasó hace mucho el 45?"

        per "Ya debe estar por venir."
        per "Che, qué pelo brilloso tenés."
        per "¿Qué te ponés?"

        hide fran_normal
        show fran_sorpresa at lado_der
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

        ma "Che, ¿y cómo hiciste para pagar todo esto? ¿Tenés algo para contarme?"

        fran "Me están saliendo bien las cosas, por lo visto. No quiero contar mucho por si no se da, pero quería agradecerte el aguante todo este tiempo."

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¡Re bien, Fran! Yo sabía que ibas a poder, ¿ves?"

        hide mar_alivio
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

        fran_int "¿Cómo podría darle una mano a Mari sin que sospeche tanto?"

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

        hide fran_largo_normal
        hide mar_alivio
        show vineta charla_sushi at vineta_pos
        with dissolve

        pause 3.0

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

        scene remis_ida with dissolve

        rem "Uf… ¿no sentís olor feo?"

        fran "Debe venir de afuera, por ahí se ponen a arreglar las cloacas y eso."

        scene remis_aromatizante with dissolve

        fran_int "La verdad es que es mío. Ni yo me aguanto."

        scene remis_llegada with dissolve

        pause 1.5

        jump acto2_escena37

    label acto2_escena36:

        scene black with fade

        scene parada_gente2
        show fran_semana_triste at lado_der
        with fade

        pas "¿Sentiste el olor?"

        fran_int "No sé si fue buena idea venir en micro."

        scene black with fade

        "Francisco se tomó el colectivo y llegó a la clínica."

    label acto2_escena37:

        scene black with fade

        scene centro with fade

        pause 1.5

        play music tema_clinica fadein 1.0

        scene consultorio
        show vineta medicion at vineta_pos
        with fade

        pause 2.0

        hide vineta
        show fran_semana_normal at izq
        show doc_mani at der
        with dissolve

        doc "¡Increíble, estupendo! Siete centímetros en siete días. ¿Picazón? ¿Olor? ¿Sueños raros?"

        fran "Todo eso, sí."

        doc "Sí, sí, está saliendo todo como esperaba. Ahora quedate quieto."

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

        doc "No importa. Las condiciones siguen igual."
        doc "Mirá, para compensar voy a agregar más plata. Esto es muy importante para mí y no podés fallar."

        hide fran_semana_normal
        show fran_semana_triste at izq
        with dissolve

        fran "¿Y no hay algo para el olor? Aunque sea un perfume, porque la gente…"

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

        "Recibiste USD 7000"

        stop music fadeout 1.5

        scene black with fade

        scene centro
        show fran_semana_triste
        with fade

        fran_int "Ya está por pasar el bondi, si me apuro seguro lo alcanzo."

    label acto2_escena38:

        scene black with fade

        scene parada_gente1
        show fran_semana_triste at lado_der
        with fade

    label menu_garita:
        call screen objetos_escena(objetos_garita)

        if _return == "personas":
            if not garita_ignorado:
                $ garita_ignorado = True

                fran "Disculpá, ¿pasó el 45?"

                per "No, pero ya…"
                per "¡Puaj!"
                per "Ya debe estar por venir. Disculpá, me tengo que ir."

            else:
                fran "Disculpá…"

                per "…"

            jump menu_garita

        elif _return == "asiento":
            scene black with fade

            # TEMPORAL: falta la viñeta tipo cómic del colectivo de costado, con el colectivero mirando al jugador
            "(El colectivo frena en la parada. El colectivero mira a Francisco.)"

            col "No, flaco, con esa baranda no te puedo dejar subir. Recién limpiamos."

            jump acto2_escena40

    label acto2_escena40:

        scene parada
        show fran_semana_triste
        with fade

        fran_int "Bueno, caminando entonces."

        hide fran_semana_triste
        show fran_cintura
        with Dissolve(1.2)

        hide fran_cintura
        show fran_muy_sorpresa
        with Dissolve(1.2)

        fran_int "¿Qué…? ¡¿Qué me está pasando?!"

        ado "¡Miralo! ¡Parece un yeti! ¡Grabalo!"

        # TEMPORAL: falta la imagen desde el celular del adolescente que lo graba
        "(Un adolescente lo graba con el celular mientras Francisco sale corriendo.)"

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

            "Meta para el local: USD 11000 / USD 30000"

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
            # TEMPORAL: falta la imagen del espejo desde los ojos de Francisco, con todo el pelo
            "(En el espejo, Francisco se ve con el pelo larguísimo.)"

            fran_int "Ni yo me reconozco."

            jump menu_bano

        elif _return == "maquina":
            fran_int "¡No puedo andar con el pelo así, es una locura! Quizás pueda…"

            play sound golpes_puerta
            queue sound golpes_puerta
            queue sound golpes_puerta

            pause 2.5

            jump acto2_escena44

        elif _return == "puerta":
            jump acto2_escena41

    label acto2_escena44:

        play sound celular_vibra

        pause 1.0

        scene mensaje_maria_puerta with dissolve

        pause

        play sound puerta_abre

        scene comedor_pagadas
        show fran_muy_triste at izq_pelo
        show mar_preo at der
        with dissolve

        ma "¡Fran! ¡¿Pero qué te pasó?!"

        fran "¡Mari! ¡No me veas, por favor!"

        ma "No te preocupes, Fran, pero decime, ¿qué te pasó?"

    label menu_decision9:

        $ vuelta_final_malo = "menu_decision9"

        scene comedor_pagadas
        show fran_muy_triste at izq_pelo
        show mar_preo at der
        with dissolve

        menu:
            "Contar lo que pasó":
                jump acto2_escena45

            "No decir nada y cerrarle la puerta":
                play sound puerta_cierra

                fran_int "Perdón, Mari, no puedo decirte nada."

                jump acto3_escena46

    label acto2_escena45:

        ma "Está bien, Fran. Por ahora vení, vamos a cortarte esos pelos."

        play sound maquina_cortar

        ma "Quedate quieto, son solo unos segundos."

        hide fran_muy_triste
        show fran_monstruo_sorpresa at izq_pelo
        with Dissolve(0.5)

        show pelo_pantalla with Dissolve(1.5)

        pause 2.0

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
        # TEMPORAL: texto hasta tener la imagen del mensaje de María
        "Mensajes de María: «Fran, ¿por qué no me respondés? Podés confiar en mí.»"

        fran_int "Y yo le cerré la puerta en la cara."

        # TEMPORAL: texto hasta tener la imagen del mensaje viejo del Dr. Malandra
        "Mensaje anterior del Dr. Malandra: «No te preocupes, está todo dentro de lo planeado. Aguantate unos días más.»"

        jump menu_habitacion_acto3

    elif _return == "computadora":
        # TEMPORAL: la computadora con texto hasta tener la imagen del Instagram
        scene computadora with dissolve

        "Publicación: «¿Alguien sabe qué es esto? Lo grabaron ayer en el barrio.»"
        "«Es un disfraz, se nota de lejos.»"
        "«Dicen que vive en las vías.»"
        "«Es un experimento del gobierno, posta.»"

        scene hab_deteriorada
        show fran_muy_triste
        with dissolve

        jump menu_habitacion_acto3

    elif _return == "boceto":
        scene boceto with dissolve

        "Meta para el local: USD 11000 / USD 30000"

        scene hab_deteriorada
        show fran_muy_normal
        with dissolve

        fran_int "Ya casi."

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje
    "Mensaje del Dr. Malandra: «Ya es la hora. Venite a la noche, así evitamos ojos curiosos.»"

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
    doc "¿Estás listo para la próxima aplicación? Quedate quieto."

    play sound crema_squish

    # TEMPORAL: texto hasta tener la imagen de la tercera crema (AR3-09)
    "(Tercera aplicación de la crema.)"

    hide fran_muy_normal
    show fran_muy_sorpresa at izq_pelo, noche
    with dissolve

    pause 2.0

    hide fran_muy_sorpresa
    show fran_monstruo_enojo at izq_pelo, noche
    with Dissolve(2.0)

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

    # BORRADOR para que revise Fabricio: el pasado y la motivación de Malandra
    doc "En la escuela me decían «bola de billar». En la facultad, «el doctor Huevo»."
    doc "Probé de todo: lociones, implantes, curanderos. Nada funcionó."
    doc "Así que me puse a investigar por mi cuenta. Treinta años de fórmulas, y vos sos el primero en el que funciona."
    doc "Vendí el auto, hipotequé la casa y puse cada peso que tenía en este consultorio."

    hide doc_pelado_normal
    show doc_pelado_mani at der, noche
    with dissolve

    doc "Si esto sale bien, nunca más se va a reír nadie de mí."

    hide doc_pelado_mani
    show doc_pelado_normal at der, noche
    with dissolve

    doc "Acá está tu paga."

    # TEMPORAL: el sobre hasta tener la imagen de Francisco cobrando
    hide fran_monstruo_sorpresa
    hide doc_pelado_normal
    play sound cajon_abre
    show vineta sobre at vineta_pos
    with dissolve

    "Recibiste USD 8000"

    hide vineta
    show fran_monstruo_normal at izq_pelo, noche
    show doc_pelado_normal at der, noche
    with dissolve

    doc "Ahora necesito una última cosa más. Necesito que el producto haga efecto una semana más."

    hide doc_pelado_normal
    show doc_pelado_mani at der, noche
    with dissolve

    doc "Hacelo, y cuando vuelvas vas a tener todo el dinero que me queda. Necesito que esto funcione a como dé lugar."

    stop music fadeout 1.5

    scene black with fade

    scene hab_deteriorada_noche
    show fran_monstruo_triste at center, noche
    with fade

    fran_int "No sé si voy a poder aguantar tanto."

    scene black with fade

    "Al día siguiente"

    scene hab_deteriorada
    show fran_monstruo_triste
    with fade

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje
    "Mensaje de María: «Fran, parece que no confiás tanto en mí como para decirme qué te está pasando, pero yo ya no puedo estar preocupándome así. No te pienso seguir escribiendo.»"

    fran_int "Perdón, Mari. No puedo arriesgarme a romper el contrato después de pasar por todo esto."

    scene black with fade

    "Al día siguiente"

    scene hab_deteriorada
    show fran_monstruo_triste
    with fade

    fran_int "Esto me está volviendo loco, no me aguanto el olor. Tengo que salir."

    scene black with fade

    scene calle_noche
    show fran_monstruo_normal at center, noche
    with fade

    play sound perro_ladra

    pause 1.0

    ado "¡Ahí está el monstruo! ¡Corran!"

    veca "¡Ay, Dios mío! ¡Metete adentro, nena!"

    vec "¡Andate de acá, bicho asqueroso!"

    hide fran_monstruo_normal
    show fran_monstruo_triste at center, noche
    with dissolve

    fran_int "¿Por qué me odian tanto? Si no les hice nada."
    fran_int "No fue buena idea haber salido."

    scene black with fade

    play sound puerta_cierra

    pause 1.0

label acto3_escena49:

    "Día 6"

    scene bano_noche
    show fran_monstruo_triste at lado_der, noche
    with fade

    # TEMPORAL: faltan el rascado y la respiración agitada (S3-02)

    fran_int "Ahhh, ya no aguanto más."

    # TEMPORAL: texto hasta tener la imagen de la mano con la máquina (AR3-09)
    "(Francisco agarra la máquina y la prende.)"

label menu_decision10:

    $ vuelta_final_malo = "menu_decision10"

    # La máquina sigue prendida hasta que se elige qué hacer
    play ambiente maquina_loop fadein 0.3

    scene bano_noche
    show fran_monstruo_triste at lado_der, noche
    with dissolve

    menu:
        "Cortarse el pelo":
            jump acto3_escena50

        "Apagar la máquina y aguantar":
            jump acto3_escena51

label acto3_escena50:

    show pelo_pantalla with Dissolve(1.5)

    pause 1.5

    stop ambiente fadeout 1.0
    scene black with fade

    jump final_malo_mensaje

label acto3_escena51:

    stop ambiente

    fran_int "No. Llegué hasta acá. Puedo aguantar un poco más."

    scene black with fade

    "Al día siguiente"

    scene hab_deteriorada
    show fran_monstruo_triste
    with fade

    play sound celular_vibra

    pause 1.0

    # TEMPORAL: texto hasta tener la imagen del mensaje
    "Mensaje del Dr. Malandra: «Ya es la hora. Vení cuanto antes.»"

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

    play sound perro_ladra

    ado "¡Eh, yeti! ¡Sonreí para la cámara!"

    veca "¡No te acerques a los chicos, degenerado!"

    vec "¡Que alguien llame a la policía!"

    hide fran_monstruo_normal
    show fran_monstruo_triste
    with dissolve

    fran_int "Solo unas cuadras más."

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

    doc "Ahora andá y pegate una ducha, que no te aguanto el olor."
    doc "El baño está al fondo, ya te preparé todo."

    scene black with fade

    # TEMPORAL: falta el sonido de la ducha (S3-02)
    pause 2.5

    scene consultorio
    show fran_normal at izq
    show doc_pelado_normal at der
    with fade

    doc "Lo prometido. Ahora tomatela, tengo que hacer unos experimentos que no te incumben."

    hide fran_normal
    hide doc_pelado_normal
    play sound cajon_abre
    show vineta sobre at vineta_pos
    with dissolve

    "Recibiste USD 23750"

    hide vineta
    with dissolve

    # TEMPORAL: texto hasta tener las imágenes de Malandra con la crema y rompiendo los frascos (AR3-09)
    "(Antes de que se cierre la puerta, Francisco ve al doctor frente al espejo, untándose la crema en la pelada.)"
    "(Después rompe los frascos que sobran.)"

    show doc_pelado_mani
    with dissolve

    doc "¡Nadie más va a tener esto! ¡Voy a ser el único calvo que recuperó su pelo!"

    stop music fadeout 1.5

label acto3_escena54:

    scene black with fade

    play music tema_barrio fadein 1.0

    scene parada_gente2
    show fran_normal at lado_der
    with fade

    fran_int "No puedo creer que esta locura se terminó."

    per "¡Buen día! ¿Esperás el 45? Ya está por pasar. ¿Viste lo del monstruo del barrio? Qué locura."

    fran_int "Hace un rato la gente se cruzaba de vereda para no tenerme cerca."

    fran "Sí, algo escuché."

    per "No puedo creer que ande semejante bicho dando vueltas por la calle. Tendrían que haberlo agarrado y revoleado a un zoológico."

    fran "¿Y si te dijera que era un flaco común y corriente que se sometió a un experimento para el crecimiento del pelo y no podía lavárselo ni cortárselo por varias semanas?"

    per "Nah, vos pensás como esa chica que juraba que el monstruo ese era su amigo, un flaco que de un día para el otro se volvió un monstruo peludo."

    fran_int "Eso me hizo acordar… Tengo que ir a hablar con Mari."

    stop music fadeout 1.5

    scene black with fade

    play sound auto_movimiento

    pause 2.5

label acto3_escena55:

    play music tema_casa fadein 2.0

    # TEMPORAL: la calle hasta tener el frente del departamento de María (AR3-05)
    scene casa_maria with fade

    play sound golpes_puerta

    show fran_normal
    with dissolve

    pause 1.0

    play sound puerta_abre

    hide fran_normal
    show fran_normal at izq
    show mar_preo at der
    with dissolve

    ma "¿Fran…?"

    fran "Mari, escuchame, te debo una explicación y una disculpa enorme."

    scene black with fade

    "Varios minutos después"

    scene casa_maria
    show fran_normal at izq
    show mar_det at der
    with fade

    ma "¿Pero estás loco? Mirá si te pasaba algo: un día lluvioso y chau contrato. ¡O si alguien te tiraba un baldazo de agua!"

    fran "Y por eso no podía salir a ningún lado, o tenía que salir a escondidas. Pero bueno, ya se terminó esa pesadilla."

    hide mar_det
    show mar_preo at der
    with dissolve

    ma "Me sigue pareciendo una locura, parece un cuento de hadas lo que me contás. Pero lo importante es que ya estás bien, ¿no?"

    fran "Sí, ya no debería quedarme nada del producto en la cabeza, y pretendo dejarme el pelo bien prolijo de ahora en más."

    hide mar_preo
    show mar_alivio at der
    with dissolve

    ma "Aunque, ahora que lo pienso, no te quedaba mal el pelo al hombro, eh. ¡Podrías dejártelo crecer de vez en cuando!"

    hide fran_normal
    show fran_sorpresa at izq
    with dissolve

    fran "¡Noo, ni en pedo!"

    # TEMPORAL: faltan los sprites de los dos riéndose
    hide fran_sorpresa
    show fran_normal at izq
    with dissolve

    pause 1.5

    stop music fadeout 1.5

    scene black with fade

    "Un mes después"

    # TEMPORAL: tema de barrio hasta tener el tema alegre (S3-01)
    play music tema_barrio fadein 1.0

    scene boceto with fade

    pause 1.0

    # TEMPORAL: el boceto hasta tener la fachada con el cartel "Gran inauguración" y la gente esperando
    if cena_sushi:
        scene local_sushi with Dissolve(2.0)
    else:
        scene local_pizza with Dissolve(2.0)

    pause 1.5

    show fran_normal at izq
    show mar_alivio at der
    with dissolve

    fran "¡Por fin, ya está todo preparado!"

    ma "¡Bravo, Fran! Y decime, ¿yo tengo que hacer reservación para venir a comer, como los simples mortales?"

    if cena_sushi:
        jump acto3_escena57
    else:
        jump acto3_escena56

label acto3_escena56:

    fran "¿Vos? Pero por favor, vos comés gratis."

    hide mar_alivio
    show mar_normal at der
    with dissolve

    ma "Ay, no, Fran, algo te voy a pagar, estás loco."

    fran "¡Bueno, si insistís!"
    fran "Lo que no te voy a cobrar es esto."

    # TEMPORAL: el táper del Acto 1 hasta tener la imagen del táper con comida
    hide fran_normal
    hide mar_normal
    show vineta taper at vineta_pos
    with dissolve

    fran "Sé que no se acerca a los tuyos, pero tengo que devolverte como mil comidas. Que esta sea la primera. Pasá, dale."

    # TEMPORAL: el boceto y texto hasta tener la imagen del local lleno
    scene local_pizza_int with fade

    "(Francisco trabaja en el local lleno, mientras María lo mira.)"

    jump noticia_malandra

label acto3_escena57:

    fran "¿Vos? Para vos tengo una propuesta especial."

    # TEMPORAL: texto hasta tener la imagen
    "(Francisco le señala la barra de sushi.)"

    fran "Te dije que cuando tuviera el local ibas a ser la chef. ¿Qué me decís, aceptás?"

    ma "¿En serio me decís? ¡Obvio que sí! ¡Ya arranco!"

    # TEMPORAL: el boceto y texto hasta tener la imagen de los dos vestidos de chef en el local lleno
    scene local_sushi_int with fade

    "(Francisco y María trabajan juntos, vestidos de chef, en el local lleno.)"

    jump noticia_malandra

label noticia_malandra:

    # TEMPORAL: texto hasta tener la imagen de la noticia (AR3-02)
    "Noticia en el celular: «El médico del conurbano que venció la calvicie: el Dr. Malandra luce una melena impecable y asegura que la fórmula se perdió para siempre. \"Fue un milagro, y es solo mío\"»."
    "(En la foto, el doctor sonríe… y se rasca la cabeza.)"

    scene black with fade

    if cena_sushi:
        "FINAL BUENO — CON MARÍA"
    else:
        "FINAL BUENO"

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
