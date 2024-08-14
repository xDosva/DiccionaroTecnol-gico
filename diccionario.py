def crear_diccionario():
    """
    Crea un diccionario con 75 definiciones de términos relacionados con la programación y la informática.

    Returns:
        dict: Un diccionario donde las claves son términos y los valores son sus respectivas definiciones.
    """
    diccionario = {}
    
    # Función para agregar una entrada al diccionario
    def agregar_definicion(palabra, definicion):
        diccionario[palabra] = definicion
    
    # Agregamos 75 definiciones
    agregar_definicion("Python", "Un lenguaje de programación de alto nivel.")
    agregar_definicion("Variable", "Un espacio en memoria que almacena un valor.")
    agregar_definicion("Función", "Un bloque de código que realiza una tarea específica.")
    agregar_definicion("Lista", "Una colección ordenada de elementos en Python.")
    agregar_definicion("Diccionario", "Una estructura de datos en Python que almacena pares clave-valor.")
    agregar_definicion("Bucles", "Una estructura que repite una secuencia de instrucciones.")
    agregar_definicion("Condicional", "Una declaración que ejecuta código basado en una condición.")
    agregar_definicion("Iteración", "El proceso de repetir acciones en una estructura de bucle.")
    agregar_definicion("String", "Una secuencia de caracteres.")
    agregar_definicion("Entero", "Un número sin parte decimal.")
    agregar_definicion("Flotante", "Un número con parte decimal.")
    agregar_definicion("Booleano", "Un tipo de dato que puede ser True o False.")
    agregar_definicion("Clase", "Una plantilla para crear objetos en programación orientada a objetos.")
    agregar_definicion("Objeto", "Una instancia de una clase.")
    agregar_definicion("Herencia", "Un mecanismo donde una clase puede heredar atributos y métodos de otra clase.")
    agregar_definicion("Polimorfismo", "La capacidad de una función para tomar diferentes formas.")
    agregar_definicion("Encapsulamiento", "El concepto de agrupar datos y métodos que operan sobre esos datos en una sola unidad.")
    agregar_definicion("Módulo", "Un archivo que contiene código Python que se puede importar y reutilizar en otros programas.")
    agregar_definicion("Paquete", "Una colección de módulos organizados en un directorio.")
    agregar_definicion("Importar", "La acción de cargar un módulo en un programa Python.")
    agregar_definicion("Algoritmo", "Un conjunto de instrucciones para resolver un problema.")
    agregar_definicion("Compilador", "Un programa que traduce código de alto nivel a código máquina.")
    agregar_definicion("Intérprete", "Un programa que ejecuta código línea por línea.")
    agregar_definicion("Depuración", "El proceso de encontrar y corregir errores en el código.")
    agregar_definicion("Comentarios", "Líneas de texto en el código que no se ejecutan y sirven para explicar el código.")
    agregar_definicion("Indentación", "La práctica de alinear código para indicar estructuras lógicas en Python.")
    agregar_definicion("Excepción", "Un evento que ocurre durante la ejecución de un programa que interrumpe el flujo normal del código.")
    agregar_definicion("Try-except", "Una estructura para manejar excepciones en Python.")
    agregar_definicion("Argumentos", "Valores que se pasan a una función cuando se llama.")
    agregar_definicion("Parámetros", "Variables que se utilizan en la definición de una función para recibir argumentos.")
    agregar_definicion("Retorno", "El valor que una función devuelve después de su ejecución.")
    agregar_definicion("Lambda", "Una función anónima y pequeña en Python.")
    agregar_definicion("Map", "Una función que aplica otra función a cada ítem de una lista.")
    agregar_definicion("Filter", "Una función que filtra elementos de una lista según una condición.")
    agregar_definicion("Reduce", "Una función que aplica una función binaria acumulativa a los elementos de una lista.")
    agregar_definicion("Comprensión de listas", "Una forma concisa de crear listas en Python.")
    agregar_definicion("Generador", "Una función que devuelve un iterador en lugar de una lista completa.")
    agregar_definicion("Yield", "Una declaración que pausa una función generadora y devuelve un valor.")
    agregar_definicion("Range", "Una función que genera una secuencia de números.")
    agregar_definicion("Enumerate", "Una función que devuelve un iterador con índice y valor de una lista.")
    agregar_definicion("Zip", "Una función que combina dos o más iterables en un solo iterador.")
    agregar_definicion("Set", "Una colección no ordenada de elementos únicos en Python.")
    agregar_definicion("Tupla", "Una colección ordenada e inmutable de elementos.")
    agregar_definicion("Frozenset", "Una versión inmutable de un conjunto.")
    agregar_definicion("Slice", "Un objeto que define un segmento de una secuencia.")
    agregar_definicion("Mutable", "Un objeto que puede ser modificado después de su creación.")
    agregar_definicion("Inmutable", "Un objeto que no puede ser modificado después de su creación.")
    agregar_definicion("Recursión", "Una técnica donde una función se llama a sí misma.")
    agregar_definicion("Base de datos", "Un sistema organizado para almacenar, gestionar y recuperar información.")
    agregar_definicion("SQL", "Un lenguaje de consulta utilizado para interactuar con bases de datos relacionales.")
    agregar_definicion("API", "Un conjunto de definiciones y protocolos para construir e integrar software de aplicaciones.")
    agregar_definicion("JSON", "Un formato de texto ligero para el intercambio de datos.")
    agregar_definicion("XML", "Un lenguaje de marcado utilizado para almacenar y transportar datos.")
    agregar_definicion("HTML", "El lenguaje de marcado estándar para crear páginas web.")
    agregar_definicion("CSS", "Un lenguaje de hojas de estilo utilizado para describir la presentación de un documento escrito en HTML o XML.")
    agregar_definicion("JavaScript", "Un lenguaje de programación que se utiliza para crear contenido dinámico en páginas web.")
    agregar_definicion("Framework", "Una estructura reutilizable que proporciona una base para desarrollar software.")
    agregar_definicion("Librería", "Un conjunto de funciones y módulos que pueden ser utilizados por un programa.")
    agregar_definicion("Git", "Un sistema de control de versiones distribuido.")
    agregar_definicion("Repositorio", "Un espacio de almacenamiento donde se guarda un proyecto de software.")
    agregar_definicion("Commit", "Una acción en Git que guarda cambios en el repositorio.")
    agregar_definicion("Branch", "Una línea de desarrollo independiente en Git.")
    agregar_definicion("Merge", "La acción de combinar cambios de diferentes ramas en Git.")
    agregar_definicion("Pull Request", "Una solicitud para revisar e integrar cambios en el código.")
    agregar_definicion("DevOps", "Un conjunto de prácticas que combina el desarrollo de software y la administración de sistemas.")
    agregar_definicion("Cloud Computing", "La entrega de servicios de computación a través de internet.")
    agregar_definicion("Virtualización", "La creación de una versión virtual de un recurso físico, como un servidor o un sistema operativo.")
    agregar_definicion("Docker", "Una plataforma de contenedores que automatiza la implementación de aplicaciones.")
    agregar_definicion("Kubernetes", "Un sistema de orquestación de contenedores para automatizar la administración de aplicaciones en contenedores.")
    agregar_definicion("Microservicios", "Un enfoque de arquitectura de software donde una aplicación se estructura como un conjunto de servicios pequeños e independientes.")
    agregar_definicion("Machine Learning", "Un campo de la inteligencia artificial que permite a las máquinas aprender de los datos.")
    agregar_definicion("Inteligencia Artificial", "La simulación de procesos de inteligencia humana por parte de sistemas informáticos.")
    agregar_definicion("Red Neuronal", "Un modelo de computación inspirado en el cerebro humano que se utiliza en el aprendizaje automático.")
    agregar_definicion("Big Data", "Conjuntos de datos extremadamente grandes que pueden analizarse computacionalmente para revelar patrones, tendencias y asociaciones.")
    agregar_definicion("Blockchain", "Una estructura de datos descentralizada que se utiliza para mantener un libro mayor digital seguro y transparente.")

    return diccionario

# Crear el diccionario
mi_diccionario = crear_diccionario()

# Menú principal
while True:
    print("\nDiccionario de Programación")
    print("1. Buscar una definición")
    print("2. Mostrar todas las definiciones")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        termino = input("Introduce el término que deseas buscar: ")
        definicion = mi_diccionario.get(termino, "Término no encontrado.")
        print(f"\n{termino}: {definicion}")
    
    elif opcion == '2':
        print("\nTodas las definiciones:")
        for palabra, definicion in mi_diccionario.items():
            print(f"{palabra}: {definicion}")
    
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
