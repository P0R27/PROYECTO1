from persona import  Persona
class Estudiante(Persona):

    universidad = "Mi Universidad"

    def __init__(self, id, nivel, contador_estudiante, nombre, apellido):
        self._id = id
        self._nivel = nivel
        self._contador_estudiante = contador_estudiante
        self._nombre = nombre
        self._apellido = apellido


    @property
    def id(self):
        return self._id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel


    def pedir_libro(self):

        return True

    def devolver_libro(self):

        return True


    def __str__(self):
        return f"Estudiante {self._nombre} {self._apellido} (ID: {self._id})"


if __name__ == "__main__":
    estudiante1 = Estudiante(id=1, nivel=3, contador_estudiante=10,
                             nombre="Juan", apellido="Pérez")
    print(estudiante1)
    print(estudiante1.universidad)

