require('dotenv').config();
const express = require('express');
const cors = require('cors');
const authMiddleware = require('./middleware/auth');
const runsRouter = require('./routes/runs');
const queueRouter = require('./routes/queue');
const marcasRouter = require('./routes/marcas');
const logsRouter = require('./routes/logs');

const app = express();
const PORT = process.env.PORT || 3336;

// Middleware
app.use(cors());
app.use(express.json());

// Auth on all /api routes
app.use('/api', authMiddleware);

// Routes
app.use('/api/runs', runsRouter);
app.use('/api/queue', queueRouter);
app.use('/api/marcas', marcasRouter);
app.use('/api/log', logsRouter);

// Health check (no auth)
app.get('/health', (req, res) => {
  res.json({ status: 'ok', engine: 'morfeo-ugc-engine', port: PORT });
});

app.listen(PORT, () => {
  console.log(`Morfeo UGC Engine API running on port ${PORT}`);
});
