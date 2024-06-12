
from persona import Persona
from estudiante import Estudiante
from docente import Docente
from material import Material
from revista import Revista
from libro import Libro
from pedido import Pedido

def main():

    estudiante1 = Estudiante("123456", "Juan", "Pérez", "juan@example.com", "555-1234", "Calle A", 3, True, "Ingeniería")
    docente1 = Docente("987654", "María", "González", "maria@example.com", "555-5678", "Calle B", 5, True, "Matemáticas")
    libro1 = Libro("L001", "J.K. Rowling", "Harry Potter", 1997, "Salani", True, 10, "Tapa dura")
    revista1 = Revista("R001", "National Geographic", "Explorando el mundo", 2022, "NG", True, 50, "Ciencia")
    pedido1 = Pedido(1, estudiante1, [libro1, revista1], "Programación", "2024-05-26", "2024-06-02")


    print(estudiante1)
    print(docente1)
    print(libro1)
    print(revista1)
    print(pedido1)

if __name__ == "__main__":
    main()


