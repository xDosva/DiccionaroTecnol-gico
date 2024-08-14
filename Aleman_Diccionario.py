def mostrar_menu():
    """
    Muestra el menú de opciones disponibles para el usuario.
    """
    print("\n--- Menú del Diccionario ---")
    print("1. Buscar una palabra")
    print("2. Listar todas las palabras")
    print("3. Salir")
 
def buscar_palabra(diccionario):
    """
    Permite al usuario buscar una palabra en el diccionario e imprimir su definición.
    Args:
        diccionario (dict): Un diccionario donde las claves son palabras y los valores son sus definiciones.
    """
    palabra = input("Ingrese la palabra que desea buscar: ").capitalize()
    if palabra in diccionario:
        print(f"{palabra}: {diccionario[palabra]}")
    else:
        print("La palabra no se encuentra en el diccionario.")
 
def listar_palabras(diccionario):
    """
    Imprime todas las palabras disponibles en el diccionario.
    Args:
        diccionario (dict): Un diccionario donde las claves son palabras.
    """
    print("\nLista de palabras:")
    for palabra in diccionario:
        print(f"- {palabra}")
 
def main():
    """
    Ejecuta el menú interactivo del diccionario, permitiendo al usuario buscar palabras,
    listar todas las palabras, o salir del programa.
    """
    diccionario = {
        "Abarcar": "Incluir o contener algo en un espacio o tiempo.",
        "Bizarro": "Extraño o raro en su comportamiento o apariencia.",
        "Cautivar": "Atraer o seducir de manera intensa.",
        "Desafiar": "Resistir o enfrentarse a algo con valentía.",
        "Eficaz": "Capaz de producir el efecto deseado.",
        "Fragancia": "Aroma agradable que emite algo.",
        "Generoso": "Que da o comparte con abundancia.",
        "Hábil": "Que tiene destreza o competencia en algo.",
        "Inquietante": "Que causa preocupación o intranquilidad.",
        "Jubiloso": "Lleno de alegría o regocijo.",
        "Luminiscencia": "Emisión de luz por un cuerpo sin calor.",
        "Majestuoso": "Grandeza que impresiona por su belleza.",
        "Nítido": "Claro y definido, sin borrosidad.",
        "Ocurrente": "Que tiene ideas o respuestas ingeniosas.",
        "Paciente": "Que muestra calma y tolerancia ante dificultades.",
        "Querencia": "Apegos o afectos profundos hacia un lugar.",
        "Resiliente": "Capaz de adaptarse y recuperarse rápidamente.",
        "Sutil": "Algo que es fino y delicado en su percepción.",
        "Tolerante": "Dispuesto a aceptar y respetar opiniones distintas.",
        "Útil": "Que tiene una función práctica y beneficiosa.",
        "Vibrante": "Que tiene una intensidad o vitalidad notable.",
        "Wagneriano": "Relativo o perteneciente a Richard Wagner o su estilo.",
        "Xenófobo": "Que muestra odio o desconfianza hacia los extranjeros.",
        "Yacer": "Estar acostado o reposar en un lugar.",
        "Zancada": "Paso largo y enérgico que se da al caminar.",
        "Ágil": "Capaz de moverse con rapidez y facilidad.",
        "Benevolente": "Que muestra buena voluntad y simpatía.",
        "Celestial": "Relacionado con el cielo o el firmamento.",
        "Diligente": "Que trabaja con esmero y cuidado.",
        "Efímero": "Que dura muy poco tiempo.",
        "Fascinante": "Que atrae y cautiva de manera intensa.",
        "Genuino": "Auténtico y verdadero, sin falsedad.",
        "Harmonioso": "Que tiene una combinación agradable y equilibrada.",
        "Intuitivo": "Que tiene la capacidad de entender o prever algo sin razonamiento consciente.",
        "Jubilación": "Estado de estar retirado de la actividad laboral por edad.",
        "Kinetico": "Relacionado con el movimiento o la energía.",
        "Lúdico": "Relacionado con el juego o el entretenimiento.",
        "Misterioso": "Que tiene algo enigmático y difícil de entender.",
        "Nostálgico": "Que siente melancolía por el pasado.",
        "Optativo": "Que se puede elegir o no.",
        "Pragmatico": "Enfocado en la práctica y la utilidad.",
        "Querubín": "Serafín o ángel de aspecto infantil y tierno.",
        "Racional": "Basado en la razón o el pensamiento lógico.",
        "Sempiterno": "Que dura para siempre o por un tiempo indefinido.",
        "Trascendente": "Que supera los límites ordinarios o terrenales.",
        "Urbano": "Relacionado con la ciudad o la vida citadina.",
        "Vivaz": "Que muestra energía y vitalidad.",
        "Wistful": "Que muestra un anhelo o nostalgia melancólica.",
        "Xilófono": "Instrumento musical de barras de madera.",
        "Yugular": "Que se refiere a la vena yugular, importante para la circulación sanguínea.",
        "Zeloso": "Que muestra gran dedicación y esmero en lo que hace.",
        "Átono": "Que carece de acento o intensidad en el lenguaje.",
        "Burlón": "Que se caracteriza por hacer bromas o mofarse.",
        "Compasivo": "Que muestra comprensión y simpatía hacia el sufrimiento ajeno.",
        "Dulzura": "Cualidad de ser dulce o amable.",
        "Ecléctico": "Que combina elementos diversos o variados.",
        "Frondoso": "Que tiene muchas hojas o ramas.",
        "Generosidad": "Acto de dar y compartir con nobleza.",
        "Harmonía": "Conjunto de elementos que combinan de manera agradable.",
        "Impetuoso": "Que actúa con prisa e impulsividad.",
        "Jubilación": "Estado de estar retirado del trabajo, normalmente por edad.",
        "Kafkiano": "Relacionado con el estilo o temática de Franz Kafka.",
        "Luminaria": "Objeto que da luz.",
        "Melancólico": "Que está afectado por la melancolía o tristeza.",
        "Nítido": "Que es claro y definido, sin manchas ni borrosidad.",
        "Opulento": "Que muestra riqueza o lujo.",
        "Precioso": "De gran valor por su belleza o rareza.",
        "Querencia": "Lugar donde uno se siente seguro o cómodo.",
        "Rítmico": "Que tiene un ritmo regular o cadencioso.",
        "Sublime": "De una belleza o perfección que inspira admiración.",
        "Tímido": "Que muestra falta de confianza en sí mismo o vergüenza.",
        "Urbano": "Que pertenece o está relacionado con la ciudad.",
        "Veloz": "Que se mueve a gran velocidad.",
        "Xenial": "Relativo a la hospitalidad y cordialidad hacia los huéspedes.",
        "Yermo": "Lugar deshabitado o sin vegetación.",
        "Zumbido": "Sonido continuo y monótono como el de un insecto."
    }
 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1/2/3): ")
        if opcion == "1":
            buscar_palabra(diccionario)
        elif opcion == "2":
            listar_palabras(diccionario)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del menú.")
 
if __name__ == "__main__":
    main()