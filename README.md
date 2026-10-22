# Skills UAI · Trabajo de Diploma

Skills e instrucciones reutilizables para ayudar a estudiantes de **Trabajo de Diploma (TD) de la UAI** a crear diagramas con PlantUML, mantenerlos alineados con su proyecto y publicarlos en el documento de entrega.

Una **skill** es una carpeta con un archivo `SKILL.md`: instrucciones que un asistente de IA puede leer y aplicar. Algunas incluyen scripts para realizar tareas concretas. No hace falta usar el mismo sistema, lenguaje o arquitectura que los demás compañeros.

Este material es una iniciativa entre estudiantes. Para determinar qué exige una entrega, usá la **consigna y la Carpeta Modelo vigentes de tu comisión**, junto con las indicaciones de tu docente. Los ejemplos de este repositorio no fijan una numeración oficial.

## ¿Qué incluye?

| Skill | Para qué sirve | Archivo |
|---|---|---|
| `tp-uml-y-casos-de-uso` | Coordina qué diagramar, dónde guardar las fuentes y cómo contrastar diagramas, casos de uso y código. | [SKILL.md](tp-uml-y-casos-de-uso/SKILL.md) |
| `plantuml` | Crea, valida y convierte `.puml` a PNG/SVG. Incluye referencias y ejemplos de distintos tipos de diagrama. Está embebida en `tp-delivery-standards`. | [SKILL.md](tp-delivery-standards/embedded-skills/plantuml/SKILL.md) |
| `publicar-diagramas-google-docs` | Prepara PNG y completa los espacios del documento en Google Docs, conservando las imágenes existentes. | [SKILL.md](publicar-diagramas-google-docs/SKILL.md) |
| `tp-delivery-standards` | Revisa coherencia entre implementación, documentación y criterios de entrega configurados para tu proyecto. | [SKILL.md](tp-delivery-standards/SKILL.md) |

**Flujo habitual:** código y casos de uso → fuentes PlantUML → PNG → carga manual a Drive → inserción y verificación en Google Docs.

## Empezar a usarlo

### 1. Descargar y elegir cómo cargar las skills

Cloná el repositorio o descargá el ZIP desde **Code → Download ZIP**:

```bash
git clone https://github.com/aggutierrez98/Skills-UAI.git
cd Skills-UAI
```

Hay dos formas de usarlo:

- **Sin instalar:** abrí la carpeta con tu asistente y pedile que lea el `SKILL.md` correspondiente por su ruta. Si tu aplicación no permite leer archivos locales, adjuntá la skill y sus referencias necesarias. Los scripts requieren una terminal local o un entorno que pueda ejecutarlos.
- **Dentro de tu proyecto:** copiá las carpetas `tp-uml-y-casos-de-uso`, `tp-delivery-standards` y `publicar-diagramas-google-docs` completas a `.agents/skills/`, si tu herramienta admite esa ubicación. Conservá sus nombres y estructura: las referencias entre skills son relativas. Para otro asistente, usá su ubicación de skills documentada o cargá las rutas explícitamente.

La skill `plantuml` se carga desde su ruta embebida; algunos asistentes no descubren skills anidadas automáticamente. No hace falta copiarla por separado.

Copiar archivos **no conecta Google**, no instala Java y no garantiza que tu asistente ejecute comandos. La detección automática y los conectores disponibles dependen de la herramienta que uses.

### 2. Describir tu proyecto una sola vez

Copiá [la plantilla de contexto](ejemplos/TD-CONTEXTO.ejemplo.md) a la raíz de tu proyecto como `TD-CONTEXTO.md` y completala. Incluye:

- Nombre, alcance, lenguaje, arquitectura y ubicación del código.
- Requisitos de tu comisión y correspondencia con las secciones del documento.
- Carpeta de diagramas, identificadores de casos de uso y reglas de nombres.
- Motor de base de datos y comandos de compilación/verificación, si corresponden.
- Documento y pestaña de destino, cuando quieras publicar.

Si ya tenés esta información en `AGENTS.md` u otra documentación, podés indicarle al asistente que use esas fuentes. **No es necesario instalar OpenSpec** ni crear una solución .NET para usar estas skills.

### 3. Instalar las herramientas para renderizar

