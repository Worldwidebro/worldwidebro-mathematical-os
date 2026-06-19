// Worldwidebro Staffing — standalone static web server (zero dependencies).
// Serves the marketing site in public/ and transparently proxies /api/* to the
// Staffing OS API (default :3000), so the request/apply forms hit the real backend.
//
//   node serve-web.js               # serves on :8080, proxies API to :3000
//   WEB_PORT=9000 API_PORT=3000 node serve-web.js
//
// To integrate directly into the main API server instead, add to src/server.ts:
//   import path from "path";
//   app.use(express.static(path.join(__dirname, "..", "public")));

const http = require("http");
const fs = require("fs");
const path = require("path");

const WEB_PORT = process.env.WEB_PORT || 8080;
const API_HOST = process.env.API_HOST || "127.0.0.1";
const API_PORT = process.env.API_PORT || 3000;
const ROOT = path.join(__dirname, "public");

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".ico": "image/x-icon",
  ".woff2": "font/woff2",
};

function proxyApi(req, res) {
  const opts = {
    host: API_HOST,
    port: API_PORT,
    path: req.url,
    method: req.method,
    headers: req.headers,
  };
  const upstream = http.request(opts, (up) => {
    res.writeHead(up.statusCode || 502, up.headers);
    up.pipe(res);
  });
  upstream.on("error", () => {
    res.writeHead(502, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "API unavailable on :" + API_PORT }));
  });
  req.pipe(upstream);
}

function serveStatic(req, res) {
  let urlPath = decodeURIComponent(req.url.split("?")[0]);
  if (urlPath === "/") urlPath = "/index.html";
  // pretty URLs: /clients -> /clients.html
  if (!path.extname(urlPath)) urlPath += ".html";

  const filePath = path.join(ROOT, urlPath);
  // prevent path traversal outside ROOT
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403).end("Forbidden");
    return;
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      fs.readFile(path.join(ROOT, "index.html"), (e2, fallback) => {
        if (e2) { res.writeHead(404).end("Not found"); return; }
        res.writeHead(404, { "Content-Type": MIME[".html"] });
        res.end(fallback);
      });
      return;
    }
    res.writeHead(200, { "Content-Type": MIME[path.extname(filePath)] || "application/octet-stream" });
    res.end(data);
  });
}

http
  .createServer((req, res) => {
    if (req.url.startsWith("/api")) return proxyApi(req, res);
    serveStatic(req, res);
  })
  .listen(WEB_PORT, () => {
    console.log(`Worldwidebro Staffing site → http://localhost:${WEB_PORT}`);
    console.log(`Proxying /api/* → http://${API_HOST}:${API_PORT}`);
  });
