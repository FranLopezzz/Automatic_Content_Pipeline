# Franlopezaz UGC Engine Skill

Sistema autónomo de generación de videos UGC para marcas argentinas.
Genera contenido TikTok/Instagram que parece orgánico pero termina con un plot twist revelando que es IA de Franlopezaz Labs.

## Cuándo usar esta skill

Cuando Paul pida:
- "generá un video de [marca]"
- "corré el pipeline"
- "qué runs hay en curso"
- "avanzá el run de [marca] al siguiente paso"
- "mostrá el estado del engine"
- "publicá el video de [run]"
- Cualquier operación sobre el Franlopezaz UGC Engine

---

## Configuración

### API Local
- **Base URL**: `http://localhost:3336`
- **Token**: Configurado en `api/.env` como `FRANLOPEZAZ_API_TOKEN`
- **Auth header**: `Authorization: Bearer $FRANLOPEZAZ_API_TOKEN`
- **Project header**: `x-project-id: franlopezaz_labs`

### Proyectos disponibles
- `franlopezaz_labs` — Pipeline principal (productos argentinos)
- `animado` — Variante estilo animado

---

## Endpoints principales

```bash
BASE="http://localhost:3336"
TOKEN="$FRANLOPEZAZ_API_TOKEN"
H_AUTH="Authorization: Bearer $TOKEN"
H_PROJ="x-project-id: franlopezaz_labs"
```

### Ver todos los runs
```bash
curl -s "$BASE/api/runs" -H "$H_AUTH" -H "$H_PROJ"
```

### Crear run nuevo (marca aleatoria)
```bash
curl -s -X POST "$BASE/api/queue/add" \
  -H "$H_AUTH" -H "$H_PROJ" -H "Content-Type: application/json" \
  -d '{"marca_id": null}'
```

### Crear run con marca específica
```bash
curl -s -X POST "$BASE/api/queue/add" \
  -H "$H_AUTH" -H "$H_PROJ" -H "Content-Type: application/json" \
  -d '{"marca_id": "havanna"}'
```

### Ver estado de un run
```bash
curl -s "$BASE/api/runs/$RUN_ID" -H "$H_AUTH" -H "$H_PROJ"
```

### Avanzar run a la siguiente etapa
```bash
curl -s -X POST "$BASE/api/runs/$RUN_ID/advance" \
  -H "$H_AUTH" -H "$H_PROJ"
```

### Regenerar campo del guión
```bash
# campos: HOOK, STORY_1, STORY_2, PLOT_TWIST, CTA
curl -s -X POST "$BASE/api/runs/$RUN_ID/regen-guion-field" \
  -H "$H_AUTH" -H "$H_PROJ" -H "Content-Type: application/json" \
  -d '{"field": "HOOK"}'
```

### Seleccionar shots para el video (índices 0-9)
```bash
curl -s -X PUT "$BASE/api/runs/$RUN_ID/shots-selection" \
  -H "$H_AUTH" -H "$H_PROJ" -H "Content-Type: application/json" \
  -d '{"shots": [0, 2, 4, 6, 8]}'
```

### Publicar en redes (Postiz → borrador)
```bash
curl -s -X POST "$BASE/api/runs/$RUN_ID/publish" \
  -H "$H_AUTH" -H "$H_PROJ"
```

### Ver log de ejecución
```bash
curl -s "$BASE/api/log?run_id=$RUN_ID" -H "$H_AUTH" -H "$H_PROJ"
```

### Ver marcas disponibles
```bash
curl -s "$BASE/api/marcas" -H "$H_AUTH" -H "$H_PROJ"
```

---

## Stages del pipeline

| Stage | Descripción |
|-------|-------------|
| `pending` | Esperando inicio |
| `brief` | Guión generado ✓ |
| `portrait` | Personaje diseñado ✓ |
| `hero` | Escena Morpheus generada ✓ |
| `multishot` | 10 variaciones generadas ✓ |
| `video` | Video con lip-sync listo ✓ |
| `published` | Publicado en redes ✓ |

---

## Flujo completo manual

```
1. Crear run con marca → POST /api/queue/add
2. Esperar brief (stage=brief) → ver guión y personaje
3. Si guión ok → POST /advance
4. Esperar portrait (stage=portrait) → ver imagen del personaje
5. Si personaje ok → POST /advance
6. Esperar hero (stage=hero) → ver escena Morpheus
7. Si escena ok → POST /advance
8. Esperar multishot (stage=multishot) → ver 10 shots
9. Seleccionar 5 mejores → PUT /shots-selection
10. POST /advance → genera videos con lip-sync
11. Esperar video (stage=video) → ver video final
12. Si ok → POST /publish → borrador en Postiz
```

---

## Operaciones de diagnóstico

### Verificar que la API está levantada
```bash
curl -s http://localhost:3336/api/runs \
  -H "Authorization: Bearer $FRANLOPEZAZ_API_TOKEN" \
  -H "x-project-id: franlopezaz_labs"
```

### Ver logs
```bash
pm2 logs franlopezaz-engine-api --lines 50
```

---

## Marcas disponibles (pool principal)

Havanna, Bon o Bon, Topper, Mantecol, Stella Artois, Andes Origen, Quilmes, Fernet Branca, Yerba Taragüí, Dulce de Leche La Serenísima, Alfajores Terrabusi, CasanCrem, Freddo, Ketchup Heinz, Mayonesa Hellmann's.

---

## Notas importantes

- **Postiz siempre a DRAFT** — nunca publicar directo
- El pipeline puede tardar 10-30 min por etapa (ComfyDeploy + VEED)
- Los outputs se guardan en `output/YYYYMMDD_HHMMSS/`
