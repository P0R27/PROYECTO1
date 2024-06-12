class Material:
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, nueva_disponibilidad):
        self._disponible = nueva_disponibilidad

    def __str__(self):
        return f"Material: {self._titulo} ({self._anio}), Autor: {self._autor}, Disponible: {self._disponible}"


if __name__ == "__main__":
    material1 = Material(codigo="M001", autor="Autor Ejemplo", titulo="Título del Material",
                         anio=2023, editorial="Editorial X", disponible=True, cantidad_disponible=20)
    print(material1)


class Revista:
    pass


class Libro:
    pass