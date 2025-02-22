#!/usr/bin/python3
"""
Module implementing a simple HTTP server.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Server(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for handling GET requests.
    """

    def do_GET(self):
        """
        Handle GET requests and send appropriate responses.
        """
        path = self.path
        if path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            dataj = json.dumps(data)
            self.wfile.write(dataj.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Endpoint not found".encode("utf-8")
            self.wfile.write(message)

def run(server_class=HTTPServer, handler_class=Server):
    """
    Start the HTTP server on localhost:8000.
    """
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
