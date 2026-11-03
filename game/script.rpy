label start:
    
    #A1E0 (Completar)


    #Acto 1 - Escena 1

    label acto1_escena1:

        scene hab_int with dissolve

        "Francisco, pagame el alquiler antes del viernes."
        "No quiero que pase como el mes pasado"

        show fran_normal

        fran "¿Antes del viernes? Si apenas llego a mañana..."

        #hide fran_normal

        #show fran_triste

        fran "¿Hasta cuando voy a estar así?"
        fran "Necesito un laburo fijo, algo en serio."

    #Acto 1 - Escena 2

    label acto1_escena2:

        scene hab_int with dissolve

        show fran_normal at center

        "Elegí un objeto para interactuar"

    label menu_habitacion:
        menu:
            "Ver el celular":
                $ celular_visto = True

                "Mensaje del Dueño: 'Francisco, pagame el alquiler antes del viernes. No quiero que pase como el mes pasado.'"
                fran "Qué manera de ser molesto. ¿No me puede dejar un día tranquilo?"
                jump menu_habitacion
            
            "Examinar el boceto ":
                $ boceto_visto = True
                "Examinás el boceto a mano del local de comida."
                fran "Ojalá algún día se haga realidad. Solo necesito juntar para arrancar; lo demás viene solo."
                jump menu_habitacion
            
            "Usar la computadora":
                jump submenu_computadora
    
    label submenu_computadora:
    fran "(A ver qué hay por acá...)"
    
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

    #Primero plano de una pagina de avisos clasificados #

    show fran_normal

    fran "A ver si hay algo en gastronomía para arrancar tranqui."

    label menu_trabajos:
        menu:
            "Buscar trabajo de mozo" if not mozo_visto:

                $ mozo_visto = True

                "Requisito: Dos años de experiencia."
                "RECHAZADO"

                show fran_normal

                fran "Si nadie te contrata, ¿cómo vas a juntar experiencia?"

                hide fran_normal

                jump menu_trabajos

            "Buscar trabajo de repartidor" if not repartidor_visto:

                $ repartidor_visto = True

                "Requisito: Moto propia."
                "RECHAZADO"

                show fran_normal

                fran "Era obvio. Tampoco iba a repartir las pizzas corriendo."

                hide fran_normal

                jump menu_trabajos

            "Buscar trabajo de ayudante de cocina" if not ayudante_visto:

                $ ayudante_visto = True

                "Página saturada. Todas la postulaciones fueron rechazadas."
                
                show fran_normal

                fran "Y eso que algo me había enseñado Hana."
                fran "Se que que todos buscan laburo."

                hide fran_normal

                jump menu_trabajos
        

        show fran_normal with dissolve

        fran "Por más que intente, nada."
        fran "Me voy a hacer unos mates."

    #Acto 1 - Escena 4
    label acto1_escena4:

        scene cocina with dissolve

        label menu_cocina:
            menu:
                "Heladera":
                    show fran_normal
                    fran "Un limón, un tomate a punto de pudrirse y agua."
                    fran "Tremendo banquete."
                    hide fran_normal

                    jump menu_cocina
                
                "Tupper de Maria":
                    show fran_normal
                    fran "Si anoche comí, fue gracias a Maria."
                    fran "Tengo que devolverle el tupper."
                
                "Mate":
                    jump sub_menu_mate
            
        label sub_menu_mate:
            menu:
                "Preparar mate":
                    "Francisco se termina la poca yerba que le quedaba."
                    show fran_normal
                    "Ya ni para la yerba me alcanza."
                    "Si no fuera por María, me moría de hambre."
                    
                    #Golpes
                    fran "¿Quien golpea?"

                    hide fran_normal
                    
                    jump acto1_escena5

                "Todavía no":
                        jump menu_cocina    

    #Acto 1 - Escena 5

    label acto1_escena5:

        scene hab_interior

        label menu_conocer:
            scene hab_int
            menu:
                "Facturas":
                    show fran_normal
                    "Luz, gas, internet... se me juntan todas."
                
                "Puerta de salida":
                    jump sub_menu_conocer
        
        label sub_menu_conocer:
            scene hab_int
            menu:
                "Atender la puerta":
                    show mar_normal
                    ma "¡Hola Fran! Vengo a buscar el tupper."
                    hide mar_normal

                    show fran_normal
                    fran "Hola Mari. Gracias por la cena, de verdad. ¿Pasas?"
                    fran "Hice unos mates."
                    hide fran_normal

                    show mar_normal
                    "Dale. ¿Cómo andás con la búsqueda?"
                    hide mar_normal

                    show fran_normal
                    fran "Mal. No sale nada y las facturas se me apilan."
                    fran "¿Y vos en el laburo?"
                    hide fran_normal

                    show mar_normal
                    ma "No es lo que más me gusta, pero me alcanza para el tratamiento de mi papá."
                    hide mar_normal
                    show mar_normal
                    ma "No te castigues tanto. Salí a dar una vuelta, despejate"
                    ma "Y te dejo torta para después."
                    hide mar_normal

                "Todavía no":
                    jump acto1_escena5

        "María agarra su tupper, deja otro con torta sobre la mesa y se va."

        show fran_normal

        fran "Bueno, debería hacerle caso a Mari, después de terminarme el termo."

    label acto1_escena6:


