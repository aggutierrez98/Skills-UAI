---
name: tp-delivery-standards
description: Revisa criterios de entrega de un Trabajo de Diploma segun la consigna y el contexto del proyecto. Usar al preparar o revisar codigo, arquitectura, diagramas, documentacion y entregables de TD sin imponer un stack o una numeracion de requisitos particulares.
---

# Criterios de entrega del TD

## Entradas

Leer el contexto del proyecto (`TD-CONTEXTO.md`, AGENTS.md o equivalente), la
consigna vigente y el alcance pedido por el usuario. Identificar el stack,
arquitectura, evidencia esperada y comandos de verificacion que realmente use.

[La referencia de entrega](references/plan-entregas-resumen.md) organiza los
aspectos a revisar, pero no sustituye la Carpeta Modelo de la comision.

## Criterios

1. Respetar tecnologias y arquitectura declaradas por el estudiante y su consigna.
2. Mantener coherencia entre comportamiento implementado y documentado.
3. Identificar que partes son propuestas, implementadas o aun no verificadas.
4. Usar nombres reales de clases, operaciones, tablas y participantes.
5. Para diagramas de esta coleccion, conservar siempre fuentes `.puml` editables.
6. Ejecutar la compilacion/tests del proyecto cuando se cambie codigo. Una
   revision de Markdown o un renderizado no requiere por si solo MSBuild,
   SQL Server ni tests propios de otro sistema.
7. No modificar permisos, documentos externos o el comportamiento del sistema
   fuera del alcance solicitado.

## Diagramas y documento formal

Usar [tp-uml-y-casos-de-uso](../tp-uml-y-casos-de-uso/SKILL.md) para diagramar o
validar UML y casos de uso. Esa skill coordina la
[subskill PlantUML](embedded-skills/plantuml/SKILL.md) y la publicacion.

La diagramacion se realiza cuando el usuario la pide; no regenerar todos los
diagramas automaticamente despues de cualquier cambio de codigo. Si cambian
interfaces o flujos, identificar el impacto documental para el trabajo acordado.

## Cierre

- Requisitos de la entrega identificados y contrastados con la fuente vigente.
- Codigo y arquitectura coherentes cuando formen parte del alcance.
- Diagramas, CU y esquema de datos consistentes segun el alcance pedido.
- Fuentes y artefactos generados ubicados en las carpetas del proyecto.
- Documento actualizado y revisado cuando se haya pedido publicar.
- Comandos ejecutados, resultados y limitaciones informados.
