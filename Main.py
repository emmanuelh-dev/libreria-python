from Biblioteca import Biblioteca
from Libro import Libro
from Exports import ExportadorBiblioteca

def menu():
    opciones = {
        '1': 'AGREGAR',
        '2': 'EDITAR',
        '3': 'BORRAR',
        '4': 'BUSCAR',
        '5': 'MOSTRAR BIBLIOTECA',
        '6': 'Exportar',
        '7': 'SALIR',
    }

    print("Menú de opciones:")
    for opcion, descripcion in opciones.items():
        print(f"{opcion}. {descripcion}")

    opcion_elegida = input("Ingrese el número de la opción deseada: ")
    return opcion_elegida

def main():
    opciones_validas = ['1', '2', '3', '4', '5', '6', '7']
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
                # Submenú para seleccionar formato de exportación
                # Tambien con la biblioteca actualizada
                exportador = ExportadorBiblioteca(biblioteca)

                # Submenú para seleccionar formato de exportación
                while True:
                    print("Seleccione el formato de exportación:")
                    print("1. Exportar a Acces")
                    print("2. Exportar a Excel")
                    print("3. Exportar a SQL")
                    print("4. Volver al menú principal")
                    sub_opcion = input("Ingrese su opción: ")

                    if sub_opcion == "1":
                        nombre_archivo_acces = input("Ingrese el nombre del archivo Acces: ")
                        exportador.exportar_a_access(f"{nombre_archivo_acces}.accdb")
                    elif sub_opcion == "2":
                        nombre_archivo_excel = input("Ingrese el nombre del archivo Excel: ")
                        exportador.exportar_a_excel(f"{nombre_archivo_excel}.xlsx")
                    elif sub_opcion == "3":
                        nombre_archivo_sql = input("Ingrese el nombre del archivo SQL: ")
                        exportador.exportar_a_sql(f"{nombre_archivo_sql}.sql")
                    elif sub_opcion == "4":
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
            elif opcion == "7":
                print("Saliendo del programa...")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
