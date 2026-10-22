# Skills UAI — guía para asistentes

Este repositorio contiene una colección de skills y ejemplos para estudiantes
de Trabajo de Diploma. No es el código de un producto ni define una arquitectura
obligatoria para los proyectos que lo utilicen.

## Al mantener esta colección

- Leer el README y la skill que se esté modificando.
- Mantener instrucciones independientes de nombres de alumnos, documentos,
  bases y rutas de una máquina particular.
- Conservar la estructura de carpetas y los enlaces relativos entre skills.
- Obtener stack, arquitectura, identificadores y requisitos del contexto de
  cada proyecto consumidor. La plantilla está en `ejemplos/TD-CONTEXTO.ejemplo.md`.
- Distinguir convenciones de esta colección de exigencias oficiales de cátedra.
- Mantener Google Docs como destino de publicación automatizada; no prometer
  edición de Word local ni carga automática de PNG a Drive.
- Usar documentos de prueba autorizados para verificar escrituras externas.
- No agregar dependencias obligatorias sobre skills que no estén incluidas.

## Verificaciones locales

```bash
python3 scripts/verificar_coleccion.py
node --test publicar-diagramas-google-docs/scripts/documento.test.mjs
python3 -m unittest discover -s publicar-diagramas-google-docs/scripts -p 'test_*.py'
```

Para cambios de renderizado, ejecutar además el preparador con los ejemplos
PlantUML y revisar sus PNG. Los comandos no requieren compilar otro proyecto.
