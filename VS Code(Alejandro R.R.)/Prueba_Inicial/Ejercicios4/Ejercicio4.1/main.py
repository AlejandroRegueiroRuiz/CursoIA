import trabajador as trabajadores
import datetime
import csv

# Función que valida si una fecha es válida en formato 'YYYY-MM-DD'.
def validar_fecha(fecha_str):
    """
    Valida si la cadena de texto proporcionada es una fecha válida en formato 'YYYY-MM-DD'.
    
    Args:
        fecha_str (str): La fecha a validar.

    Returns:
        bool: True si la fecha es válida, False si no lo es.
    """
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Función para añadir un trabajador a las listas de médicos o enfermeras.
def añadirTrabajador(listaMed, listaEnf):
    """
    Permite al usuario añadir un nuevo trabajador (médico o enfermera) a las listas correspondientes.
    
    Args:
        listaMed (list): Lista de médicos en el hospital.
        listaEnf (list): Lista de enfermeras en el hospital.
    """
    tipo = input("Quieres añadir un médico o una enfermera(M/E)? ")
    while tipo.upper() not in ["M", "E"]:
        print("Error al introducir el tipo")
        tipo = input("Quieres añadir un médico o una enfermera(M/E)? ")

    nif = input("Introduce el nif: ")
    
    # Comprobar si el NIF ya existe en las listas de médicos o enfermeras
    while any(medico.nif == nif for medico in listaMed) or any(enfermera.nif == nif for enfermera in listaEnf) or len(nif) != 9:
        print("Error: El NIF ya existe o el nif introducido es un nif inválido.")
        nif = input("Introduce el nif nuevamente: ")

    nombre = input("Introduce tu nombre completo: ")

    fechaNac = input("Introduce la fecha de nacimiento(aaaa-mm-dd): ")
    while validar_fecha(fechaNac) == False:
        print("Error al introducir la fecha de nacimiento")
        fechaNac = input("Introduce la fecha de nacimiento(aaaa-mm-dd): ")

    sexo = input("Introduce el sexo(H/M): ")
    while sexo.upper() not in ["H", "M"]:
        print("Error al introducir el sexo")
        sexo = input("Introduce el sexo(H/M): ")

    n_col = input("Introduce el número de colegiado(Opcional): ")

    if tipo == "M":
        espec = input("Introduce la especialidad: ")
        fechaAlta = input("Introduce la fecha de alta: ")
        medico = trabajadores.Medico(nif, nombre, fechaNac, sexo, n_col, espec, fechaAlta)
        listaMed.append(medico)
    else:
        areaTrabajo = input("Introduce el área de trabajo: ")
        n_persona_a_cargo = input("Introduce el número de personas a cargo: ")
        enfermera = trabajadores.Enfermera(nif, nombre, fechaNac, sexo, n_col, areaTrabajo, n_persona_a_cargo)
        listaEnf.append(enfermera)

# Función para borrar un trabajador (médico o enfermera) de las listas.
def borrarTrabajador(listaMed, listaEnf, nif):
    """
    Elimina un trabajador (médico o enfermera) de las listas según el NIF proporcionado.

    Args:
        listaMed (list): Lista de médicos.
        listaEnf (list): Lista de enfermeras.
        nif (str): El NIF del trabajador a eliminar.
    """
    for medico in listaMed:
        if medico.nif == nif:
            listaMed.remove(medico)

    for enfermera in listaEnf:
        if enfermera.nif == nif:
            listaEnf.remove(enfermera)

# Función para mostrar todos los trabajadores en las listas de médicos y enfermeras.
def mostrarTrabajadores(listaMed, listaEnf):
    """
    Muestra la información de todos los trabajadores del hospital, médicos y enfermeras.

    Args:
        listaMed (list): Lista de médicos.
        listaEnf (list): Lista de enfermeras.
    """
    for medico in listaMed:
        trab = trabajadores.Medico.mostrarDatos(medico)
        print(trab)
    for enfermera in listaEnf:
        trab = trabajadores.Enfermera.mostrarDatos(enfermera)
        print(trab)

