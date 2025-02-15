## Ejecutar Jmeter desde la linea de comandos

Por qu+e no ejecutar el modo interfaz gráfica de usuario GUI

* GUI consume mas recursos/memoria
* GUI no se recomienda para pruebas de carga pesadas
* La linea de comandos puede ser integrada con otros sistemas (Jenkins/CI- Integracion continua, etc)

## PASO 1:
    Ir a la linea de comandos CMD-> JMeter -> Carpeta bin

## PASO 2:
    Ejecjutar el comando jmeter -n -t[ruta script jmeter] -l[ruta archivo de resultados]

-n significa  no ejecutar desde el GUI
-t es la ruta del script de jmeter
-l ruta del archivo de resultados



