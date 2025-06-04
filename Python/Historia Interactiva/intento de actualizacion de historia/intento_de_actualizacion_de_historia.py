print("Bienvenido al juego de aventuras")

print("Tu mision es encontrar a tu esposa desaparecida luego de que te llegara un mensaje de ella con su ubicacion.")
print("Al llegar a la ubicacion encuentras una casa en el bosque.")
while True:
    decision1 = input("Por donde intentas entrar? (puerta/ventana): ").strip().lower()
    # Ruta de la puerta
    if decision1 == "puerta":
        print ("La puerta esta cerrada")
        while True:
            decision2 = input("Quieres intentar forzarla o buscar otra entrada (forzar/Buscar): ").strip().lower()
            # ruta de forzar la puerta
            if decision2 == "forzar":
                 print ("Encuentras una llave inglesa con la que le das golpes a la cerradura hasta partirla.")
                 print ("Al pasar encuentras unas escaleras al segundo piso.")
                 while True:
                     decision3 = input("Deseas subir o investigar el primer piso (subir/quedarse): ").strip().lower()
                     # Ruta de explorar el primer piso
                     if decision3 == "quedarse":
                         print ("Iluminas con la linterna de tu celular y encuentras basura y comida podrida por toda la casa, revisas las habitaciones una por una hasta que encuentras a una mujer tirada en el piso.")
                         while True:
                             decision4 = input("Que haces al verla? (acercarse/irse): ").strip().lower()
                             if decision4 == "acercarse":
                                 print ("la miras bien y notas que es tu esposa, al acercarte ves que debajo de ella hay sangre fresca y una herida de bala, el encontrar a tu esposa muerta y saber que pudiste ayudarla si llegabas antes te hace tener un ataque de ansiedad y con un cuchillo que estaba tirado decides suicidarte para morir con ella.")
                                 print ("Bad ending.")
                                 exit()
                             elif decision4 == "irse":
                                 print ("decides que no vale la pena seguir buscando y huyes solo de el lugar.")
                                 print ("Bad ending.")
                                 exit()
                             else:
                                 print ("Desicion no valida, intente de nuevo.")
                                 # Ruta de subir al segundo piso
                     elif decision3 == "subir":
                         print ("al subir las escaleras te encuentras un pasillo con 2 puertas, una a la izquierda y otra a la derecha.")
                         while True:
                             decision5 = input("Que puerta abres? (izquierda/derecha): ").strip().lower()
                             # Ruta de la puerta izquierda
                             if decision5 == "izquierda":
                                 print ("encuentras un cuarto sucio y vacio, al revisar el armario encuentras una pistola y un mensaje de tu esposa que dice que la estan reteniendo en el sotano.")
                                 print ("Decides ir al sotano a buscarla.")
                                 while True:
                                     decision6 = input("al bajar al sotano en silencio encuentras a un hombre amenazando a tu mujer, que haras? (disparar/esperar): ").strip().lower()
                                     if decision6 == "disparar":
                                         print ("Disparas al hombre y logras salvar a tu esposa, ambos escapan de la casa y llaman a la policia.")
                                         print ("Good ending.")
                                         exit()
                                     elif decision6 == "esperar":
                                         print ("El hombre te ve y te dispara, mueres en el acto.")
                                         print ("Bad ending.")
                                         exit()
                                     else:
                                         print ("Desicion no valida, intente de nuevo.")
                                         # Ruta de la puerta derecha
                             elif decision5 == "derecha":
                                 print ("encuentras un cuarto con una cama y una ventana, al acercarte a la ventana ves que hay un hombre mirando hacia la casa, al verte te apunta con un arma y te dispara, mueres en el acto.")
                                 print ("Bad ending.")
                                 exit()
                             else:
                                 print ("Desicion no valida, intente de nuevo.") 
                     else:
                         print ("Desicion no valida, intente de nuevo.")
            elif decision2 == "buscar":
                 print ("Decides buscar otra entrada y encuentras una ouerta trasera abierta.")
                 while True:
                     decision7 = input("al entrar encuentras la entrada a un sotano y un pasillo al resto de la casa, que haras?(sotano/pasillo): ").strip().lower()
                     # Ruta de entrar al sotano
                     if decision7 == "sotano":
                         while True:
                             decision15 = input("Al entrar al sotano encuentras a tu esposa atada y amordazada, que haces al verla? (desatar/revisar): ").strip().lower()
                             if decision15 == "desatar":
                                   print ("Al acercarte a ella intentas desatarla pero alguien te toma por la espalda y te da un tiro acabando con tu vida.")
                                   print ("Bad ending.")
                                   exit()
                             elif decision15 == "revisar":
                                  print ("Al revisar el sotano encuentras un hombre escondido que te ataca, logras defenderte pero quitandole la pistola y matandolo para desatar a tu esposa y huir.")
                                  print ("Good ending.")
                                  exit()
                             else:
                                  print ("Desicion no valida, intente de nuevo.")
                                  # Ruta de explorar la casa
                     elif decision7 == "pasillo":
                         print ("avanzas por el pasillo y exploras la casa, al no encontrar nada vuelves al inicio donde ver a un hombre con un arma, intentas huir pero el hombre te dispara y mueres.")
                         print ("Bad ending.")
                         exit()
                     else:
                         print ("Desicion no valida, intente de nuevo.")
            else:
                  print ("Desicion no valida, intente de nuevo.")   
                  # Ruta de la ventana
    elif decision1 == "ventana":
        while True:
            decision8 = input("Al entrar por la ventana escuchas un ruido en el segundo piso, que haces? (buscar/ignorar): ").strip().lower()
            # Ruta de ignorar el ruido
            if decision8 == "ignorar":
                print ("decides ignorar el ruido y seguir buscando, al revisar la casa encuentras todo desordenado como si la casa estuviera abandonada, al revisar la cocina encuentras un cuchillo y decides llevarlo contigo.")
                while True:
                    decision11 = input("al haber explorado todo el primer piso, que haces? (subir/ir al sotano): ").strip().lower()
                    # Ruta de subir al segundo piso
                    if decision11 == "subir":
                         print ("mientras subes te encuentras de frente con un hombre que te apunta con un arma, al intentar defenderte te dispara y mueres en el acto.")
                         print ("Bad ending.")
                         exit()
                         # Ruta de ir al sotano
                    elif decision11 == "ir al sotano":
                        while True:
                            decision10 = input("Al bajar al sotano no encuentras gran cosa, decides explorar en silecio hasta que escuchas un ruido, que haces? (investigar/esconderse): ").strip().lower()
                             # Ruta de investigar el ruido
                            if decision10 == "investigar":
                                 print ("Al investigar el ruido encuentras a un hombre que te ataca, este te amenaza con matar a tu esposa y te amarra junto a tu esposa, quedas cautivo.")
                                 print ("Bad ending")
                                 exit()
                                 # Ruta de esconderse
                            elif decision10 == "esconderse":
                                 print ("Al esconderte ves como un hombre entra al sotano junto a tu esposa amordazada, te acercas en silencio y le clavas el cuchillo en la espalda, el hombre cae al suelo y logras desatar a tu esposa, ambos escapan de la casa.")
                                 print ("Good ending.")
                                 exit()
                            else:
                                 print ("Desicion no valida, intente de nuevo.")
                                 # Ruta de buscar el ruido
            elif decision8 == "buscar":
                print ("decides subir corriendo y encuentras a un hombre amordazando a tu esposa, te acercas al hombre y le das un golpe en la cabeza con una lampara dejandolo inconsciente, desatas a tu esposa y ambos escapan de la casa.")
                print ("Good ending.")
                exit()
            else:
                print ("Desicion no valida, intente de nuevo.") 
    else:
        print ("Desicion no valida, intente de nuevo.")

    
        



                
                
           
            
               
                
            
                
                
   
        
        

    
