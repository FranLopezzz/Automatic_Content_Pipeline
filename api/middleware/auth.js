function authMiddleware(req, res, next) {
  const token = process.env.FRANLOPEZAZ_API_TOKEN;
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing Authorization header' });
  }

  const provided = authHeader.slice(7);
  if (provided !== token) {
    return res.status(401).json({ error: 'Invalid token' });
  }

  req.projectId = req.headers['x-project-id'] || 'franlopezaz_labs';
  next();
}

module.exports = authMiddleware;
