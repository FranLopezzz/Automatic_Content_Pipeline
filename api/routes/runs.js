const express = require('express');
const router = express.Router();
const { getRun, listRuns, advanceRun, updateRunState } = require('../lib/run-manager');
const logger = require('../lib/logger');

// GET /api/runs — list all runs
router.get('/', (req, res) => {
  try {
    const runs = listRuns(req.projectId);
    res.json(runs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// GET /api/runs/:id — get single run
router.get('/:id', (req, res) => {
  try {
    const run = getRun(req.params.id);
    if (!run) return res.status(404).json({ error: 'Run not found' });
    res.json(run);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST /api/runs/:id/advance — advance to next stage
router.post('/:id/advance', (req, res) => {
  try {
    const result = advanceRun(req.params.id);
    if (result.error) return res.status(400).json(result);
    res.json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST /api/runs/:id/regen-guion-field — regenerate script field
router.post('/:id/regen-guion-field', (req, res) => {
  try {
    const { field } = req.body || {};
    const validFields = ['HOOK', 'STORY_1', 'STORY_2', 'PLOT_TWIST', 'CTA'];

    if (!field || !validFields.includes(field)) {
      return res.status(400).json({ error: `Invalid field. Must be one of: ${validFields.join(', ')}` });
    }

    const run = getRun(req.params.id);
    if (!run) return res.status(404).json({ error: 'Run not found' });

    if (!run.brief) {
      return res.status(400).json({ error: 'Run has no brief yet. Advance to brief stage first.' });
    }

    logger.log(req.params.id, `Regenerating guion field: ${field}`);

    // Mark the field as pending regeneration
    run.brief[field] = `[REGENERATING ${field}...]`;
    updateRunState(req.params.id, { brief: run.brief });

    res.json({ message: `Field "${field}" queued for regeneration`, run_id: req.params.id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// PUT /api/runs/:id/shots-selection — select shots
router.put('/:id/shots-selection', (req, res) => {
  try {
    const { shots } = req.body || {};

    if (!Array.isArray(shots)) {
      return res.status(400).json({ error: 'shots must be an array of indices (0-9)' });
    }

    const run = getRun(req.params.id);
    if (!run) return res.status(404).json({ error: 'Run not found' });

    logger.log(req.params.id, `Shots selected: [${shots.join(', ')}]`);
    const updated = updateRunState(req.params.id, { selected_shots: shots });

    res.json({ message: 'Shots selection updated', selected_shots: shots, run_id: req.params.id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST /api/runs/:id/publish — publish to Postiz as draft
router.post('/:id/publish', (req, res) => {
  try {
    const run = getRun(req.params.id);
    if (!run) return res.status(404).json({ error: 'Run not found' });

    if (run.stage !== 'video') {
      return res.status(400).json({ error: `Cannot publish from stage "${run.stage}". Must be in "video" stage.` });
    }

    logger.log(req.params.id, 'Publishing to Postiz as DRAFT');
    const updated = updateRunState(req.params.id, { stage: 'published', published: true });

    res.json({ message: 'Published as DRAFT to Postiz', run_id: req.params.id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
