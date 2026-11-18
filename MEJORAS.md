# Propuesta de mejoras para profesionalizar el proyecto

Revisión del estado del proyecto tras la versión 1.0.0 (noviembre de 2026).

El punto de partida es razonable para un proyecto desarrollado sin experiencia profesional en desarrollo de aplicaciones:

- El cálculo está separado de la interfaz: [calculos/calculo_via.py](calculos/calculo_via.py) no depende de Flet.
- Los datos están modelados con `dataclass`.
- Las tablas de resultados se generan a partir de definiciones de columnas.

Lo que falta para que sea profesional está menos en el estilo del código y más en tres aspectos:

1. **Demostrar que los resultados son correctos.**
2. **Poder reproducir cada versión.**
3. **Que no falle sin avisar.**

Las propuestas están ordenadas por importancia para una herramienta de cálculo de ingeniería.

---

## 1. Pruebas automáticas contra la hoja de cálculo (prioridad máxima)

Ahora mismo nada comprueba que el programa dé los mismos números que la hoja Excel validada (`ffcc.0.0.8`). Cualquier cambio, incluidas las optimizaciones de rendimiento, podría alterar un resultado sin que nadie lo detecte. En un programa que se usa para dimensionar gálibos, este es el mayor riesgo.

- [ ] Preparar con `pytest` una batería de **casos de referencia**: datos de entrada de la hoja y sus resultados esperados (Sa, Si, gálibo límite, gálibo nominal y pantógrafo por punto), con tolerancia.
- [ ] Cubrir casos representativos: recta y curva, ancho ibérico, internacional y métrico, y vía en buen y mal estado.
- [ ] Añadir pruebas unitarias de las funciones de [calculos/calculos.py](calculos/calculos.py), cada una con su referencia al artículo de la Orden FOM/1630/2015.

Esta batería de pruebas es además el **dossier de validación** del programa: demuestra que reproduce la hoja validada en N casos y que se comprueba automáticamente en cada cambio.

## 2. Control de versiones y trazabilidad

- [ ] Confirmar los cambios pendientes en commits separados por tema (rendimiento, pestaña "?", etc.).
- [ ] Trabajar en ramas y marcar cada versión publicada con una etiqueta (`git tag v1.0.0`).
- [ ] Mantener un `CHANGELOG.md` con lo que cambia en cada versión.
- [ ] Usar **versionado semántico**: 1.0.0 → 1.0.1 para correcciones, 1.1.0 para funciones nuevas. La versión está centralizada en [configuracion.py](configuracion.py).
- [ ] **Trazabilidad de resultados:** incluir la versión del programa y los datos de entrada en todo lo que se exporta (texto copiado al portapapeles y DXF), para que cualquier resultado de un proyecto se pueda reproducir más adelante.
- [ ] El `.gitignore` excluye los `*.xlsx`, pero `ffcc.0.0.8 COPIA LOCAL.xlsx` ya está en el repositorio. Si es la referencia de validación, debe estar a propósito y con un nombre claro (por ejemplo `validacion/referencia_v1.0.0.xlsx`). Si no lo es, quitarla del repositorio.

## 3. Fallos y robustez

La exportación a DXF (`generar_DXF` en [main.py](main.py)) es la parte más frágil:

- [ ] **Si no se ha elegido ninguna opción, falla sin avisar**: `ft_dxf.value` es `None` y `None[-1]` lanza un error que Flet descarta.
- [ ] Si se elige la vía 2 sin tenerla activada, `resultado` es `None` y también falla.
- [ ] La ruta del fichero está fija (`c:/Autodesk/nomsalida.dxf`): falla si la carpeta no existe, sobrescribe sin preguntar y no confirma nada al usuario. Sustituirla por un `ft.FilePicker` con "Guardar como".
- [ ] El botón dice "Exportar Galibo Límite", pero exporta cualquiera de las seis opciones.
- [ ] El DXF se escribe a mano con lo mínimo. La biblioteca `ezdxf` genera ficheros válidos con capas, polilíneas cerradas y unidades.

En general:

- [ ] Añadir un **registro de errores** (`logging` a un fichero). Ahora los errores dentro de los eventos de Flet desaparecen sin dejar rastro.

## 4. Distribución reproducible

- [ ] [main.spec](main.spec) genera un ejecutable llamado `main.exe`, no incluye la carpeta `assets` (logo e icono) y no indica ningún icono. Hay que corregirlo.
- [ ] Crear un único script de compilación (`build.ps1`) que genere siempre igual el ejecutable con nombre y versión (`PAGIF_v1.0.0.exe`).
- [ ] Trabajar con un entorno virtual (`.venv`).
- [ ] Fijar todas las versiones en `requirements.txt` y crear un `requirements-dev.txt` para `pytest`, `ruff` y `pyinstaller`.
- [ ] Indicar la versión de Python necesaria.
- [ ] Anotar como deuda técnica que Flet está fijado en 0.24.1 porque las versiones posteriores cambian la API. Las pruebas del punto 1 son las que permitirán actualizar con seguridad.

## 5. Calidad y legibilidad del código

- [ ] Usar **`ruff`** (análisis y formato automático) para unificar el estilo.
- [ ] **Documentar las variables del modelo:** en `Punto` ([datos_variables.py](datos_variables.py)) muchas variables tienen el comentario vacío. Cada una debería indicar su significado y el artículo de la Orden de donde sale (por ejemplo, `Dbsusp_ai`: "Δb susp, art. X.Y").
- [ ] Unificar los nombres de las funciones: conviven `calcular_SVa1_ast` y `calcular_nom_SV3a`, y hay un parámetro mal escrito (`hquierbroaux`).
- [ ] Sacar de [main.py](main.py) la lógica que no es de interfaz: la exportación DXF debería ir en un módulo `exportacion/dxf.py` sin dependencias de Flet, que además se podría probar.

## 6. Documentación

- [ ] Separar el README en dos partes:
  - **Usuarios:** qué calcula, limitaciones y cómo instalarlo.
  - **Desarrolladores:** estructura, cómo ejecutar las pruebas y cómo compilar.
- [ ] Pasar la lista "TAREAS A HACER" del README a incidencias (issues) de GitHub.
- [ ] Añadir un **aviso de alcance**: qué casos cubre el programa y cuáles no (por ejemplo, los gráficos solo muestran el lado interior de la curva).

## 7. Automatización

Cuando lo anterior esté hecho:

- [ ] Configurar GitHub Actions para que, en cada envío de cambios, se ejecuten las pruebas y `ruff`.
- [ ] Al crear una etiqueta `v*`, compilar el `.exe` y adjuntarlo a una *release*.

Así nada llega a los usuarios sin haber pasado las pruebas.

---

## Orden recomendado

1. **Punto 2:** confirmar en git el trabajo pendiente.
2. **Punto 1:** pruebas contra la hoja de cálculo.
3. **Punto 3:** corregir la exportación DXF.

Las pruebas son la base de todo lo demás, porque permiten cambiar el código sin miedo a alterar los resultados.
