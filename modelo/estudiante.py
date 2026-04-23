# modelo/estudiante.py

from modelo.persona import Persona


class Estudiante(Persona):
    """Estudiante universitario. Hereda de Persona."""

    def __init__(self, cedula: str, nombre: str, apellido: str, carrera: str):
        super().__init__(cedula, nombre, apellido)
        self._carrera = carrera

    @property
    def carrera(self) -> str:
        return self._carrera

    def __str__(self) -> str:
        return f"{super().__str__()} | Carrera: {self._carrera}"