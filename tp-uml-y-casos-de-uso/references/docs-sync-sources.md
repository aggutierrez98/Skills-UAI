# Fuentes y sincronización con el documento

## Destino por proyecto

Obtener del usuario o de su contexto el documento, la pestaña y las secciones
de destino. No hay un documento predeterminado para esta colección. No reutilizar
enlaces o IDs de conexiones de otro estudiante o de una sesión anterior.

La carpeta de fuentes se acuerda con el proyecto; por defecto:
`diagramas/<requisito>/`. Guardar allí `.puml` y las especificaciones relacionadas.

## Correspondencia

Preparar una relación explícita entre archivo, tipo de diagrama, CU/requisito,
pestaña, encabezado real y placeholder. El prefijo de una carpeta no demuestra
que el documento use la misma numeración. Ignorar menciones en índices y texto.

Si hay varias imágenes bajo un CU, acotar cada destino con un rótulo propio,
por ejemplo `Diagrama de clases:` y `Diagrama de secuencia:`.

## Publicación

1. Actualizar y validar las fuentes antes de generar las imágenes.
2. Usar [la skill de publicación](../../publicar-diagramas-google-docs/SKILL.md).
3. Preparar el lote local y esperar la carga manual del usuario a Drive.
4. Descubrir conectores de Docs/Drive disponibles y planificar sobre una lectura
   estructural con revisión vigente.
5. Conservar imágenes existentes; consultar ambigüedades o reemplazos.
6. Después de escribir o recibir un timeout, releer y verificar antes de reintentar.

La publicación automatizada es para Google Docs. Para entregar un Word,
descargar como `.docx` y revisar el resultado. Para editar directamente un
Word local hace falta una herramienta adicional; no asumir que está instalada.

## Balanceo

Clases, secuencias, CU y persistencia deben reflejar la versión que se entrega.
Registrar las fuentes y limitaciones si no se pudo inspeccionar código/base.
No afirmar que un PNG insertado demuestra por sí solo que el modelo sea correcto.
