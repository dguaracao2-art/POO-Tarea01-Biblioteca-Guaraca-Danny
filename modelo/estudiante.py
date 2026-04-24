from modelo.persona import Persona


class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, carrera):
        super().__init__(cedula, nombre, apellido)
        self._carrera = carrera

    @property
    def carrera(self):
        return self._carrera

    def __str__(self):
        return f"{super().__str__()} | Carrera: {self._carrera}"