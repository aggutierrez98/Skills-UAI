# Catálogo y nombres por proyecto

Usar con [la skill central](../SKILL.md). Este archivo propone convenciones;
el catálogo real y los artefactos obligatorios se toman de la consigna/contexto
del estudiante. No hay una lista universal de CU ni una renumeración automática.

## Preparar el catálogo

Registrar por requisito o proceso:

| Campo | Ejemplo ficticio |
|---|---|
| Identificador y título | `solicitudes` / Gestión de solicitudes |
| Carpeta | `diagramas/solicitudes/` |
| Casos de uso | `CU01 · Registrar solicitud` |
| Artefactos acordados | Clases generales y secuencia de CU01 |
| Sección formal | Negocio → Solicitudes → CU01 |

Si se usan T0X, G0X o N0X, confirmar su significado y numeración con la comisión.
No cambiar los IDs que ya vinculan código, fuentes y documento.

## Nombres sugeridos

| Artefacto | Patrón |
|---|---|
| Clases | `<requisito>-clases.puml` |
| DER | `<requisito>-datos.puml` |
| Secuencia de CU | `<id-cu>-<accion>-secuencia.puml` |
| Componentes | `<requisito>-componentes.puml` |
| Actividad | `<requisito>-actividad.puml` |
| Especificación de CU | Nombre y formato acordados, por ejemplo `<id-cu>-<accion>.md` |

Preferir nombres únicos para PNG: el preparador detecta homónimos aunque las
fuentes vivan en carpetas diferentes. Guardar un diagrama completo por `.puml`.

No crear todas las carpetas por adelantado ni mover las existentes únicamente
para ajustarlas a estos ejemplos. Mantener el convenio del estudiante.

## Especificaciones

Usar los campos de la plantilla autorizada: actores, condiciones, escenario,
alternativas y resultados según corresponda. No se impone un JSON, un documento
por requisito ni una numeración global nueva.

Si se dispone de un generador propio, documentar su esquema y comandos. Las
skills externas `tp-use-case-spec` y `tp-carpeta-modelo` no se incluyen y no son
necesarias para crear/renderizar `.puml` con esta colección.
