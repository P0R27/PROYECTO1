
from material import Material


class Libro(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo_pasta):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self._tipo_pasta = tipo_pasta

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, nuevo_tipo_pasta):
        self._tipo_pasta = nuevo_tipo_pasta


if __name__ == "__main__":
    libro1 = Libro(codigo="L001", autor="J.K. Rowling", titulo="Harry Potter", anio=1997,
                   editorial="Salani", disponible=True, cantidad_disponible=10, tipo_pasta="Tapa dura")
    print(libro1)





