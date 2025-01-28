from abc import ABC
from datetime import datetime

class Trabajador(ABC):
    """
    Clase base para representar a un trabajador en general.
    Define atributos comunes como el NIF, nombre, fecha de nacimiento, sexo y número de colegiado.
    """
    def __init__(self, nif, nombre, fechaNac, sexo, n_Col=0):
        """
        Constructor de la clase Trabajador.

        Args:
            nif (str): Número de identificación fiscal del trabajador.
            nombre (str): Nombre completo del trabajador.
            fechaNac (str): Fecha de nacimiento del trabajador en formato 'YYYY-MM-DD'.
            sexo (str): Sexo del trabajador (por ejemplo, 'M' o 'F').
            n_Col (int, optional): Número de colegiado del trabajador. Por defecto es 0.
        """
        self.nif = nif
        self.nombre = nombre
        self.fechaNac = datetime.strptime(fechaNac, "%Y-%m-%d")
        self.sexo = sexo
        self.n_Col = n_Col


class Medico(Trabajador):
    """
    Clase para representar a un médico, que es una especialización de Trabajador.
    Añade atributos específicos como la especialidad y la fecha de inicio de ejercicio.
    """
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, num_colegiado, especialidad, fecha_inicio):
        """
        Constructor de la clase Medico.

        Args:
            nif (str): Número de identificación fiscal del médico.
            nombre (str): Nombre completo del médico.
            fecha_nacimiento (str): Fecha de nacimiento del médico en formato 'YYYY-MM-DD'.
            sexo (str): Sexo del médico (por ejemplo, 'M' o 'F').
            num_colegiado (int): Número de colegiado del médico.
            especialidad (str): Especialidad médica del médico.
            fecha_inicio (str): Fecha en la que el médico comenzó a ejercer, en formato 'YYYY-MM-DD'.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo, num_colegiado)
        self.especialidad = especialidad
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        
    def mostrarDatos(self):
        """
        Muestra los datos del médico en formato de texto.

        Returns:
            str: Información completa sobre el médico, como nombre, NIF, fecha de nacimiento, sexo, número de colegiado, especialidad y fecha de inicio.
        """
        return (f"Nombre: {self.nombre}, NIF: {self.nif}, Fecha de Nacimiento: {self.fechaNac.strftime('%Y-%m-%d')}, "
                f"Sexo: {self.sexo}, Nº Colegiado: {self.n_Col}, Especialidad: {self.especialidad}, "
                f"Fecha de Inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}")

    def devolverDatos(self):
        """
        Devuelve los datos del médico en forma de lista.

        Returns:
            list: Lista con los datos del médico (NIF, nombre, fecha de nacimiento, sexo, número de colegiado, especialidad, fecha de inicio).
        """
        return [self.nif, self.nombre, self.fechaNac.strftime("%Y-%m-%d"), self.sexo, self.n_Col, 
                self.especialidad, self.fecha_inicio.strftime("%Y-%m-%d")]

    def devolverFechaInicio(self):
        """
        Devuelve la fecha de inicio del médico en formato de cadena 'YYYY-MM-DD'.

        Returns:
            str: Fecha de inicio del médico.
        """
        return self.fecha_inicio.strftime("%Y-%m-%d")
    

class Enfermera(Trabajador):
    """
    Clase para representar a una enfermera, que es una especialización de Trabajador.
    Añade atributos específicos como el área de trabajo y el número de personas a cargo.
    """
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, num_colegiado, area_trabajo, num_personas_a_cargo):
        """
        Constructor de la clase Enfermera.

        Args:
            nif (str): Número de identificación fiscal de la enfermera.
            nombre (str): Nombre completo de la enfermera.
            fecha_nacimiento (str): Fecha de nacimiento de la enfermera en formato 'YYYY-MM-DD'.
            sexo (str): Sexo de la enfermera (por ejemplo, 'M' o 'F').
            num_colegiado (int): Número de colegiado de la enfermera.
            area_trabajo (str): Área en la que trabaja la enfermera (por ejemplo, 'Urgencias', 'Pediatría').
            num_personas_a_cargo (int): Número de personas que la enfermera tiene a su cargo.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo, num_colegiado)
        self.area_trabajo = area_trabajo
        self.num_personas_a_cargo = num_personas_a_cargo

    def mostrarDatos(self):
        """
        Muestra los datos de la enfermera en formato de texto.

        Returns:
            str: Información completa sobre la enfermera, como nombre, NIF, fecha de nacimiento, sexo, número de colegiado, área de trabajo y número de personas a cargo.
        """
        return (f"Nombre: {self.nombre}, NIF: {self.nif}, Fecha de Nacimiento: {self.fechaNac.strftime('%Y-%m-%d')}, "
                f"Sexo: {self.sexo}, Nº Colegiado: {self.n_Col}, Áreas de Trabajo: {self.area_trabajo}, "
                f"Número de personas a cargo: {self.num_personas_a_cargo}")

    def devolverDatos(self):
        """
        Devuelve los datos de la enfermera en forma de lista.

        Returns:
            list: Lista con los datos de la enfermera (NIF, nombre, fecha de nacimiento, sexo, número de colegiado, área de trabajo, número de personas a cargo).
        """
        return [self.nif, self.nombre, self.fechaNac.strftime("%Y-%m-%d"), self.sexo, self.n_Col, 
                self.area_trabajo, self.num_personas_a_cargo]
    
    def devolverPersonas_a_Cargo(self):
        """
        Devuelve el número de personas a cargo de la enfermera.

        Returns:
            int: Número de personas a cargo de la enfermera.
        """
        return self.num_personas_a_cargo
