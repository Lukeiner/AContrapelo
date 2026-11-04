label start:
    
    #A1E0

    scene black
    show text "GRUPO PENTANILO PRESENTA" at truecenter with Dissolve(1.0)
    pause 5
    hide text with Dissolve(1.0)
    show text "A CONTRAPELO" at truecenter with Dissolve(1.0)
    pause 2
    hide text with Dissolve(1.0)


    #Acto 1 - Escena 1

    label acto1_escena1:

        scene hab_int with dissolve

        pause 1.0

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

    label menu_trabajos:
        menu (screen="choice_pc"):
            "Buscar trabajo de mozo" if not mozo_visto:

                $ mozo_visto = True

                "Requisito: dos años de experiencia."
                "Rechazado."

                show fran_normal with dissolve

                fran_int "Si nadie te contrata, ¿cómo vas a juntar experiencia?"

                hide fran_normal with dissolve

                jump menu_trabajos

            "Buscar trabajo de repartidor" if not repartidor_visto:

                $ repartidor_visto = True

                "Requisito: moto propia."
                "Rechazado."

                show fran_normal with dissolve

                fran_int "Era obvio. Tampoco iba a repartir las pizzas corriendo."

                hide fran_normal with dissolve

                jump menu_trabajos

            "Buscar trabajo de ayudante de cocina" if not ayudante_visto:

                $ ayudante_visto = True

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
                    show fran_normal with dissolve
                    fran_int "Un limón, un tomate a punto de pudrirse y agua."
                    fran_int "Tremendo banquete."
                    hide fran_normal with dissolve

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
                    "Francisco se termina la poca yerba que le quedaba."
                    show fran_triste with dissolve
                    fran_int "Ya ni para la yerba me alcanza."
                    fran_int "Si no fuera por María, me moría de hambre."
                    
                    #Golpes
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
                "Facturas":
                    show fran_normal with dissolve
                    fran_int "Luz, gas, internet... se me juntan todas."
                    hide fran_normal with dissolve
                    jump menu_conocer
                
                "Puerta de salida":
                    jump sub_menu_conocer
        
        label sub_menu_conocer:
            menu:
                "Atender la puerta":
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
                    fran "Mal. No sale nada y las facturas se me apilan."
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

        "María agarra su táper, deja otro con torta sobre la mesa y se va."

        hide mar_alivio with dissolve

        hide fran_triste
        show fran_normal at izq
        with dissolve

        fran_int "Bueno, debería hacerle caso a Mari, después de terminarme el termo."

    label acto1_escena6:

        scene calle with dissolve

        show fran_triste with dissolve

        fran_int "Capaz pueda vender algo de ropa."
        fran_int "Ya no se me ocurre nada."

        hide fran_triste with dissolve

        "Francisco ve gente amontonada frente a un poste."
        scene parada with dissolve

        "Cuando se acerca, se dispersan y queda a la vista un cartel."

        show fran_sorpresa with dissolve
        fran_int "Justo cuando necesito plata..."
        fran_int "Queda a unas cuadras."
        fran_int "Paso a ver."

    label acto1_escena7:

        scene centro with dissolve
        with hpunch

        "Un candidato sale apurado, casi lo choca."

        cand "¡Está loco ese tipo! Nadie va a aceptar hacerse eso."

        show fran_triste with dissolve

        fran_int "Se nota que él no necesita plata. El alquiler no se paga solo."

    label acto1_escena8:

        scene consultorio with dissolve

        show fran_normal at izq with dissolve

        fran "Buen día, vengo por el anuncio..."

        show doc_normal at der with dissolve

        "Aparece el Dr. Malandra y le pone un cuestionario en las manos."

        doc "Qué bueno que llegaste. Completame esto."

        menu:
            "¿Vivís solo?"
            "Sí, vivo solo":
                pass
            "Sí, hace rato":
                pass

        menu:
            "¿Alguien notaría si no te ve por un tiempo?"
            "Nadie lo notaría":
                pass
            "Casi nadie":
                pass

        menu:
            "Del 1 al 10, ¿cuánto te importa lo que piense la gente?"
            "1":
                pass
            "2":
                pass

        hide doc_normal
        show doc_mani at der
        with dissolve

        doc "¡Perfecto! Sos la persona ideal."
        doc "Estoy desarrollando un producto para el crecimiento capilar."

        hide doc_mani
        show doc_eno at der
        with dissolve

        doc "Son tres aplicaciones y cobrás en cada una."
        doc "Por la primera, 6000 dólares."
        doc "Condiciones: no lavarte ni cortarte el pelo mientras dure el tratamiento, y no contarle a nadie."

        hide doc_eno
        show doc_normal at der
        with dissolve

        doc "Si no cumplís, devolvés la plata y te embargo los bienes."
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

        hide doc_normal
        show doc_eno at der
        with dissolve

        doc "¡Es por la ciencia!"
        doc "Te estás perdiendo la oportunidad de tu vida."

        hide fran_normal
        hide doc_eno
        with dissolve

        "Francisco vuelve caminando a su casa. Se le hace de noche."

    label acto1_escena10:
        scene hab_noche with dissolve


        show fran_triste with dissolve

        fran_int "¿Hice bien? Con esa plata pagaba todo..."
        fran_int "y hasta capaz invitaba a María a comer algo."

        scene mensaje_viernes with dissolve

        fran_int "Otra vez. No se cansa."
    
    label acto1_escena11:

        scene hab_int with dissolve

        pause 1.0

        scene mensaje_changa with dissolve

        fran_int "Y bueno."
        fran_int "Si no queda otra."

        scene hab_int
        show fran_triste
        with dissolve

        "Francisco contesta y se prepara para salir. Nada cambió."

        "FINAL NORMAL — TODO SIGUE IGUAL"
        "FIN"

        label menu_normal:
            menu:
                "Volver a la última decisión":
                    scene consultorio
                    show fran_triste at izq
                    show doc_normal at der
                    with dissolve
                    jump menu_trato


                "Salir al menú":
                    return
    
    label acto1_escena12:

        hide fran_triste
        show fran_normal at izq
        with dissolve

        "Francisco firma el contrato."

        hide doc_normal
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

        show vineta secador at vineta_pos with dissolve

        doc "Mirá, al oxidarse, el péptido reacciona con la queratina del folículo..."
        doc "...lo que acelera la mitosis capilar en un cuatrocientos por ciento, según mis cálculos..."
        fran_int "Con tanta palabrería y el secador no escuché nada."

        hide vineta
        show fran_normal at izq
        show doc_mani at der
        with dissolve

        doc "Ahora la crema. Solo se aplica acá, en ambiente estéril."

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

        doc "No, no. Solo dejame anotar."

        hide fran_normal
        hide doc_normal
        show vineta medicion at vineta_pos
        with dissolve

        pause 3.0

        hide vineta
        show fran_normal at izq
        show doc_normal at der
        with dissolve

        "Recibiste USD 6000"

        doc "Nos vemos en una semana."
        doc "Nada de agua, nada de tijera"
        doc "y ni una palabra a nadie."

        hide fran_normal
        show fran_sorpresa at izq
        with dissolve

        fran "¿Todo esto es para mí?"
        fran "Sí, sí… entendido."

        hide fran_sorpresa
        show fran_normal at izq
        with dissolve

        fran_int "Con esto pago todo y me sobra."
        fran_int "Mejor vuelvo en colectivo."
