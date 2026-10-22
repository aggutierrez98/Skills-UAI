---
name: tp-uml-y-casos-de-uso
description: Coordina diagramas PlantUML y especificaciones de casos de uso de un Trabajo de Diploma. Usar al crear, actualizar o validar clases, secuencias, DER u otros diagramas, contrastarlos con el codigo y preparar su publicacion en el documento del TP, respetando el stack y la consigna de cada estudiante.
---

# TP UML y casos de uso

Punto de entrada para diagramar un proyecto de TD y mantener coherencia entre
codigo, casos de uso, modelos de datos y documento de entrega.

## Contexto antes de actuar

1. Leer `TD-CONTEXTO.md` en la raiz del proyecto, o la documentacion equivalente
   que indique el usuario (AGENTS.md, arquitectura, consigna, catalogo).
2. Identificar alcance, stack, capas reales, fuentes y formato de entrega.
3. Confirmar que requisitos y tipos de diagramas se van a trabajar. Un pedido
   explicito de diagramacion ya autoriza ese alcance; preguntar solo lo faltante.
4. Si no hay contexto, pedir el minimo necesario. No asumir un framework,
   arquitectura, base, identificadores de CU o numeracion de otra comision.

La plantilla `ejemplos/TD-CONTEXTO.ejemplo.md` de la coleccion sirve de ayuda.
Su ubicacion puede no estar presente si se instalaron solo las carpetas de skills.

## Recursos que coordina

- Para crear, validar o renderizar `.puml`, leer
  [PlantUML](../tp-delivery-standards/embedded-skills/plantuml/SKILL.md) y su
  [guia de entorno](../tp-delivery-standards/embedded-skills/plantuml/references/entorno-proyecto.md).
- Para publicar PNG en Google Docs, leer
  [publicar-diagramas-google-docs](../publicar-diagramas-google-docs/SKILL.md).
- Para nombres y organizacion, consultar
  [catalogo-requisitos.md](references/catalogo-requisitos.md).
- Para sincronizacion documental, consultar
  [docs-sync-sources.md](references/docs-sync-sources.md).
- Para DER en SQL Server, consultar
  [der-desde-mssql.md](references/der-desde-mssql.md). En otros motores,
  inspeccionar sus metadatos con las herramientas correspondientes.

Las skills `tp-use-case-spec` y `tp-carpeta-modelo` no estan incluidas. Si el
usuario tiene equivalentes instalados, usarlos cuando corresponda. En caso
contrario, trabajar con la plantilla autorizada que aporte, sin inventar un
generador de `.docx` ni declarar bloqueado el diagramado por esas ausencias.

## Flujo de trabajo

1. Identificar requisito/proceso, CU y evidencia de comportamiento: codigo,
   especificacion aprobada y esquema de persistencia cuando aplique.
2. Acordar los artefactos requeridos segun la consigna. Clases, secuencia por
   CU, DER y vistas globales son opciones habituales; no imponerlas a todos
   los requisitos como si fueran una exigencia oficial universal.
3. Crear o actualizar fuentes bajo la carpeta acordada, por defecto
   `diagramas/<requisito>/`. Respetar estructura e IDs ya existentes; no mover
   ni renumerar material ajeno sin acuerdo.
4. Contrastar clases, atributos, operaciones, parametros y relaciones con el
   codigo. En secuencias, representar participantes reales (UI/controlador,
   servicios, repositorios u otros segun el proyecto), con activaciones y
   fragmentos `alt`/`opt`/`loop` donde sean relevantes.
5. Alinear escenario principal y alternativas del CU con sus interacciones.
   Para un modelo propuesto aun no implementado, identificarlo como tal y
   distinguirlo de lo observado en el codigo.
6. Para DER fisicos, inspeccionar la base o el esquema/migraciones disponible.
   Ante diferencias, registrar ambas evidencias y consultar cual representa
   la version de entrega; no modificar la base para que coincida con el dibujo.
7. Renderizar, validar sintaxis y revisar legibilidad a escala de documento.
   No usar una proporcion fija de ancho/alto para todos los tipos de diagrama.
8. Ejecutar los chequeos documentales y, si se cambio codigo, la compilacion o
   tests configurados por el proyecto. Informar los que no pudieron ejecutarse.
9. Publicar solo las fuentes aprobadas, manteniendo una correspondencia
   explicita entre archivos y encabezados del documento.

## Fuente de verdad

- Comportamiento implementado: codigo de la version que se documenta.
- UML editable: `.puml` guardados en el repositorio.
- Casos de uso: especificaciones aprobadas en el formato del proyecto.
- Persistencia: esquema inspeccionado y version de migraciones/DDL identificada.
- Entrega: documento formal que refleja esos artefactos.

Un pedido de cambiar texto del documento no autoriza por si solo modificar
comportamiento del sistema. Si describe una funcionalidad nueva, explicitarla
y acordar su implementacion antes de presentarla como existente.

## Checklist

- [ ] Requisito y alcance identificados segun la comision/proyecto.
- [ ] Fuentes `.puml` guardadas con nombres y ubicaciones acordadas.
- [ ] Clases y secuencias contrastadas con codigo o marcadas como propuestas.
- [ ] CU y secuencias coherentes, con identificadores preservados.
- [ ] DER contrastado con la fuente disponible y limitaciones registradas.
- [ ] Render sin errores y legible en la pagina de entrega.
- [ ] Documento destino confirmado, sin enlaces heredados de otros proyectos.
- [ ] Imagenes existentes conservadas salvo reemplazo solicitado.
- [ ] Verificaciones ejecutadas y resultados informados sin suposiciones.
