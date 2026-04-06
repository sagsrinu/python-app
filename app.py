from http.server import HTTPServer, BaseHTTPRequestHandler

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from EC2 ")

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Server running...")
server.serve_forever()
