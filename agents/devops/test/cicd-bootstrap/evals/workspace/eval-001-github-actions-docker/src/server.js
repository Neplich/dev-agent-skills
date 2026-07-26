import http from "node:http";

export function createServer() {
  return http.createServer((_request, response) => {
    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ status: "ok" }));
  });
}

if (process.env.NODE_ENV !== "test") {
  createServer().listen(3000);
}
