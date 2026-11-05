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
                    show vineta heladera at vineta_pos with dissolve
                    fran_int "Tremendo banquete."
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
                    show vineta yerba at vineta_pos with dissolve
                    fran_int "Ya ni para la yerba me alcanza."
                    hide vineta
                    show fran_triste
                    with dissolve
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

        hide fran_triste
        hide mar_alivio
        show vineta taper at vineta_pos
        with dissolve

        pause 3.0

        hide vineta
        show fran_normal at izq
        with dissolve

        fran_int "Bueno, debería hacerle caso a Mari, después de terminarme el termo."

    label acto1_escena6:

        scene calle with dissolve

        show fran_triste with dissolve

        fran_int "Capaz pueda vender algo de ropa."
        fran_int "Ya no se me ocurre nada."

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

        scene candidato with dissolve
        with hpunch

        cand "¡Está loco ese tipo! Nadie va a aceptar hacerse eso."

        scene centro
        show fran_triste
        with dissolve

        fran_int "Se nota que él no necesita plata. El alquiler no se paga solo."

    label acto1_escena8:

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
                    scene consultorio
                    show fran_triste at izq
                    show doc_normal at der
                    with dissolve
                    jump menu_trato


                "Salir al menú":
                    return
    
    label acto1_escena12:

        hide fran_triste
        hide doc_normal
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

        show vineta sobre at vineta_pos with dissolve

        "Recibiste USD 6000"

        hide vineta
        show fran_normal at izq
        show doc_normal at der
        with dissolve

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

    #Acto 2

    label acto2_escena13:

        scene parada
        show fran_largo_normal
        with dissolve

        fran "Disculpá, ¿pasó hace mucho el 60?"

        per "Ya debe estar por venir."
        per "Che, qué pelo brilloso tenés."
        per "¿Qué te ponés?"

        hide fran_largo_normal
        show fran_largo_sorpresa
        with dissolve

        fran "¿Mi pelo? Shampoo de manzana."

        hide fran_largo_sorpresa
        show fran_largo_normal
        with dissolve

        fran_int "Si supiera…"

    label acto2_escena14:

        scene comedor_noche
        show fran_largo_normal
        with dissolve

        fran_int "Qué lindo es poder comprar comida."
        fran_int "La heladera se va a asustar."

        scene black with fade

        "Al día siguiente"

    label acto2_escena15:

        scene hab_int
        show fran_largo_normal
        with fade

        fran_int "Hace rato no dormía tan bien."

    label menu_habitacion_2:
        menu:
            "Ver el celular":

                scene mensaje_comprobante with dissolve

                fran_int "Por cómo me persigue, parece que le encanta apurarme."

                scene hab_int
                show fran_largo_normal
                with dissolve

                jump menu_habitacion_2

            "Examinar el boceto":

                scene boceto with dissolve

                "Meta para el local: USD 4000 / USD 30000"

                fran_int "Por fin este sueño no parece tan lejano."

                scene hab_int
                show fran_largo_normal
                with dissolve

                jump menu_habitacion_2

            "Puerta al comedor":
                menu:
                    "Ir al comedor":
                        jump acto2_escena16

                    "Todavía no":
                        jump menu_habitacion_2

    label acto2_escena16:

        scene comedor_dia
        show fran_largo_normal
        with dissolve

        fran_int "Tendría que aprovechar el día y salir a pasear un rato."

    label menu_escena16:
        menu:
            "Facturas pagadas":
                fran_int "Todas pagadas. Qué lindo es no preocuparse."

                jump menu_escena16

            "Puerta de salida":
                menu:
                    "Salir a pasear":
                        jump acto2_escena17

                    "Todavía no":
                        jump menu_escena16

    label acto2_escena17:

        scene calle
        show fran_largo_normal
        with dissolve

        fran_int "No lavarse ni cortarse el pelo..."
        fran_int "¿Y el cuerpo?"
        fran_int "Mejor no arriesgarme."

        fran "¡Buen día, vecino!"
        fran "Tome, cómprese una escoba nueva."

        vec "No, Fran, si todos sabemos que andás corto de plata."

        fran "Por fin me están saliendo las cosas."
        fran "Acépteme esto."

        # Provisorio: va frente a la pizzeria de dia (AR2-05)
        fran_int "Tengo que invitar a María a cenar."
        fran_int "¿Sushi, en honor a Hana? ¿O una buena pizza, que no falla nunca?"

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

        scene calle_atardecer
        with dissolve

        # Provisorio hasta tener las imagenes de los mensajes (AR2-08)
        "Mensaje de Francisco: ¡Hola, Mari! ¿Cenamos hoy? Invito yo, pido sushi."
        "Mensaje de María: ¿Vos invitando? ¿Quién sos y qué hiciste con Fran? Dale, a las 9."
        "Pedido confirmado — Combinado 30 piezas"

        show fran_largo_sorpresa with dissolve

        fran_int "¿Tanto sale? Bueno, es una ocasión especial."

    label acto2_escena19:

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "Traje agua con gas."
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

        fran "Hana siempre me lo decía."
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico."

        jump acto2_escena22

    label acto2_escena21:

        hide mar_normal
        show mar_det at der
        with dissolve

        ma "¡Jaja! ¡Comer esta obra de arte con tenedor es una falta de respeto!"

        fran "Tenés razón. Si Hana me viera..."
        fran "Ella y Kutetsu me cuidaron un año y medio cuando era chico."

        hide mar_det
        show mar_alivio at der
        with dissolve

        ma "Con más razón. Agarrá el palillo, dale."
        ma "El de abajo fijo, el de arriba aprieta."
        ma "Y antes de comer se dice \"itadakimasu\"."

    label acto2_escena22:

        hide mar_alivio
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

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_alivio at der
        with dissolve

        fran "Te propongo algo: cuando tenga mi local, la chef sos vos."

        ma "Mirá que los itamae no son baratos, eh."

        fran_int "Lo dije en joda… pero capaz no tanto."

        jump acto2_escena34

    #Ruta pizza

    label acto2_escena26:

        scene pizzeria
        with dissolve

        # Provisorio hasta tener las imagenes de los mensajes (AR2-08)
        "Mensaje de Francisco: Mari, ¿cenamos hoy? Invito una muzza."
        "Mensaje de María: ¿Vos invitando? Dale, a las 9. Llevo la gaseosa."

        show fran_largo_normal with dissolve

        fran_int "Una buena muzza nunca falla."

    label acto2_escena27:

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "Che, ¿te estás dejando el pelo largo?"
        ma "Te creció un montón en dos días."

        hide fran_largo_normal
        show fran_largo_sorpresa at izq
        with dissolve

        fran_int "¿Tanto se nota?"

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

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        ma "Te veo distinto. ¿En qué andás?"

        fran "Estoy juntando para abrir mi local de comida."

        hide mar_normal
        show mar_alivio at der
        with dissolve

        ma "¡Qué bueno, Fran! ¿Y de dónde sacaste la plata?"

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

        scene comedor_noche
        show fran_largo_normal at izq
        show mar_normal at der
        with dissolve

        fran "¿Y a vos cómo te va en la vida?"

        ma "En el laburo, como siempre. Mucho trabajo y poca plata."
        ma "Pero alcanza para lo de mi papá así que estamos bien."

    #Rutas juntas

    label acto2_escena34:

        scene hab_noche
        show fran_largo_normal
        with dissolve

        fran_int "Hacía mucho que no la pasaba tan bien."
        fran_int "Una aplicación más y estoy más cerca del local."

        scene black with fade

        "6 días después"

        scene hab_int
        show fran_largo_triste
        with fade

        fran_int "No aguanto esta picazón. Lo único que quiero es una ducha."
        fran_int "Bueno, a la clínica. ¿Cómo voy?"

    label menu_ida_clinica:
        menu:
            "En remís":
                jump acto2_escena35

            "En colectivo":
                jump acto2_escena36

    label acto2_escena35:

        scene calle
        show fran_largo_triste
        with dissolve

        rem "Uf… ¿no sentís olor a algo? Capaz es el motor."

        fran_int "No es el motor."

        jump acto2_escena37

    label acto2_escena36:

        scene parada
        show fran_largo_triste
        with dissolve

        pas "¿Sentiste el olor?"

        fran_int "¿Lo dicen por mí?"

    label acto2_escena37:

        scene consultorio
        show vineta medicion at vineta_pos
        with dissolve

        pause 2.0

        hide vineta
        show fran_largo_normal at izq
        show doc_mani at der
        with dissolve

        doc "¡Siete centímetros en siete días! ¿Picazón? ¿Olor? ¿Sueños raros?"

        fran "Todo eso, sí."

        hide fran_largo_normal
        hide doc_mani
        show vineta crema at vineta_pos
        with dissolve

        pause 2.0

        hide vineta
        show fran_largo_normal at izq
        show doc_normal at der
        with dissolve

        doc "Las condiciones siguen igual. Y la última paga es mucho mayor."

        hide fran_largo_normal
        show fran_largo_triste at izq
        with dissolve

        fran "Doctor, ¿no hay algo para la picazón? Aunque sea un perfume, porque la gente…"

        hide doc_normal
        show doc_shock at der
        with dissolve

        doc "¿Perfume? ¿Querés arruinar meses de trabajo? ¡Nada de nada!"
        doc "Tomá tu plata y andate, que me apestás el consultorio."

        "Recibiste USD 11000"

        scene centro
        show fran_largo_triste
        with dissolve

    label menu_vuelta_clinica:
        menu:
            "En colectivo":
                jump acto2_escena38

            "En remís":
                jump acto2_escena39

    label acto2_escena38:

        scene parada
        show fran_largo_triste
        with dissolve

    label menu_garita:
        menu:
            "Personas":
                fran "Disculpá, ¿pasó el 60?"

                per "No sé, no sé. Alejate, por favor."

                jump menu_garita

            "Asiento de la garita":
                col "No, no. Así no subís, recién limpiamos."

                jump acto2_escena40

    label acto2_escena39:

        per "¡Qué asco, bañate!"

        rem "No, maestro. Tengo el auto recién tapizado."

    label acto2_escena40:

        scene calle
        show fran_largo_triste
        with dissolve

        fran_int "Bueno. Caminando, entonces."

        # Efecto del pelo: se completa cuando este el sprite de pelo muy largo (P2-26)
        hide fran_largo_triste
        show fran_muy_sorpresa
        with Dissolve(1.5)

        fran_int "¿Qué…? ¡¿Qué me está pasando?!"

        ado "¡Miralo! ¡Parece un yeti! ¡Grabalo!"

        scene black with fade

    label acto2_escena41:

        scene comedor_dia
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

                fran_int "Por esto lo hago. Una aplicación más y es mío."

                scene hab_int
                show fran_muy_normal
                with dissolve

                jump menu_habitacion_encierro

            "Computadora":
                scene computadora with dissolve

                # Provisorio hasta tener la imagen del video (AR2-08)
                "Video: EL YETI DEL CONURBANO"
                "\"ese tipo necesita una ducha urgente\""
                "\"llamen a zoonosis\""

                show fran_muy_sorpresa with dissolve

                fran_int "¿Ese soy yo?"

                scene hab_int
                show fran_muy_normal
                with dissolve

                jump menu_habitacion_encierro

            "Puerta al comedor":
                jump acto2_escena41

    label acto2_escena43:

        scene bano
        show fran_muy_triste
        with dissolve

    label menu_bano:
        menu:
            "Espejo":
                fran_int "Ni yo me reconozco. Y el olor… y la picazón."

                jump menu_bano

            "Máquina de cortar pelo":
                fran_int "Dos minutos y se termina todo. Vuelvo a ser yo…"

                jump acto2_escena44

            "Puerta al comedor":
                jump acto2_escena41

    label acto2_escena44:

        scene comedor_dia
        with dissolve

        # Provisorio hasta tener la imagen del mensaje (AR2-08)
        "Mensaje de María: ¡Fran! Soy yo. Abrí, por favor."

        show fran_muy_triste at izq
        show mar_preo at der
        with dissolve

        ma "Eras vos… Vi el video. No te reconocí por la cara, sino por la campera."
        ma "¿Qué te pasó? Vení, dejame que te ayude a cortar ese pelo."

        fran_int "No le puedo contar nada. Si le cuento, rompo el trato."

    label menu_decision9:

        $ vuelta_final_malo = "menu_decision9"

        scene comedor_dia
        show fran_muy_triste at izq
        show mar_preo at der
        with dissolve

        menu:
            "Aceptar la ayuda":
                jump acto2_escena45

            "No decir nada y cerrarle la puerta":
                # Provisorio hasta que exista A3E46
                scene black with fade

                "Continúa en el Acto 3."

                return

    label acto2_escena45:

        show pelo_pantalla with Dissolve(1.5)

        ma "¡Fran! ¡Fran, contestame!"

        scene black with fade

    # A3E50 tiene que entrar por aca: el guion retoma desde el mensaje del doctor
    label final_malo_mensaje:

        # Provisorio hasta tener la imagen del mensaje (AR2-08)
        "Mensaje del Dr. Malandra: Usted rompió el contrato. No me hago responsable. Mis abogados se encargan del embargo."

        "FINAL MALO — EL YETI BONAERENSE"
        "FIN"

    label menu_final_malo:
        menu:
            "Volver a la última decisión":
                jump expression vuelta_final_malo

            "Salir al menú":
                return
