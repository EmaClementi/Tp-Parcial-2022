cancion1 =  {"Nombre": "NO VOY EN TREN", "Artista": "CHARLY GARCIA", "Letra": "No voy en tren, voy en avión. No necesito a nadie A nadie alrededor. No voy en tren, voy en avión. No necesito a nadie A nadie alrededor. Porque no hay nadie que mi piel resista. Porque no hay nadie que yo quiera ver. No veo televisión ni las revistas. No veo ya nada que no pueda ser. Por eso yo no voy en tren, voy en avión. No necesito a nadie A nadie alrededor. No voy en tren, voy en avión. No necesito a nadie A nadie alrededor. Cuando era niño nunca fuí muy listo. Tocaba el piano como un animal. Yo sé que algunos piensan que soy mixto. Pero yo tengo personalidad. Yo soy de la cruz del sur. Soy el que cierra y el que apaga la luz. Yo soy de la cruz del sur. Aquí y en everywhere. No voy en tren, voy en avión. No voy en tren, voy en avión."}
cancion2 =  {"Nombre": "DE MUSICA LIGERA", "Artista": "SODA STEREO", "Letra": " Ella durmió al calor de las masas, y yo desperté queriendo soñarla. Algún tiempo atrás pensé en escribirle que nunca sorteé las trampas del amor. De aquel amor de música ligera nada nos libra, nada más queda. Ella durmió al calor de las masas, y yo desperté queriendo soñarla. Algún tiempo atrás pensé en escribirle que nunca sorteé las trampas del amor. De aquel amor de música ligera nada nos libra, nada más queda. No le enviaré cenizas de rosas, ni pienso evitar un roce secreto. De aquel amor de música ligera nada nos libra, nada más queda. De aquel amor de música ligera nada nos libra, nada más queda, nada más. Nada más queda. Nada más queda. Nada más queda. Nada más queda." }
cancion3 =  {"Nombre": "UN POCO DE AMOR FRANCES", "Artista": "LOS REDONDOS", "Letra": " Una tipa rapaz como te gusta a vos. Esa tipa vino a consolarte. Un poco de amor francés no muerde su lengua, no. no es sincera pero te gusta oírla. Es una linda ración con un defecto, con uno o dos, y es un cóctel que no se mezcla solo. Quiere si quiere más. ya no la engatusas. es una copa de lo mejor cuando se ríe. El lujo es vulgaridad, dijo y me conquistó. de esa miel no comen las hormigas. Quiere si quiere más. ya no la engatusas. es una copa de lo mejor cuando se ríe."}
cancion4 =  {"Nombre": "COSTUMBRES ARGENTINAS", "Artista": "ABUELOS DE LA NADA", "Letra": "Muerdo el anzuelo y vuelvo a empezar de nuevo cada vez. Tengo en la mano una carta para jugar el juego cuando quieras. Caminando, caminándote, mi calle que quizás yo pueda cambiar. Esperando, esperándote, costumbres argentinas de decir no. El problema es otra vez la situación cada vez peor del corazón, yo camino todo y veo cada vez que quiero y te espero. Caminando, caminándote, mi calle que quizás yo pueda cambiar. Esperando, esperándote, costumbres argentinas de decir no." }
cancion5 =  {"Nombre": "JI JI JI", "Artista": "LOS REDONDOS", "Letra": " En este film velado en blanca noche el hijo tenaz de tu enemigo el muy verdugo cena distinguido una noche de cristal que se hace añicos. No lo soñé se enderezó y brindó a tu suerte No lo soñé y se ofreció mejor que nunca No mires por favor y no prendas la luz... la imagen te desfiguró. Este film da una imagen exquisita chicos son como bombas pequeñitas el mejor camino a la cueva del perico para tipos que no duermen por la noche. No lo soñé  Ibas corriendo a la deriva No lo soñé los ojos ciegos bien abiertos. El montaje final es muy curioso, es en verdad realmente entretenido vas en la oscura multitud desprevenido tiranizando a quienes te han querido." }
listaCanciones = [cancion1,cancion2,cancion3,cancion4,cancion5]

def verListaCanciones():
    print("LISTA DE CANCIONES")
    for cancion in listaCanciones:
        print("Nombre:",cancion["Nombre"],".","Artista:",cancion["Artista"])
def filtrarCanciones(opcion):
    for cancion in listaCanciones:
        if opcion == "nombre":
            print("Nombre:",cancion["Nombre"])
        elif opcion == "artista":
            print("Artista:",cancion["Artista"])
        elif opcion == "letra":
            print("Letra:",cancion["Letra"])
        else:
            print("La opcion ingresada no es correcta")

def buscarCancion(cancionAbuscar):
    for cancion in listaCanciones:
        if cancion["Nombre"] == cancionAbuscar:
            print("Nombre:",cancion["Nombre"],".","Artista:",cancion["Artista"])
            break
        else:
            print("La cancion no esta en la lista")
def agregarCancion():
    nombre = input("Ingrese el nombre de la cancion:")
    artista = input("Ingrese el nombre del artista:")
    letra = input("Ingrese la letra de la cancion:")
    nuevaCancion = {"Nombre": nombre,"Artista": artista,"Letra": letra}
    listaCanciones.append(nuevaCancion)
    verListaCanciones()

def modificarCancion(cancionAbuscar):
    for cancion in listaCanciones:
        if cancion["Nombre"] == cancionAbuscar:
            opcion = input("Que desea modificar? (Nombre)(Artista)(Letra):").lower()
            if opcion == "nombre":
                nombreNuevo = input("Ingrese el nuevo nombre:").upper()
                cancion["Nombre"] = nombreNuevo
                print("CANCION MODIFICADA: ","Nombre:",cancion["Nombre"],".","Artista:",cancion["Artista"],".","Letra:",cancion["Letra"])

            elif opcion == "artista":
                nuevoArtista = input("Ingrese el nuevo artista:").upper()
                cancion["Artista"] = nuevoArtista
                print("CANCION MODIFICADA: ","Nombre:",cancion["Nombre"],".","Artista:",cancion["Artista"],".","Letra:",cancion["Letra"])
                
            elif opcion == "letra":
                letraNueva = input("Ingrese la nueva letra:")
                cancion["Letra"] = letraNueva
                print("CANCION MODIFICADA: ","Nombre:",cancion["Nombre"],".","Artista:",cancion["Artista"],".","Letra:",cancion["Letra"])
            else:
                print("La opcion ingresada no es correcta")


