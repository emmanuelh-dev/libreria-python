from openpyxl import Workbook
from pandas import DataFrame
import pandas as pd
import pyodbc

class ExportadorBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def exportar_a_access(self, nombre_archivo):
      print("Exportando...")

    def exportar_a_sql(self, nombre_archivo):
            with open(nombre_archivo, 'w') as f:
                # Escribir el encabezado del archivo SQL
                f.write("-- Script de inserción SQL para la tabla Libros\n\n")
                f.write("INSERT INTO Libros (titulo, autor, genero, isbn) VALUES\n")

                # Escribir los datos de cada libro como una instrucción INSERT
                first = True
                for libro in self.biblioteca.libros:
                    if not first:
                        f.write(",\n")
                    else:
                        first = False
                    values = f"('{libro.titulo}', '{libro.autor}', '{libro.genero}', '{libro.isbn}')"
                    f.write(values)

            print(f"Biblioteca exportada a archivo SQL en '{nombre_archivo}'.")

    def exportar_a_excel(self, nombre_archivo):
        # Crear un nuevo libro de Excel (workbook)
        wb = Workbook()

        # Seleccionar la hoja activa (por defecto)
        ws = wb.active
        ws.title = "Libros"  # Asignar un nombre a la hoja

        # Escribir los encabezados de columna
        encabezados = ['Título', 'Autor', 'Género', 'ISBN']
        ws.append(encabezados)

        # Escribir los datos de los libros en filas
        for libro in self.biblioteca.libros:
            # Obtener los atributos de cada libro como una lista de valores
            libro_data = [libro.titulo, libro.autor, libro.genero, libro.isbn]
            ws.append(libro_data)  # Agregar cada lista de datos como una fila

        # Guardar el libro de Excel en el archivo especificado
        wb.save(nombre_archivo)

        # Mostrar mensaje de éxito
        print(f"Biblioteca exportada a Excel en '{nombre_archivo}'.")