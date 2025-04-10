Biblioteca

Este proyecto es una aplicación web básica desarrollada con Django para gestionar autores, libros y reseñas. 

---

## Características principales

- Registrar autores y libros.
- Registrar reseñas para cada libro.
- Visualizar libros y sus reseñas.
- Carga de datos iniciales desde un script en consola.

---


## Instalación y ejecución local

1. Clona el repositorio:

```
git clone https://github.com/carloxavz/biblioteca_project
```

2. Crea y activa un entorno virtual:

```
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instala las dependencias:

```
pip install django
```

4. Aplica las migraciones:

```
python manage.py makemigrations
python manage.py migrate
```

5. Crea un superusuario para acceder al admin:

```
python manage.py createsuperuser
```

6. Ejecuta el servidor:

```
python manage.py runserver
```

7. Entra al panel de administración:
http://127.0.0.1:8000/admin

---

## Poblar datos de prueba

```
python manage.py shell < poblar_datos.py
```

## Autores

Carlos Antonio Avendaño Villamizar  
Juan David Marciales Niebles
Ingeniería de Sistemas  
Universidad Francisco de Paula Santander

---