| Herramienta | Cuándo se necesita |
|---|---|
| Java compatible con tu versión de PlantUML y `plantuml.jar` | Para renderizar las fuentes. Descarga: [PlantUML](https://plantuml.com/download). |
| Graphviz (`dot` en PATH) | Para los tipos de diagrama que lo requieren. Descarga: [Graphviz](https://graphviz.org/download/). |
| Python 3.11 o superior y Pillow | Para el preparador de lotes PNG. |
| Node.js 20 o superior | Para el planificador/verificador offline y sus tests; no requiere `npm install`. |
| Conectores de Google Docs y Drive en tu asistente | Solo para leer/publicar en Google. Se priorizan MCP nativos y se utiliza One como alternativa si está conectado. |

Configurá `PLANTUML_JAR` con la ruta del JAR en **tu máquina**, o pasá `--jar` al preparador.

**Linux / macOS / WSL**, desde este repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
export PLANTUML_JAR="$HOME/herramientas/plantuml.jar"
java -jar "$PLANTUML_JAR" -version
dot -V
```

**Windows PowerShell**, desde este repositorio:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PLANTUML_JAR = "$HOME\herramientas\plantuml.jar"
java -jar $env:PLANTUML_JAR -version
dot -V
```

Reemplazá la ruta del JAR por la real. Estas variables se establecen para la terminal actual. En WSL necesitás que Java, Graphviz y Python sean accesibles desde WSL.

## Primera prueba local

Incluimos [una secuencia](ejemplos/diagramas/CU01-registrar-solicitud-secuencia.puml) y [un diagrama de clases](ejemplos/diagramas/solicitudes-clases.puml) ficticios. Desde la raíz de esta colección:

```bash
.venv/bin/python publicar-diagramas-google-docs/scripts/preparar_png.py \
  "ejemplos/diagramas/*.puml" --output "salidas/ejemplo-01"
```

En PowerShell, el mismo comando en una línea:

```powershell
.\.venv\Scripts\python.exe publicar-diagramas-google-docs/scripts/preparar_png.py "ejemplos/diagramas/*.puml" --output "salidas/ejemplo-01"
```

El resultado es una **carpeta nueva** con PNG a 200 DPI y `manifest.json` con dimensiones y hashes. Los originales `.puml` se conservan; las leyendas se omiten en el render. Para repetir, elegí otra salida, por ejemplo `salidas/ejemplo-02`.

En tu proyecto, reemplazá el glob por tus fuentes y anteponé `.agents/skills/` a la ruta del script si instalaste ahí las skills. Consultá [la guía de entorno PlantUML](tp-delivery-standards/embedded-skills/plantuml/references/entorno-proyecto.md).

## Publicar en el documento del TP

1. Indicá al asistente qué fuentes publicar y en qué documento/pestaña.
2. Revisá el lote generado. El asistente debe informar la **ruta local exacta**.
3. **Subí los PNG manualmente a una carpeta de Drive** y pasale su enlace. No hace falta subir el manifiesto.
4. El asistente lee el documento, identifica encabezados reales y relaciona cada imagen con su espacio. Si hay dudas, debe preguntarte.
5. Publicá primero una muestra para revisar el formato; luego completá el lote y verificá las inserciones.

Para facilitar la correspondencia, usá estilos de encabezado reales y, debajo, un rótulo y un placeholder en párrafos separados:

```text
CU01 · Registrar solicitud         ← Encabezado, no solo texto en negrita
Diagrama de secuencia:
[Pegar aquí el diagrama de secuencia]
```

Las imágenes existentes se conservan por defecto. Los scripts locales generan un plan; **la escritura la realiza el asistente mediante un conector disponible**. No contienen autenticación ni realizan la carga binaria a Drive. Si Google no puede recuperar una imagen privada, el flujo pide resolver el acceso y no cambia permisos automáticamente.

**Google Docs y Word:** esta colección publica en Google Docs. Después podés descargar el documento desde Google Docs como Microsoft Word (`.docx`) y revisar su paginación. La edición directa de un Word local y la generación de especificaciones `.docx` no están incluidas.

Guías técnicas: [conectores](publicar-diagramas-google-docs/references/conectores.md) y [destinos, planificación y verificación](publicar-diagramas-google-docs/references/publicacion.md).

## Ejemplos de pedidos al asistente

**Generar diagramas desde mi código**
> Leé `TD-CONTEXTO.md` y `tp-uml-y-casos-de-uso/SKILL.md`. Para CU01, contrastá el flujo con el código y prepará su secuencia y las clases participantes en PlantUML. Preguntame si falta información.

**Preparar imágenes**
> Usá `publicar-diagramas-google-docs/SKILL.md` para preparar los `.puml` de `diagramas/solicitudes`. Indicame la carpeta local; yo los subo a Drive.

**Retomar después de subir**
> Ya subí los PNG a esta carpeta: [enlace]. Completá los placeholders de secuencia en este documento: [enlace], pestaña [identificador]. Conservá las imágenes existentes y mostrame primero el plan.

Si instalaste las skills dentro de tu proyecto, usá sus rutas bajo `.agents/skills/` en los pedidos.

## Límites y preguntas frecuentes

- **¿Sirve con otro lenguaje o arquitectura?** Sí. Indicá el stack y las capas reales. No se presupone WinForms, SQL Server ni una arquitectura de siete capas.
- **¿Debo usar códigos T0X/N0X o CUN?** No. Son ejemplos; podés usar tus títulos e identificadores y mapearlos explícitamente.
- **¿Incluye toda la Carpeta Modelo?** No. Usá la documentación autorizada de tu comisión. Las skills `tp-carpeta-modelo` y `tp-use-case-spec`, mencionadas en versiones de origen, no están distribuidas aquí ni son dependencias obligatorias.
- **¿Funciona sin conectores?** La creación y el renderizado local, sí. La publicación automática necesita un conector capaz de leer la estructura y escribir imágenes en Docs. Si no existe, insertá los PNG manualmente.
- **¿Inserta en tablas o documentos con columnas especiales?** El planificador básico los rechaza cuando no puede determinar el área útil; requieren adaptación explícita.
- **¿Por qué rechaza un lote?** Verificá nombres PNG duplicados, fuentes sin diagrama completo, JAR/configuración, placeholders repetidos o una carpeta de salida ya existente.
- **¿Reemplaza la revisión del TP?** Revisá nombres, relaciones, flujos, legibilidad y consistencia con tu implementación antes de entregar.

## Verificar y colaborar

Desde la raíz del repositorio:

```bash
python3 scripts/verificar_coleccion.py
node --test publicar-diagramas-google-docs/scripts/documento.test.mjs
python3 -m unittest discover -s publicar-diagramas-google-docs/scripts -p 'test_*.py'
```

En Windows podés usar `py -3` en lugar de `python3`. Estos chequeos son locales y no editan documentos de Google.

Para proponer mejoras, leé [CONTRIBUTING.md](CONTRIBUTING.md). La adaptación y el origen del material se explican en [docs/ORIGEN.md](docs/ORIGEN.md).
