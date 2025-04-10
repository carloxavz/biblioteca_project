
from biblioteca.models import Autor, Libro, Resena

autor = Autor.objects.create(nombre="Gabriel Garcia Marquez", nacionalidad="Colombiano")
libro = Libro.objects.create(titulo="Cien anios de soledad", autor=autor, fecha_publicacion="1967-06-05", resumen="Una novela que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.")
Resena.objects.create(libro=libro, texto="Una obra maestra de la literatura.", calificacion=5)

autor = Autor.objects.create(nombre="J.K. Rowling", nacionalidad="Británica")
libro = Libro.objects.create(titulo="Harry Potter y la piedra filosofal", autor=autor, fecha_publicacion="1997-06-26", resumen="La historia de un joven mago que descubre su herencia mágica.")
Resena.objects.create(libro=libro, texto="Un libro mágico y emocionante.", calificacion=4)

autor = Autor.objects.create(nombre="J.R.R. Tolkien", nacionalidad="Británico")
libro = Libro.objects.create(titulo="El hobbit", autor=autor, fecha_publicacion="1937-09-21", resumen="La aventura de Bilbo Bolsón en la Tierra Media.")        
Resena.objects.create(libro=libro, texto="Un clásico de la literatura fantástica.", calificacion=5)

autor = Autor.objects.create(nombre="George R.R. Martin", nacionalidad="Estadounidense")
libro = Libro.objects.create(titulo="Juego de tronos", autor=autor, fecha_publicacion="1996-08-06", resumen="La lucha por el Trono de Hierro en los Siete Reinos de Westeros.")     
Resena.objects.create(libro=libro, texto="Una historia épica llena de intriga y traición.", calificacion=5)

autor = Autor.objects.create(nombre="Isaac Asimov", nacionalidad="Estadounidense")
libro = Libro.objects.create(titulo="Fundación", autor=autor, fecha_publicacion="1951-06-01", resumen="La historia de la Fundación Galáctica y su lucha por preservar el conocimiento.")
Resena.objects.create(libro=libro, texto="Una obra maestra de la ciencia ficción.", calificacion=5)