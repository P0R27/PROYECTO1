from persona import Persona
class Docente (Persona):

    universidad = "Mi Universidad"

    def __init__(self, id, titulo_3er_nivel, titulo_4to_nivel, contador_docente):
        self._id = id
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        self._contador_docente = contador_docente

    @property
    def id(self):
        return self._id

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, nuevo_titulo):
        self._titulo_3er_nivel = nuevo_titulo


    def pedir_libro(self):

        return True

    def devolver_libro(self):

        return True


    def __str__(self):
        return f"Docente (ID: {self._id}, Título 3er nivel: {self._titulo_3er_nivel})"


if __name__ == "__main__":
    docente1 = Docente(id=101, titulo_3er_nivel="Doctor en Educación", titulo_4to_nivel="Ph.D.", contador_docente=20)
    print(docente1)
    print(docente1.universidad)
