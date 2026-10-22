# DER desde la base de datos real (MSSQL Server)

Para crear o actualizar cualquier DER, **inspeccionar primero la estructura real de la base en
SQL Server** y replicarla fielmente. La base es la fuente de verdad de la persistencia; el DER
debe reflejar la version documentada y mantenerse balanceado con las migraciones/DDL y el codigo.

## Conexion del proyecto

Esta referencia es para SQL Server. Para otro motor, usar su catalogo de
metadatos y herramientas equivalentes. Obtener instancia, base y esquema de
la configuracion del proyecto; no hay una base predeterminada.

Ejemplo PowerShell con autenticacion integrada de Windows. Reemplazar los
valores antes de ejecutar y reutilizar las variables en las consultas:

```powershell
$Servidor = 'MI_INSTANCIA'
$Base = 'MI_BASE'
sqlcmd -S $Servidor -d $Base -E -Q "SELECT DB_NAME();"
```

Adaptar la autenticacion a la instalacion real sin guardar secretos en los
diagramas o documentos. Las consultas siguientes solo leen metadatos.

## Que extraer

Para el DER hay que obtener exactamente de la base: tablas, columnas con tipo y longitud,
nullabilidad, claves primarias, claves foraneas (con tabla/columna referenciada) y unicidad.

### Tablas y columnas (tipo, longitud, nullabilidad)

```powershell
sqlcmd -S $Servidor -d $Base -E -Q "
SET NOCOUNT ON;
SELECT t.TABLE_SCHEMA, t.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE,
       c.CHARACTER_MAXIMUM_LENGTH AS LEN, c.NUMERIC_PRECISION, c.NUMERIC_SCALE,
       c.IS_NULLABLE, c.ORDINAL_POSITION
FROM INFORMATION_SCHEMA.TABLES t
JOIN INFORMATION_SCHEMA.COLUMNS c ON c.TABLE_NAME = t.TABLE_NAME AND c.TABLE_SCHEMA = t.TABLE_SCHEMA
WHERE t.TABLE_TYPE = 'BASE TABLE'
ORDER BY t.TABLE_SCHEMA, t.TABLE_NAME, c.ORDINAL_POSITION;"
```

### Claves primarias

```powershell
sqlcmd -S $Servidor -d $Base -E -Q "
SET NOCOUNT ON;
SELECT tc.TABLE_SCHEMA, tc.TABLE_NAME, kcu.COLUMN_NAME, tc.CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
  ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME AND kcu.CONSTRAINT_SCHEMA = tc.CONSTRAINT_SCHEMA
WHERE tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
ORDER BY tc.TABLE_SCHEMA, tc.TABLE_NAME, kcu.ORDINAL_POSITION;"
```

### Claves foraneas (tabla/columna origen -> destino)

```powershell
sqlcmd -S $Servidor -d $Base -E -Q "
SET NOCOUNT ON;
SELECT fk.name AS FK, SCHEMA_NAME(tp.schema_id) AS ESQUEMA, tp.name AS TABLA, cp.name AS COLUMNA,
       SCHEMA_NAME(tr.schema_id) AS ESQUEMA_REF, tr.name AS TABLA_REF, cr.name AS COLUMNA_REF,
       fkc.constraint_column_id AS ORDEN
FROM sys.foreign_keys fk
JOIN sys.foreign_key_columns fkc ON fkc.constraint_object_id = fk.object_id
JOIN sys.tables tp  ON tp.object_id = fkc.parent_object_id
JOIN sys.columns cp ON cp.object_id = fkc.parent_object_id AND cp.column_id = fkc.parent_column_id
JOIN sys.tables tr  ON tr.object_id = fkc.referenced_object_id
JOIN sys.columns cr ON cr.object_id = fkc.referenced_object_id AND cr.column_id = fkc.referenced_column_id
ORDER BY SCHEMA_NAME(tp.schema_id), tp.name, fk.name, fkc.constraint_column_id;"
```

## Flujo de trabajo del DER

1. Confirmar conectividad y que la instancia/base sean las indicadas por el usuario.
2. Ejecutar las consultas de arriba para obtener tablas, columnas, PK y FK reales.
3. Construir el `.puml` del DER (subskill PlantUML, ver `er_diagrams.md`) replicando exactamente
   nombres de tablas, columnas, tipos, nullabilidad, PK y FK observadas.
4. Completar unicidad, indices, valores por defecto, checks y otros metadatos
   relevantes segun el alcance; las consultas anteriores son un punto de partida.
5. Cruzar con las migraciones/DDL del proyecto. Si difieren, registrar la
   discrepancia y confirmar que version se entrega antes de declarar el DER vigente.
6. Para un DER integrado, incluir las tablas acordadas y usar el codigo de
   requisito que corresponda a la consigna, sin asumir G07/G08.

## Si no hay acceso a la base

Si la instancia no esta disponible, avisar al usuario y, como ultimo recurso, derivar el DER de
las migraciones o DDL disponibles, dejando explicito que no se pudo validar contra la base real.
