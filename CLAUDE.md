# Morfeo UGC Engine — Agent Instructions

## Qué es este proyecto

Motor autónomo de generación de videos UGC para marcas argentinas. Dos componentes:
- **API** (Node.js/Express, puerto 3336) — gestiona runs y cola
- **Pipeline** (Python) — ejecuta stages de generación con APIs externas

## Endpoints principales

```
GET  /api/runs                        — Listar runs
GET  /api/runs/:id                    — Detalle de un run
POST /api/queue/add                   — Crear run nuevo
POST /api/runs/:id/advance            — Avanzar al siguiente stage
POST /api/runs/:id/regen-guion-field  — Regenerar campo del guión
PUT  /api/runs/:id/shots-selection    — Seleccionar shots
POST /api/runs/:id/publish            — Publicar como draft
GET  /api/marcas                      — Listar marcas disponibles
GET  /api/log?run_id=xxx              — Ver log de ejecución
```

Headers requeridos: `Authorization: Bearer $MORFEO_API_TOKEN` + `x-project-id: morfeo_labs`

## Stages

pending → brief → portrait → hero → multishot → video → published

## Convenciones

- Run ID: formato `YYYYMMDD_HHMMSS`
- Estado de cada run: `output/{run_id}/state.json`
- Logs: `logs/{run_id}.log`
- Datos persistentes: JSON files en `api/data/`
- Pipeline se invoca via `child_process.spawn` desde la API
