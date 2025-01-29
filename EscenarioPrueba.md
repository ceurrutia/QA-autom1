# Escenario de prueba

Es una descripcion detallada de como se probara una funcion especifica del software.
Un escenario puede contener muchos casos de prueba.
Antes de crear un escenario de prueba se debe comprender cabalmente el requisito. Mantener nuestros escenarios simples y claros.
Cubrir todos los flujos posible. Crear un escenario para cada cobertura.

Los escenarios deben ser independientes unos de otros y sean reutilizables. No se debe depender de otro escenario para ejecutar una prueba.

### Considerar la manera de automaizar este tipo de escenarios tan repetitivos. 

## Debe contener
* Titulo
* Objetivo o propisito, que se espera lograr
* Precondiciones (Juego de datos, permisos)
* Pasos, acciones que se vana realizar
* Criterio de exito
* Post Condiciones (Status del sistema esperado)

#### Ejemplo

1. Titulo: Verificacion de login
2. Objetivo:  Asegurar que el usuario pueda iniciar sesion en forma corretca
3. Datos de prueba: Usuario admin y contrasenia. Nunca de produccion por favor!!!! Contactar con el dba.
4. Precondicion:
    * 1 usuario registrado, tener un juego de datos que acceda.
    * Un navegador
    * Una conexion a internet.
5. Pasos:
    * Abrir la conexion en el navegador usando la url: 
    * Hacer click en acceder
    * Ingresar un juego de datos valido
    * Clickear sobre el boton que dice "Acceder"
6. Criterio: El usuario es redirigido a la pagina principal de la aplicacion.
7. Post condicion: El usuario ha accedido correctamente a la aplicacion, mostrar alerta alert success  que diga "Has iniciado sesion correctamente".