# Función para mostrar los detalles de un trabajador especificado por su NIF.
def mostrarDetallesTrabajador(listaMed, listaEnf, nif):
    """
    Muestra los detalles de un trabajador específico según su NIF.

    Args:
        listaMed (list): Lista de médicos.
        listaEnf (list): Lista de enfermeras.
        nif (str): El NIF del trabajador.
    """
    for medico in listaMed:
        if medico.nif == nif:
            trab = trabajadores.Medico.mostrarDatos(medico)
            print(trab)

    for enfermera in listaEnf:
        if enfermera.nif == nif:
            trab = trabajadores.Enfermera.mostrarDatos(enfermera)
            print(trab)

# Función para mostrar la experiencia laboral de un médico, en años.
def mostrarExperienciaMedico(listaMed, nif):
    t=""
    """
    Muestra los años de experiencia de un médico calculados desde su fecha de inicio.

    Args:
        listaMed (list): Lista de médicos.
        nif (str): El NIF del médico.
    """
    for medico in listaMed:
        if medico.nif == nif:
            inicio = trabajadores.Medico.devolverFechaInicio(medico)
            inicio = inicio.split('-')

            ano = int(inicio[0])
            mes = int(inicio[1])
            dia = int(inicio[2])

            dif = datetime.datetime.now() - datetime.datetime(ano, mes, dia)
            dif = dif.days
            t = f"\nTiene {dif // 365} años de experiencia en el sector"
            break
    if t == "":
        print("\nEste médico no trabaja en este hospital")
    else:
        print(t)
        

# Función para mostrar el número de personas a cargo de una enfermera.
def mostrarPersonas_a_Cargo(listaEnf, nif):
    t=""
    """
    Muestra el número de personas a cargo de una enfermera.

    Args:
        listaEnf (list): Lista de enfermeras.
        nif (str): El NIF de la enfermera.
    """
    for enfermera in listaEnf:
        if enfermera.nif == nif:
            personas = trabajadores.Enfermera.devolverPersonas_a_Cargo(enfermera)
            t = f"\nTiene {personas} personas a su cargo"
            break
    if t == "":
        print("\nEsta enfermera no trabaja en este hospital")
    else:
        print(t)

# Función para añadir personas a cargo de una enfermera.
def añadirPersonas_a_Cargo(listaEnf, nif):
    t=""
    """
    Añade personas al número de personas a cargo de una enfermera.

    Args:
        listaEnf (list): Lista de enfermeras.
        nif (str): El NIF de la enfermera.
    """
    for enfermera in listaEnf:
        if enfermera.nif == nif:
            personas = trabajadores.Enfermera.devolverPersonas_a_Cargo(enfermera)
            print(f"Tiene {personas} personas a su cargo")
            anadidos = int(input("Cuántas personas quieres añadir? "))
            enfermera.num_personas_a_cargo = int(enfermera.num_personas_a_cargo) + anadidos

    if t == "":
        print("\nEsta enfermera no trabaja en este hospital")

# Función para reducir el número de personas a cargo de una enfermera.
def quitarPersonas_a_Cargo(listaEnf, nif):
    t=""
    """
    Reduce el número de personas a cargo de una enfermera.

    Args:
        listaEnf (list): Lista de enfermeras.
        nif (str): El NIF de la enfermera.
    """
    for enfermera in listaEnf:
        if enfermera.nif == nif:
            personas = trabajadores.Enfermera.devolverPersonas_a_Cargo(enfermera)
            print(f"\nTiene {personas} personas a su cargo")
            anadidos = int(input("\nCuántas personas quieres quitar? "))
            enfermera.num_personas_a_cargo = int(enfermera.num_personas_a_cargo) - anadidos

    if t == "":
        print("\nEste médico no trabaja en este hospital")
    else:
        print(t)

