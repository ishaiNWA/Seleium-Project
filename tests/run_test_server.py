import http.server
import socketserver
import os
from pathlib import Path

def run_server(port=8000):
    # Change to the directory containing test_links.html
    os.chdir(Path(__file__).parent / 'resources')
    
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at port {port}")
        print(f"Test page URL: http://localhost:{port}/test_links.html")
        print("Press CTRL+C to stop the server.")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
