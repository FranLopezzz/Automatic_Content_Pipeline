const fs = require('fs');
const path = require('path');

const LOGS_DIR = path.join(__dirname, '..', '..', 'logs');

function ensureLogsDir() {
  if (!fs.existsSync(LOGS_DIR)) {
    fs.mkdirSync(LOGS_DIR, { recursive: true });
  }
}

function log(runId, message) {
  ensureLogsDir();
  const timestamp = new Date().toISOString();
  const line = `[${timestamp}] ${message}\n`;
  const logFile = path.join(LOGS_DIR, `${runId}.log`);
  fs.appendFileSync(logFile, line, 'utf-8');
}

function readLog(runId) {
  const logFile = path.join(LOGS_DIR, `${runId}.log`);
  try {
    return fs.readFileSync(logFile, 'utf-8');
  } catch (err) {
    if (err.code === 'ENOENT') return '';
    throw err;
  }
}

module.exports = { log, readLog };
