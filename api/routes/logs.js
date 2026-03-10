const express = require('express');
const router = express.Router();
const { readLog } = require('../lib/logger');

// GET /api/log?run_id=xxx
router.get('/', (req, res) => {
  try {
    const { run_id } = req.query;
    if (!run_id) {
      return res.status(400).json({ error: 'run_id query parameter is required' });
    }

    const logContent = readLog(run_id);
    const lines = logContent.split('\n').filter(Boolean);

    res.json({ run_id, entries: lines });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
