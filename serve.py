import os, http.server, socketserver

os.chdir(os.path.join(os.path.dirname(__file__), "블로그"))
PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
