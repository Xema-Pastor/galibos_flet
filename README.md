# galibos_flet
Programa de cálculo de gálibos ferroviarios según la Orden FOM/1630/2015, con el framework FLET

Nombre del proyecto IDI: DI0835

## Unidades de cálculo:
Todos las cotas, distancias y demás están en mm
Los datos que se leen de los formularios de FLET son del tipo _str_, y deben ser convertidos a _int_ o _float_ cuanto antes. Los valores que se guardanen var.* son todos del tipo número (salvo los que, evidentemente, son del tipo texto).

## TAREAS A HACER
* Que los gráficos sean listos y que detecten la parte interior de la curva y la exterior. Ahora mismo únicamente muestran los datos de LIM y NOM interiores. Hay que añadir los exterioes
* Unificar los objetos ftt y fttabla, pues en esencia son lo mismo
* Optimizar el rendimiento, haciendo que no recalcule lo que no hace falta
* Que pueda copiar datos y ponerlos en el portapapeles
* Poner controles propios para los pantógrafos
* Añadir los datos generales de los pantógrafos que se guardan en VIA en las pestañas de Descripción
