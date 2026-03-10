# Morfeo UGC Engine

Sistema autónomo de generación de contenido UGC. Genera 4 videos TikTok/Instagram por día con lip-sync, personajes generados por IA y plot twist de Morfeo Labs.

## Arquitectura

- **API** (`api/`) — Express.js en puerto 3336. Gestiona runs, cola de ejecución y estado del pipeline.
- **Pipeline** (`pipeline/`) — Python. Orquesta las etapas de generación: guión → personaje → escena → variaciones → video → publicación.

## Requisitos

- Node.js 18+
- Python 3.10+
- ffmpeg

## Instalación rápida

```bash
# 1. API
cd api
npm install
cp .env.example .env   # Configurar API keys
node server.js

# 2. Pipeline
cd ../pipeline
pip install -r requirements.txt
cp .env.example .env   # Configurar API keys
```

## Verificar instalación

```bash
curl http://localhost:3336/api/runs \
  -H "Authorization: Bearer $MORFEO_API_TOKEN" \
  -H "x-project-id: morfeo_labs"
# → debe devolver []
```

## Stages del pipeline

| Stage | Descripción |
|-------|-------------|
| `pending` | Esperando inicio |
| `brief` | Guión generado |
| `portrait` | Personaje diseñado |
| `hero` | Escena Morpheus generada |
| `multishot` | 10 variaciones generadas |
| `video` | Video con lip-sync listo |
| `published` | Publicado en redes |

## Costos por video

~$1.00 – $1.50 USD por video (Claude + ComfyDeploy + ElevenLabs + Gemini).

## Estructura

```
morfeo-engine/
├── api/           — Express API (puerto 3336)
├── pipeline/      — Pipeline Python (stages de generación)
├── output/        — Outputs por run (gitignored)
└── logs/          — Logs de ejecución (gitignored)
```
