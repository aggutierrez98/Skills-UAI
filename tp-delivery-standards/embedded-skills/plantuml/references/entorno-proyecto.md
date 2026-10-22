# Entorno PlantUML del proyecto

Resolver las rutas desde el proyecto y la ubicacion real de la skill. No
presuponer instalaciones, wrappers o variables configuradas en otra maquina.

## Herramientas

- Java y un JAR de PlantUML compatible con esa version de Java.
- Graphviz (`dot`) para los diagramas que lo requieren.
- Python para los scripts de conversion. El preparador de PNG de publicacion
  usa ademas Pillow; ver el README y `requirements.txt` de la coleccion.
- `PLANTUML_JAR` apuntando al JAR, o el argumento `--jar` del preparador.

Comprobar con `java -version`, `dot -V` y
`java -jar <ruta-al-jar> -version`. El comando `plantuml` solo esta disponible
si se instalo un ejecutable/wrapper; no se requiere para usar el JAR directamente.

## Fuentes y render

1. Leer el contexto del proyecto y confirmar el alcance pedido.
2. Guardar un diagrama completo por `.puml`, con nombres unicos, en la carpeta
   acordada (por defecto `diagramas/<requisito>/`).
3. Usar nombres reales de clases, metodos, tablas y relaciones si el diagrama
   describe implementacion. Identificar modelos propuestos cuando corresponda.
4. Renderizar y comprobar sintaxis y legibilidad antes de publicar.

Ejemplo sin wrappers, desde la carpeta de un diagrama:

```bash
java -jar "$PLANTUML_JAR" -tsvg archivo.puml
```

En PowerShell usar `$env:PLANTUML_JAR` en lugar de `$PLANTUML_JAR`.

Para preparar lotes PNG a 200 DPI, omitir leyendas y limitar pixeles, usar
`publicar-diagramas-google-docs/scripts/preparar_png.py` desde la raiz de la
coleccion. Si las skills estan instaladas bajo `.agents/skills/`, anteponer
esa ruta. El script acepta `--jar` y trabaja con includes relativos al fuente.

## Legibilidad en el documento

Comprobar las dimensiones reales y revisar una muestra a escala de pagina.
No aplicar un rango fijo de ancho/alto a todos los diagramas: una secuencia
larga y un diagrama de clases pueden requerir composiciones distintas.

Cuando un diagrama quede muy ancho o alto:

1. Ajustar direccion, agrupaciones y espaciado.
2. Usar enlaces `hidden` para layout si ayudan, marcandolos como recursos
   visuales que no representan relaciones del dominio.
3. Proponer otra orientacion de pagina o una division por responsabilidades.
4. Acordar cualquier simplificacion con el usuario; no borrar operaciones,
   interfaces o relaciones solo para que la imagen entre en una pagina.

Conservar proporciones al insertar. Un PNG grande no garantiza legibilidad
si termina reducido a texto diminuto. Si no se resuelve, informar el problema
antes de publicar el lote completo.

Volver a [la skill central](../../../../tp-uml-y-casos-de-uso/SKILL.md) para
contrastar los artefactos y sincronizar con la documentacion formal.
