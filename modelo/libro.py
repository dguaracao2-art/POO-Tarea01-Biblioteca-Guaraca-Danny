class Libro:
    def __init__(self, isbn, titulo, autor):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._disponible = True

    @property
    def isbn(self):
        return self._isbn

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        self._disponible = False

    def devolver(self):
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self._isbn}] {self._titulo} - {self._autor} ({estado})"