# HTTP2Whois
Python script to easily use remote whois protocol from local HTTP server (for pentesting purposes)

## Prerequisites
- http.server
- socketserver
- argparse
- urllib

## Options

```bash
options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Host domain or IP
  -p PORT, --port PORT  HTTP server port
```

## Usage

```bash
$ python3 http2whois.py [-h] -H HOST [-p PORT]
```
## Screenshots

![Capture d’écran](https://github.com/mathis2001/HTTP2Whois/assets/40497633/2d882ba7-ecc4-4828-9c41-1ffd95e7ab1d)
![http2whois](https://github.com/mathis2001/HTTP2Whois/assets/40497633/5492ee36-7b8a-4865-b598-7ff354ae8274)
