from Libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        nuevo_libro = Libro(titulo, autor, genero, isbn)
        self.libros.append(nuevo_libro)
        print("Libro agregado exitosamente.")
        print(f"Total de libros en la biblioteca: {len(self.libros)}")

    def buscar(self):
        libro = self.buscar_por_termino()
        
        if libro is None:
            print("Algo salió mal")
        else:
            print("Libro encontrado:")
            for valor in libro.values():
                print(valor)

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Libros en la biblioteca:")
            for i, libro in enumerate(self.libros, start=1):
                print(f"{i}. {libro.titulo} - {libro.autor} - {libro.genero} - ISBN: {libro.isbn}")

    def editar_libro(self, isbn=None, titulo=None, autor=None, genero=None):
        libro_a_editar = self.buscar_por_termino()

        if libro_a_editar:
            print(f"Editando el libro: {libro_a_editar.titulo}")

            # Solicitar al usuario las nuevas propiedades del libro (si no se proporcionan como argumentos)
            titulo = input(f"Ingrese el nuevo título del libro (dejar en blanco para mantener '{libro_a_editar.titulo}'): ") or libro_a_editar.titulo
            autor = input(f"Ingrese el nuevo autor del libro (dejar en blanco para mantener '{libro_a_editar.autor}'): ") or libro_a_editar.autor
            genero = input(f"Ingrese el nuevo género del libro (dejar en blanco para mantener '{libro_a_editar.genero}'): ") or libro_a_editar.genero
            isbn = input(f"Ingrese el nuevo ISBN del libro (dejar en blanco para mantener '{libro_a_editar.isbn}'): ") or libro_a_editar.isbn

            # Crear un nuevo objeto Libro con las propiedades actualizadas
            nuevo_libro = Libro(titulo, autor, genero, isbn)

            # Reemplazar el libro existente con el libro actualizado en la lista de libros
            index_libro = self.libros.index(libro_a_editar)
            self.libros[index_libro] = nuevo_libro

            print("Libro editado exitosamente.")
        else:
            print("No se encontró ningún libro con ese ISBN.")


    def borrar_libro(self):
        libro = self.buscar_por_termino()

        if libro == None:
            print("No se encontro el libro")
        else:
            confirmacion = input(f"¿Estás seguro de que deseas borrar '{libro.titulo}'? (s/n): ")

            if confirmacion == "s":
                self.libros.remove(libro)
                print(f"Libro borrado exitosamente. Quedan {len(self.libros)} libros.")
            else:
                print("Operacion cancelada")



    def buscar_por_termino(self, opcion=None):
        opciones = {
            "1": "titulo",
            "2": "autor",
            "3": "genero",
            "4": "isbn"
        }
        opciones_validas = ['1', '2', '3', '4', '5']

        if not self.libros:
            print("No hay libros disponibles")
            return

        print("Selecciona tu término de búsqueda:")
        for op, desc in opciones.items():
            print(f"{op}. {desc}")
        seleccion = input("Selecciona el término a buscar: ")

        if seleccion in opciones_validas:
            criterio = opciones[seleccion]

            # Pedir al usuario el valor a buscar
            valor = input(f"Ingrese el {criterio} a buscar: ")

            # Llamar a la función buscar_libros con el criterio y valor proporcionados
            libros_encontrados = self.buscar_libros(criterio, valor)

            if not libros_encontrados:
                print("No se encontraron libros con ese criterio de búsqueda.")
                return None

            if len(libros_encontrados) == 1:
                # Si solo hay un libro encontrado, mostrarlo directamente
                libro_elegido = libros_encontrados[0]
                print("Libro encontrado:")
                print(f"- {libro_elegido.titulo} por {libro_elegido.autor}")
                return libro_elegido
            else:
                # Si hay múltiples libros encontrados, permitir al usuario seleccionar uno
                print("Libros encontrados:")
                for i, libro in enumerate(libros_encontrados, start=1):
                    print(f"{i}. {libro.titulo} por {libro.autor}")

                while True:
                    try:
                        seleccion_libro = int(input("Selecciona el número del libro que deseas (0 para cancelar): "))
                        if seleccion_libro == 0:
                            print("Operación cancelada.")
                            return None
                        elif 1 <= seleccion_libro <= len(libros_encontrados):
                            libro_elegido = libros_encontrados[seleccion_libro - 1]
                            print(f"Libro seleccionado: {libro_elegido.titulo} por {libro_elegido.autor}")
                            return libro_elegido
                        else:
                            print("Número de selección inválido. Inténtalo de nuevo.")
                    except ValueError:
                        print("Debe ingresar un número válido.")

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            return None


    # Filtra los libros
    def buscar_libros(self, criterio, valor):
        libros_encontrados = []
        for libro in self.libros:
            if valor.lower() in getattr(libro, criterio).lower():
                libros_encontrados.append(libro)
        return libros_encontrados