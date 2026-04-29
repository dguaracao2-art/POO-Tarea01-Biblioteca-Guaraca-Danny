from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
from faker import Faker

fake = Faker()


def main():
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    print("── Registrando libros ──")

    
    libro1 = Libro("978-0-13-468599-1", "El Principito", "Antoine de Saint-Exupéry")
    #Creamos libros con Faker que da datos aleatorios
    libro2 = Libro(
        fake.isbn13(),
        fake.sentence(nb_words=3),
        fake.name()
    )

    libro3 = Libro(
        fake.isbn13(),
        fake.sentence(nb_words=4),
        fake.name()
    )

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    print("\n── Registrando estudiantes ──")

    # Usamos Faker para generar datos aleatorios de estudiantes
    est1 = Estudiante(
        fake.random_number(digits=10),
        fake.first_name(),
        fake.last_name(),
        "Ingeniería en Software"
    )

    est2 = Estudiante(
        fake.random_number(digits=10),
        fake.first_name(),
        fake.last_name(),
        "Ingeniería Industrial"
    )

    # 👇 Guardamos cédula para usar después
    cedula_est1 = est1.cedula
    cedula_est2 = est2.cedula

    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)

    print(f"\n{biblioteca}\n")

    print("── Realizando préstamos ──")

    resultado = biblioteca.prestar_libro(
        libro1.isbn, cedula_est1, fake.date(), fake.date()
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        libro2.isbn, cedula_est1, fake.date(), fake.date()
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        libro3.isbn, cedula_est2, fake.date(), fake.date()
    )
    print(resultado)

    print("\n── Intentando prestar libro ya prestado ──")

    resultado = biblioteca.prestar_libro(
        libro1.isbn, cedula_est2, fake.date(), fake.date()
    )
    print(resultado)

    print("\n── Préstamos activos del estudiante 1 ──")

    prestamos = biblioteca.consultar_prestamos_activos(cedula_est1)
    for prestamo in prestamos:
        print(f"  → {prestamo}")

    print("\n── Devolviendo un libro ──")

    resultado = biblioteca.devolver_libro(libro1.isbn, cedula_est1)
    print(resultado)

    print(f"\n── Estado del libro devuelto ──")
    print(f"  {libro1}")

    print("\n── Prestando nuevamente ──")

    resultado = biblioteca.prestar_libro(
        libro1.isbn, cedula_est2, fake.date(), fake.date()
    )
    print(resultado)

    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()