import os
from datetime import datetime
from wsgiref.simple_server import make_server


def app(environ, start_response):
    current_year = os.environ.get("PYGOTHAM_YEAR", datetime.now().year)
    url = f"https://{current_year}.pygotham.org"
    start_response("302 Moved Temporarily", [("Location", url)])
    return [url.encode()]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    with make_server("", port, app) as httpd:
        httpd.serve_forever()
