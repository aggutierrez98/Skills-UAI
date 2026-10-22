# Cómo colaborar

Esta colección reúne herramientas prácticas de estudiantes de TD. Son
bienvenidas las correcciones de instrucciones, ejemplos y scripts que puedan
servir a distintos proyectos.

## Proponer una mejora

1. Abrí un issue con el problema o proponé un cambio mediante pull request.
2. Explicá el escenario: asistente utilizado, sistema operativo, versiones y
   resultado esperado. Usá ejemplos ficticios si el material es privado.
3. Mantené las rutas relativas entre skills y actualizá el README si cambia
   la instalación, una dependencia o el alcance.
4. Ejecutá los comandos de verificación indicados en el README. Para cambios
   de renderizado, probá también PNG reales con PlantUML.

## Criterios de portabilidad

- Configurar el proyecto mediante su contexto; evitar nombres de alumnos,
  bases concretas, enlaces personales o rutas absolutas de una máquina.
- Diferenciar ejemplos/convenios de trabajo de requisitos oficiales de una
  comisión. Para corregir un requisito académico, indicar su fuente y versión.
- Mantener el código fuente `.puml` como artefacto editable y usar datos de
  ejemplo independientes de un sistema particular.
- No imponer un lenguaje, framework, motor de base o arquitectura que el
  proyecto del estudiante no haya declarado.
- Conservar imágenes existentes al completar documentos. Reconciliar el
  resultado después de un timeout antes de repetir escrituras.
- Describir capacidades requeridas de los conectores sin suponer que todos
  los asistentes tienen los mismos nombres de herramientas.
- Añadir casos de prueba útiles cuando se modifique el comportamiento de un
  script. Las pruebas de conectores deben usar un documento de prueba propio
  y una autorización explícita de su titular.

## Material de terceros

Conservá la atribución y las condiciones de distribución del material que
incorpores. No copies consignas, plantillas o documentos completos de cátedra
sin verificar que puedan redistribuirse. No incluyas credenciales ni snapshots
de documentos personales en el pull request.
