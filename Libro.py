class Libro:
    def __init__(self, titulo, autor, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, ISBN: {self.isbn}"

    def actualizar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def actualizar_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def actualizar_genero(self, nuevo_genero):
        self.genero = nuevo_genero

    def actualizar_isbn(self, nuevo_isbn):
        self.isbn = nuevo_isbn

    def obtener_informacion(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "isbn": self.isbn
        }