# Función para guardar los datos de médicos y enfermeras en archivos CSV.
def guardarDatosCSV(listaMed, listaEnf):
    """
    Guarda los datos de los médicos y enfermeras en archivos CSV.

    Args:
        listaMed (list): Lista de médicos.
        listaEnf (list): Lista de enfermeras.
    """
    cabeceras_medicos = ["NIF", "Nombre", "Fecha de Nacimiento", "Sexo", "Número Colegiado", "Especialidad", "Fecha de Inicio"]
    cabeceras_enfermeras = ["NIF", "Nombre", "Fecha de Nacimiento", "Sexo", "Número Colegiado", "Área de Trabajo", "Número de Personas a Cargo"]

    ficheroMed = input("\nIntroduce el nombre que quieres que tenga el fichero donde se van a guardar los médicos: ")

    with open(ficheroMed, mode="w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(cabeceras_medicos)
        for medico in listaMed:
            escritor_csv.writerow(medico.devolverDatos())

    ficheroEnf = input("\nIntroduce el nombre que quieres que tenga el fichero donde se van a guardar las enfermeras: ")

    with open(ficheroEnf, mode="w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(cabeceras_enfermeras)
        for enfermera in listaEnf:
            escritor_csv.writerow(enfermera.devolverDatos())

# Función para cargar los datos de médicos y enfermeras desde archivos CSV.
def cargarDatosCSV(listaMed, listaEnf):
    """
    Carga los datos de médicos y enfermeras desde archivos CSV.

    Args:
        listaMed (list): Lista de médicos.
        listaEnf (list): Lista de enfermeras.
    """
    ficheroMed = input("Introduce el nombre del fichero de médicos: ")
    ficheroEnf = input("Introduce el nombre del fichero de enfermeras: ")

    try:
        with open(ficheroMed, mode="r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Ignorar la primera línea (cabecera)
            for fila in lector_csv:
                nif = fila[0]
                nombre = fila[1]
                fecha_nacimiento = fila[2]
                sexo = fila[3]
                num_colegiado = int(fila[4])
                especialidad = fila[5]
                fecha_inicio = fila[6]
                medico = trabajadores.Medico(nif, nombre, fecha_nacimiento, sexo, num_colegiado, especialidad, fecha_inicio)
                listaMed.append(medico)
    except FileNotFoundError:
        print("No se encontró el archivo de médicos.")

    try:
        with open(ficheroEnf, mode="r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Ignorar la primera línea (cabecera)
            for fila in lector_csv:
                nif = fila[0]
                nombre = fila[1]
                fecha_nacimiento = fila[2]
                sexo = fila[3]
                num_colegiado = int(fila[4])
                area_trabajo = fila[5]
                num_personas_a_cargo = int(fila[6])
                enfermera = trabajadores.Enfermera(nif, nombre, fecha_nacimiento, sexo, num_colegiado, area_trabajo, num_personas_a_cargo)
                listaEnf.append(enfermera)
    except FileNotFoundError:
        print("No se encontró el archivo de enfermeras.")

# Función principal que implementa el menú de gestión del hospital.
def menu():
    """
    Muestra un menú interactivo para gestionar la lista de trabajadores (médicos y enfermeras) del hospital.
    Permite realizar diversas operaciones como añadir, borrar, mostrar y cargar/trabajar con datos de trabajadores.
    """
    listaMed = []  # Lista de médicos.
    listaEnf = []  # Lista de enfermeras.
    while True:
        print("\nGestión de los trabajadores del hospital")
        print("1.  Añadir trabajador")
        print("2.  Borrar trabajador")
        print("3.  Mostrar lista de trabajadores")
        print("4.  Mostrar detalle de un trabajador")
        print("5.  Mostrar número de años trabajados de un médico")
        print("6.  Mostrar número de personas a cargo de una enfermera")
        print("7.  Añadir personas a cargo de una enfermera")
        print("8.  Reducir personas a cargo de una enfermera")
        print("9.  Guardar datos en .csv")
        print("10. Cargar datos de .csv")
        print("11. Salir\n")
        
        opcion = input("Elige una opción (1-11): ")

        # Acciones asociadas a cada opción del menú
        if opcion == "1":
            añadirTrabajador(listaMed, listaEnf)
        elif opcion == "2":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            borrarTrabajador(listaMed, listaEnf, nif)
        elif opcion == "3":
            mostrarTrabajadores(listaMed, listaEnf)
        elif opcion == "4":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            mostrarDetallesTrabajador(listaMed, listaEnf, nif)
        elif opcion == "5":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            mostrarExperienciaMedico(listaMed, nif)
        elif opcion == "6":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            mostrarPersonas_a_Cargo(listaEnf, nif)
        elif opcion == "7":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            añadirPersonas_a_Cargo(listaEnf, nif)
        elif opcion == "8":
            nif = input("Introduce el nif: ")
            while len(nif) != 9:
                print("Introduce el nif correctamente")
                nif = input("Introduce el nif: ")
            quitarPersonas_a_Cargo(listaEnf, nif)
        elif opcion == "9":
            guardarDatosCSV(listaMed, listaEnf)
        elif opcion == "10":
            cargarDatosCSV(listaMed, listaEnf)
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 11.")

# Punto de entrada principal al ejecutar el script.
if __name__ == "__main__":
    menu()


