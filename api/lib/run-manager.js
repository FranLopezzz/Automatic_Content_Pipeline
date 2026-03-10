const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { readJSON, writeJSON } = require('./store');
const logger = require('./logger');

const OUTPUT_DIR = path.join(__dirname, '..', '..', 'output');
const QUEUE_FILE = path.join(__dirname, '..', 'data', 'queue.json');

const STAGES = ['pending', 'brief', 'portrait', 'hero', 'multishot', 'video', 'published'];

function generateRunId() {
  const now = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  return `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}_${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}`;
}

function getRunDir(runId) {
  return path.join(OUTPUT_DIR, runId);
}

function getStatePath(runId) {
  return path.join(getRunDir(runId), 'state.json');
}

function createRun(marcaId, projectId) {
  const id = generateRunId();
  const runDir = getRunDir(id);
  fs.mkdirSync(runDir, { recursive: true });

  const state = {
    id,
    marca_id: marcaId || null,
    stage: 'pending',
    status: 'active',
    project_id: projectId,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    brief: null,
    portrait_url: null,
    hero_url: null,
    shots: [],
    selected_shots: [],
    video_url: null,
    published: false,
    error: null
  };

  writeJSON(getStatePath(id), state);

  // Add to queue
  const queue = readJSON(QUEUE_FILE) || [];
  queue.push({ id, marca_id: state.marca_id, project_id: projectId, created_at: state.created_at });
  writeJSON(QUEUE_FILE, queue);

  logger.log(id, `Run created | marca=${marcaId || 'random'} | project=${projectId}`);
  return state;
}

function getRun(runId) {
  return readJSON(getStatePath(runId));
}

function listRuns(projectId) {
  if (!fs.existsSync(OUTPUT_DIR)) return [];

  const dirs = fs.readdirSync(OUTPUT_DIR).filter(d => {
    const statePath = path.join(OUTPUT_DIR, d, 'state.json');
    return fs.existsSync(statePath);
  });

  const runs = dirs.map(d => readJSON(path.join(OUTPUT_DIR, d, 'state.json'))).filter(Boolean);

  if (projectId) {
    return runs.filter(r => r.project_id === projectId);
  }
  return runs;
}

function getNextStage(currentStage) {
  const idx = STAGES.indexOf(currentStage);
  if (idx === -1 || idx >= STAGES.length - 1) return null;
  return STAGES[idx + 1];
}

function advanceRun(runId) {
  const state = getRun(runId);
  if (!state) return { error: 'Run not found' };

  const nextStage = getNextStage(state.stage);
  if (!nextStage) return { error: `Cannot advance from stage "${state.stage}"` };

  // Spawn pipeline to execute the next stage
  const pythonPath = process.env.PYTHON_PATH || 'python';
  const pipelinePath = path.join(__dirname, '..', '..', 'pipeline', 'pipeline.py');

  logger.log(runId, `Advancing: ${state.stage} → ${nextStage}`);

  const child = spawn(pythonPath, [pipelinePath, '--run-id', runId, '--advance-one'], {
    cwd: path.join(__dirname, '..', '..'),
    env: { ...process.env },
    stdio: 'pipe'
  });

  child.stdout.on('data', (data) => {
    logger.log(runId, `[pipeline] ${data.toString().trim()}`);
  });

  child.stderr.on('data', (data) => {
    logger.log(runId, `[pipeline:err] ${data.toString().trim()}`);
  });

  child.on('close', (code) => {
    logger.log(runId, `Pipeline exited with code ${code}`);
  });

  return { message: `Advancing ${runId}: ${state.stage} → ${nextStage}`, run_id: runId };
}

function updateRunState(runId, updates) {
  const state = getRun(runId);
  if (!state) return null;

  Object.assign(state, updates, { updated_at: new Date().toISOString() });
  writeJSON(getStatePath(runId), state);
  return state;
}

module.exports = {
  createRun,
  getRun,
  listRuns,
  advanceRun,
  updateRunState,
  getNextStage,
  STAGES
};
