from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Otros properties y setters para los demás atributos...

    @abstractmethod
    def pedir_libro(self):
        pass

    @abstractmethod
    def devolver_libro(self):
        pass

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._cedula})"

# Ejemplo de uso
class Estudiante(Persona):
    def pedir_libro(self):
        print(f"{self._nombre} está solicitando un libro.")

    def devolver_libro(self):
        print(f"{self._nombre} está devolviendo un libro.")

class Docente(Persona):
    def pedir_libro(self):
        print(f"{self._nombre} está solicitando un libro para la clase.")

    def devolver_libro(self):
        print(f"{self._nombre} está devolviendo un libro después de la clase.")


estudiante1 = Estudiante("123456", "Juan", "Pérez", "juan@example.com", "555-1234", "Calle A", 3, True, "Ingeniería")
docente1 = Docente("987654", "María", "González", "maria@example.com", "555-5678", "Calle B", 5, True, "Matemáticas")

print(estudiante1)
estudiante1.pedir_libro()
docente1.devolver_libro()

