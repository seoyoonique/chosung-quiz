import os, http.server, socketserver

os.chdir(os.path.join(os.path.dirname(__file__), "한글타이포"))
PORT = 3001
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
