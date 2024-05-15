from Biblioteca import Biblioteca
from Libro import Libro
def menu():
    opciones = {
        '1': 'AGREGAR',
        '2': 'EDITAR',
        '3': 'BORRAR',
        '4': 'BUSCAR',
        '5': "MOSTRAR BIBLIOTECA",
        '6': 'SALIR',
    }

    print("Menú de opciones:")
    for opcion, descripcion in opciones.items():
        print(f"{opcion}. {descripcion}")

    opcion_elegida = input("Ingrese el número de la opción deseada: ")
    return opcion_elegida

def main():
    opciones_validas = ['1', '2', '3', '4', '5']
    biblioteca = Biblioteca()

    biblioteca.libros = [
        Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción', '9780307350437'),
        Libro('El principito', 'Antoine de Saint-Exupéry', 'Infantil', '9780156012195'),
        Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', '9788478884450'),
        Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Clásico', '9788424119485'),
        Libro('Orgullo y prejuicio', 'Jane Austen', 'Romance', '9788491052562')
    ]

    while True:
        opcion = menu()
        if opcion in opciones_validas:
            if opcion == "1":
                biblioteca.agregar_libro()
            elif opcion == "2":
                biblioteca.editar_libro()
            elif opcion == "3":
                biblioteca.borrar_libro()
            elif opcion == "4":
                biblioteca.buscar()
            elif opcion == "5":
                biblioteca.mostrar_libros()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()