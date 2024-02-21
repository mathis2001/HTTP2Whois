import http.server
import socketserver
import subprocess
import argparse
from urllib.parse import urlparse, parse_qs

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", help="Host domain or IP", type=str, required=True)
parser.add_argument("-p", "--port", help="HTTP server port", type=int)
args = parser.parse_args()

class WhoisHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if 'whois' in query_params:
            domain = query_params['whois'][0]
            domain = domain.replace('"', '\\"') #.replace("'", "\\'")
            host = args.host

            whois_command = f'whois -h {host} -p 43 "{domain}"'

            try:
                result = subprocess.check_output(whois_command, shell=True, text=True)
                response = f"{result}"
            except subprocess.CalledProcessError as e:
                response = f"Error executing whois command: {e}"

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode())

        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bad Request: 'whois' parameter not provided")

if __name__ == "__main__":
    if args.port:
        PORT = args.port
    else:
        PORT = 8000
    with socketserver.TCPServer(("", PORT), WhoisHandler) as httpd:
        print(f"Serving on port {PORT}")
        print(f"You can now use whois protocol via 'http://localhost:{PORT}/?whois='")
        httpd.serve_forever()
