from datetime import date

class Pedido:
    def __init__(self, id_pedido, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion):
        self._id_pedido = id_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._contador_pedido = 0

    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def solicitante(self):
        return self._solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @property
    def materia(self):
        return self._materia

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    def pedir_material(self, list_materia):

        self._contador_pedido += 1
        return f"Material pedido: {list_materia}, Pedido número: {self._contador_pedido}"

    def devolver_material(self):

        return "Material devuelto"

    def __str__(self):
        return f"Pedido {self._id_pedido} - Solicitante: {self._solicitante}, Material: {self._lista_material}"


if __name__ == "__main__":
    hoy = date.today()
    pedido1 = Pedido(id_pedido=1, solicitante="Estudiante Juan", lista_material="Libro Python",
                     materia="Programación", fecha_prestamo=hoy, fecha_devolucion=hoy)
    print(pedido1)
    print(pedido1.pedir_material("Libro Matemáticas"))
    print(pedido1.devolver_material())
