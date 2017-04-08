# Static webserver

Static http server, using env to determine the path of python. Listing current directory over at http://localhost:8000 (can also be reached by the computers LAN IP since it's serving on http://0.0.0.0:8000/).

## Python 2.x

```shell
$ env python -m SimpleHTTPServer 8000
```

## Python 3.x

```shell
$ env python3 -m http.server 8000
```