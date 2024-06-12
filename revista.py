

from material import Material


class Revista(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo


if __name__ == "__main__":
    revista1 = Revista(codigo="R001", autor="National Geographic", titulo="Explorando el mundo",
                       anio=2022, editorial="NG", disponible=True, cantidad_disponible=50, tipo="Ciencia")
    print(revista1)


