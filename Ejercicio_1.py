class Persona:
    def __init__(self, nombre, apellido, documento_identidad, anio_nacimiento):

        """
        Constructor de la clase Persona (Diagrama de clases)

        Parámetros:
        - nombre (str): Nombre de la persona.
        - apellido (str): Apellido de la persona.
        - documento_identidad (str): Número del documento de identidad.
        - anio_nacimiento (int): Año de nacimiento de la persona.
        """

        self.nombre = nombre
        self.apellido = apellido
        self.documento_identidad = documento_identidad
        self.anio_nacimiento = anio_nacimiento

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Número de documento de identidad:", self.documento_identidad)
        print("Año de nacimiento:", self.anio_nacimiento)
        print()  # Línea en blanco para separar registros y que salga lindo


def main():
    persona1 = Persona("Pedro", "Perez", "1053121010", 1998)
    persona2 = Persona("Luis", "Leon", "1053223344", 2001)

    persona1.imprimir_datos()
    persona2.imprimir_datos()

if __name__ == "__main__":
    main()
