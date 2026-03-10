const express = require('express');
const router = express.Router();
const { createRun } = require('../lib/run-manager');
const marcasRouter = require('./marcas');

router.post('/add', (req, res) => {
  try {
    let { marca_id } = req.body || {};

    // If marca_id is null, pick a random brand
    if (!marca_id) {
      const marcas = marcasRouter.MARCAS;
      const random = marcas[Math.floor(Math.random() * marcas.length)];
      marca_id = random.id;
    }

    const run = createRun(marca_id, req.projectId);
    res.status(201).json(run);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
