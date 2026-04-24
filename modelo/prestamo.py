# modelo/prestamo.py

from modelo.libro import Libro
from modelo.estudiante import Estudiante


class Prestamo:
    """Representa un préstamo de un libro a un estudiante."""

    def __init__(self, libro: Libro, estudiante: Estudiante,
                 fecha_prestamo: str, fecha_devolucion: str):
        self._libro = libro
        self._estudiante = estudiante
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._activo = True

    @property
    def libro(self) -> Libro:
        return self._libro

    @property
    def estudiante(self) -> Estudiante:
        return self._estudiante

    @property
    def activo(self) -> bool:
        return self._activo

    def registrar_devolucion(self) -> None:
        """Marca el préstamo como devuelto y libera el libro."""
        self._activo = False
        self._libro.devolver()

    def __str__(self) -> str:
        estado = "ACTIVO" if self._activo else "DEVUELTO"
        return (f"Préstamo [{estado}]: {self._libro.titulo} → "
                f"{self._estudiante.nombre} {self._estudiante.apellido} | "
                f"Desde: {self._fecha_prestamo} | "
                f"Hasta: {self._fecha_devolucion}")