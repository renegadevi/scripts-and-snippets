# Static webserver

Static http server on default port 8000, using env to determine the path of python. Directory listing over at http://localhost:8000 (can also be reached by the computers LAN IP since it's serving on http://0.0.0.0:8000/).

## Python 2.x

```shell
$ env python -m SimpleHTTPServer
```

## Python 3.x

```shell
$ env python3 -m http.server
```