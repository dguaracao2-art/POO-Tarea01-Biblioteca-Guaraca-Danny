# modelo/persona.py

class Persona:
    """Clase base que representa a una persona."""

    def __init__(self, cedula: str, nombre: str, apellido: str):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido

    @property
    def cedula(self) -> str:
        return self._cedula

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    def __str__(self) -> str:
        return f"{self._cedula}: {self._nombre} {self._apellido}"