# Caso de Usuario: Inicio de Sesión en el Sistema

## Nombre: Inicio de Sesión

## Actor: Usuario registrado

## Descripción: El usuario debe ingresar sus credenciales para acceder al sistema.

### Precondiciones:

El usuario debe estar registrado en el sistema.
Debe existir una base de datos con las credenciales almacenadas.

### Flujo Principal:

* El usuario abre la pantalla de inicio de sesión.
* El sistema muestra los campos de "Usuario" y "Contraseña" junto con el botón "Iniciar sesión".
* El usuario ingresa su nombre de usuario y contraseña.
* El usuario presiona el botón "Iniciar sesión".
* El sistema verifica las credenciales en la base de datos.
* Si las credenciales son correctas, el sistema redirige al usuario a la página principal del sistema.

### Flujo Alternativo:

* Si el usuario no ingresa datos en los campos requeridos, el sistema muestra un mensaje de error indicando que los campos son obligatorios.
* Si las credenciales son incorrectas, el sistema muestra un mensaje de error indicando que los datos no son válidos.

### Postcondición:

El usuario accede correctamente al sistema si sus credenciales son válidas.
Si las credenciales son incorrectas, el sistema evita el acceso y muestra un mensaje de error.