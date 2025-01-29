# Tecnicas de pruebas de software

Las tecnicas de pruebas de software ayudan a diseñar mejores casos de prueba, dado que no es posible realizar pruebas exhaustivas.

## 1. Analisis de valor limite (Boundary)
Se basa en pruebas entre particiones, valor maximo, minimo, VVA, ofrece una selección de pruebas.

Ejemplo, introducir en un input valores del 1 al 10 como ideal. Si ingresamos 10.000 no vams a hacer todas las combinaciones.

- Condición de entrada 1 - 10

Pruebas:
El cero esta fuera del limite, validar si permite ingresar 0, lo mismo el 11.

0, 1, 2 y 9, 10, 11

## 2. Particion de clases de equivalencia
Permite dividir el dominio de entrada en un conjunto de clases de datos.
Ejemplo: Con dos inputs de texto

- Condición de entrada: 1 a 10 y 20 a 30

Pruebas:

---- a 0 (no valido)
1 a 10 (valido)
11 a 19 (no valido)
20 a 30 (valido)
31 a --- (no valido)

Seleccion de valores: -2, 3, 15, 25, 45

## 3. Pruebas basadas en tablas de decisiones o tabla causa-efecto
Responden a una combinacion de entrada de datos.
Debe haber un boton de envio.

- Condición de entrada:
Tipo de usuario (Estudiante, profesor, miembro público)
Tipo de libro (Ficción, no ficción, referencia)
Estado del libro (disponible, no disponible)

## 4. Transicion de estado
Cuando los cambios en las condiciones de entrada cambian el estado de la aplicacion. Ejemplo: El dark mode, si no esta bien aplicado, los items de menu no se ven.

* Ejemplo en un inicio de sesion:
Estado Inicial (AUT Desconectado)
Transición de estado: Intento de sesión exitoso
Transición de estado: Intento de sesión fallido
Transición de estado: Cuenta bloqueada

## 5. Error al adivinar
Basados en la expereincia de los analistas que adivinan donde podria haber un error.

