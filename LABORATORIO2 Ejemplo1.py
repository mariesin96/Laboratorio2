# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Atributos
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método para mostrar información del libro
    def mostrar_info(self):
        print(f"'{self.titulo}' de {self.autor}, {self.paginas} páginas")

# Creación de un objeto de la clase Libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)

# Uso del método del objeto
libro1.mostrar_info()
