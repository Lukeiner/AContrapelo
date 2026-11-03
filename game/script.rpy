label start:
    
    #A1E0 (Completar)


    #Acto 1 - Escena 1

    label acto1_escena1:

        scene hab_int with dissolve

        "Francisco se despierta y agarra el celular."

        "Francisco, pagame el alquiler antes del viernes."
        "No quiero que pase como el mes pasado."

        show fran_normal

        fran "¿Antes del viernes? Si apenas llego a mañana."

        hide fran_normal

        show fran_triste

        fran "¿Hasta cuándo voy a estar así?"
        fran "Necesito un laburo fijo, algo en serio."

    #Acto 1 - Escena 2

    label acto1_escena2:

        scene hab_int with dissolve

        show fran_normal at center

        "Elegí un objeto para interactuar."

    label menu_habitacion:
        menu:
            "Ver el celular":
                $ celular_visto = True

                "Mensaje del Dueño: 'Francisco, pagame el alquiler antes del viernes. No quiero que pase como el mes pasado.'"
                fran "Qué manera de ser molesto. ¿No me puede dejar un día tranquilo?"
                jump menu_habitacion
            
            "Examinar el boceto":
                $ boceto_visto = True
                "Examinás el boceto a mano del local de comida."
                fran "Ojalá algún día se haga realidad. Solo necesito juntar para arrancar; lo demás viene solo."
                jump menu_habitacion
            
            "Usar la computadora":
                jump submenu_computadora
    
    label submenu_computadora:
    fran "(Tengo que ponerme a buscar laburo.)"
    
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

                "Requisito: dos años de experiencia."
                "Rechazado."

                show fran_normal

                fran "Si nadie te contrata, ¿cómo vas a juntar experiencia?"

                hide fran_normal

                jump menu_trabajos

            "Buscar trabajo de repartidor" if not repartidor_visto:

                $ repartidor_visto = True

                "Requisito: moto propia."
                "Rechazado."

                show fran_normal

                fran "Era obvio. Tampoco iba a repartir las pizzas corriendo."

                hide fran_normal

                jump menu_trabajos

            "Buscar trabajo de ayudante de cocina" if not ayudante_visto:

                $ ayudante_visto = True

                "Página saturada. Todas las postulaciones fueron rechazadas."
                
                show fran_normal

                fran "Y eso que algo me había enseñado Hana."
                fran "Se ve que todos buscan laburo."

                hide fran_normal

                jump menu_trabajos
        

        show fran_triste with dissolve

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
                
                "Táper de María":
                    show fran_normal
                    fran "Si anoche comí, fue gracias a María."
                    fran "Tengo que devolverle el táper."
                    hide fran_normal
                    jump menu_cocina
                
                "Mate":
                    jump sub_menu_mate
            
        label sub_menu_mate:
            menu:
                "Preparar mate":
                    "Francisco se termina la poca yerba que le quedaba."
                    show fran_triste
                    fran "Ya ni para la yerba me alcanza."
                    fran "Si no fuera por María, me moría de hambre."
                    
                    #Golpes
                    hide fran_triste
                    show fran_normal

                    fran "¿Quién golpea?"

                    hide fran_normal
                    
                    jump acto1_escena5

                "Todavía no":
                        jump menu_cocina    

    #Acto 1 - Escena 5

    label acto1_escena5:


        label menu_conocer:
            scene hab_int
            menu:
                "Facturas":
                    show fran_normal
                    fran "Luz, gas, internet... se me juntan todas."
                    hide fran_normal
                    jump menu_conocer
                
                "Puerta de salida":
                    jump sub_menu_conocer
        
        label sub_menu_conocer:
            scene hab_int
            menu:
                "Atender la puerta":
                    show mar_alivio
                    ma "¡Hola, Fran! Vengo a buscar el táper."
                    hide mar_alivio

                    show fran_normal
                    fran "Hola Mari. Gracias por la cena, de verdad. ¿Pasás?"
                    fran "Hice unos mates."
                    hide fran_normal

                    show mar_normal
                    ma "Dale. ¿Cómo andás con la búsqueda?"
                    hide mar_normal

                    show fran_triste
                    fran "Mal. No sale nada y las facturas se me apilan."
                    fran "¿Y vos en el laburo?"
                    hide fran_triste

                    show mar_preo
                    ma "No es lo que más me gusta, pero me alcanza para el tratamiento de mi papá."
                    hide mar_preo
                    show mar_alivio
                    ma "No te castigues tanto. Salí a dar una vuelta, despejate."
                    ma "Y te dejo torta para después."
                    hide mar_alivio

                "Todavía no":
                    jump acto1_escena5

        "María agarra su táper, deja otro con torta sobre la mesa y se va."

        show fran_normal

        fran "Bueno, debería hacerle caso a Mari, después de terminarme el termo."

    label acto1_escena6:

        scene calle with dissolve

        show fran_triste

        fran "Capaz pueda vender algo de ropa."
        fran "Ya no se me ocurre nada."

        hide fran_triste

        "Francisco ve gente amontonada frente a un poste."
        "Cuando se acerca, se dispersan y queda a la vista un cartel."

        "¿Necesitás plata? Clínica busca voluntarios para tratamiento experimental. Excelente paga."
        show fran_sorpresa
        fran "Justo cuando necesito plata..."
        fran "Queda a unas cuadras."
        fran "Paso a ver."

    label acto1_escena7:

        scene centro with hpunch

        "Un candidato sale apurado, casi lo choca."

        cand "¡Está loco ese tipo! Nadie va a aceptar hacerse eso."

        show fran_triste

        fran "Se nota que él no necesita plata. El alquiler no se paga solo."

    label acto1_escena8:

        scene consultorio with dissolve

        show fran_normal

        fran "Buen día, vengo por el anuncio..."

        hide fran_normal

        "Aparece el Dr. Malandra y le pone un cuestionario en las manos."

        show doc_normal

        doc "Qué bueno que llegaste. Completame esto."

        hide doc_normal

        "¿Vivis solo?"
        "Si, vivo solo"

        "¿Alguien notaría si no te ve por un tiempo?"
        "Nadie lo notaría."

        "Del 1 al 10, ¿cuánto te importa lo que piense la gente?"
        #renpy.input("Del 1 al 10, ¿cuánto te importa lo que piense la gente?", default="1")

        show doc_mani

        doc "¡Perfecto! Sos la persona ideal."
        doc "Estoy desarrollando un producto para el crecimiento capilar."

        hide doc_mani

        show doc_eno

        doc "Son tres aplicaciones y cobrás en cada una."
        doc "Por la primera, 6000 dólares."
        doc "Condiciones: no lavarte ni cortarte el pelo mientras dure el tratamiento, y no contarle a nadie."

        hide doc_eno

        show doc_normal

        doc "Si no cumplís, devolvés la plata y te embargo los bienes."
        doc "¿Aceptás?"

        hide doc_normal

        show fran_triste

        fran "Ahora entiendo al que se fue corriendo."

        hide fran_triste

        label menu_trato:
            menu:
                "Rechazar el trato":
                    jump acto1_escena9
                
                "Aceptar el trato":
                    jump acto1_escena12
    
    label acto1_escena9:

        scene consultorio

        show fran_normal

        fran "Es demasiado para mí."
        fran "Mejor lo dejamos acá."

        hide fran_normal
        
        show doc_eno

        doc "¡Es por la ciencia!"
        doc "Te estás perdiendo la oportunidad de tu vida."

        "Francisco vuelve caminando a su casa. Se le hace de noche."

        
    label acto1_escena10:
        scene hab_int


        show fran_triste

        fran "¿Hice bien? Con esa plata pagaba todo..."
        fran "y hasta capaz invitaba a María a comer algo."

        hide fran_triste

        "Mensaje del Dueño" 
        "Si el viernes no está la plata, buscate otro lugar."

        show fran_triste

        fran "Otra vez. No se cansa."

        hide fran_triste
    
    label acto1_escena11:

        scene hab_int

        "Mensaje del Dueño"
        "Fran, tengo una changa para vos."

        "Me das una mano y te descuento el alquiler."
        "¿Qué decís?"

        show fran_triste

        fran "Y bueno."
        fran "Si no queda otra."

        "Francisco contesta y se prepara para salir. Nada cambió."

        "FINAL NORMAL — TODO SIGUE IGUAL"
        "FIN"

        label menu_normal:
            menu:
                "Volver a la última decisión":
                    scene consultorio with dissolve
                    jump menu_trato


                "Salir al menú":
                    return
    
    label acto1_escena12:

        scene consultorio with dissolve

        "Francisco firma el contrato."

        show doc_mani

        doc "¡Perfecto!"
        doc "Primero, lavate la cabeza con esto."
        doc "No desperdicies ni una gota."

        hide doc_mani

        "Es un shampoo de manzana barato."
        "Después, el doctor le apunta con una secadora enorme mientras habla sin parar de fórmulas."

        show fran_normal

        fran "Con tanta palabrería y el secador no escuché nada."

        hide fran_normal

        show doc_mani

        doc "Ahora la crema. Solo se aplica acá, en ambiente estéril."

        hide doc_mani

        "El doctor le aplica la crema en el cuero cabelludo a Francisco, espera unos segundos y le pregunta."

        show doc_mani
        
        doc "¿Te pica?"
        doc "¿Sentís algo raro?"

        hide doc_mani

        show fran_normal

        fran "Nada."
        fran "¿Debería?"

        hide fran_normal

        show doc_normal

        doc "No, no. Solo dejame anotar."

        hide doc_normal

        "El doctor le mide la cabeza con reglas y lupas, saca un sobre grueso de un cajón y se lo da."

        "Recibiste USD 6000"

        show doc_normal

        doc "Nos vemos en una semana."
        doc "Nada de agua, nada de tijera"
        doc "y ni una palabra a nadie.."

        hide doc_normal

        show fran_sorpresa

        fran "¿Todo esto es para mí?"
        fran "Sí, sí… entendido."

        hide fran_sorpresa
        show fran_normal
        fran "Con esto pago todo y me sobra."
        fran "Mejor vuelvo en colectivo."
    



    

    


