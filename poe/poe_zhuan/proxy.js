import express from 'express';
import request from 'request';
const app = express();
const PORT = 3000;

app.use('/api', (req, res) => {
  const url = `https://poe.game.qq.com${req.url.replace('/api', '')}`;
  req.pipe(request({ uri: url, headers: { 'Cookie': req.headers.cookie } })).pipe(res);
});

app.listen(PORT, () => {
  console.log(`Proxy server is running on http://localhost:${PORT}`);
});
