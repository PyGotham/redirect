from datetime import datetime
import os
from typing import List, TYPE_CHECKING
from wsgiref.simple_server import make_server

if TYPE_CHECKING:
    from wsgiref.types import StartResponse, WSGIEnvironment


def app(environ: "WSGIEnvironment", start_response: "StartResponse") -> List[bytes]:
    try:
        current_year = int(os.environ["PYGOTHAM_YEAR"])
    except (KeyError, ValueError):
        current_year = datetime.now().year
    url = f"https://{current_year}.pygotham.org"
    start_response("302 Moved Temporarily", [("Location", url)])
    return [url.encode()]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    with make_server("", port, app) as httpd:
        httpd.serve_forever()
