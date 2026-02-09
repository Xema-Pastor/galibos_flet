# galibos_flet
Programa de cálculo de gálibos ferroviarios según la Orden FOM/1630/2015, con el framework FLET

Nombre del proyecto IDI: DI0835

## Unidades de cálculo:
Todos las cotas, distancias y demás están en mm
Los datos que se leen de los formularios de FLET son del tipo _str_, y deben ser convertidos a _int_ o _float_ cuanto antes. Los valores que se guardanen var.* son todos del tipo número (salvo los que, evidentemente, son del tipo texto).

## TAREAS A HACER
* Que los gráficos sean listos y que detecten la parte interior de la curva y la exterior. Ahora mismo únicamente muestran los datos de LIM y NOM interiores. Hay que añadir los exteriores
* ~~Unificar los objetos ftt y fttabla, pues en esencia son lo mismo. No se ha podido unificar, pero se han agrupado la creación de las entidades~~
* ~~Optimizar el rendimiento, haciendo que no recalcule lo que no hace falta~~
* ~~Que pueda copiar datos y ponerlos en el portapapeles~~
* ~~Poner controles propios para los pantógrafos~~
* ~~Añadir los datos generales de los pantógrafos que se guardan en VIA en las pestañas de Descripción~~
* ~~Corregir que la separación entre vías también se vea afectada por el factor de escala~~
* Que genere un archivo *.dxf con las secciones

## EDICIÓN CON VS_CODE
El programa está escrito con la tecnología de FLET (https://flet.dev/). Para editar en vs_code es necesario:
* Instalar flet: _(pip install 'flet[all]')_
* Flet utiliza _hot reload_ para ejecutar la aplicación y ver los cambios que se hacen de manera instantánea. Para ejecutar la aplicación y verla como página web es necesario iniciar flet en la terminal con _flet run --web main.py_
* Para crear los ejecutables a partir del código es necesario intalar pyinstaller _(pip install pyinstaller)_. Una vez instalado para hacer el ejecutable se debe ejecutar en la terminal la orden _pyinstaller --onefile --windowed main.py_


