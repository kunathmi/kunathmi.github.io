"""
serve.py  —  Local preview server for the built portfolio site.

Usage:
    uv run python serve.py          # serves on http://localhost:8000
    uv run python serve.py 9000     # serves on http://localhost:9000

This serves the docs/ directory (the output of build.py) using Python's
built-in HTTP server — no additional dependencies required.
Press Ctrl+C to stop.
"""

import http.server
import os
import sys
import webbrowser
from pathlib import Path

DOCS_DIR = Path(__file__).parent / "docs"
DEFAULT_PORT = 8000


def main() -> None:
    # Allow an optional port argument: `uv run python serve.py 9000`
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT

    if not DOCS_DIR.exists():
        sys.exit(
            "Error: docs/ directory not found.\n"
            "Run  uv run python build.py  first to generate the site."
        )

    # Change working directory to docs/ so the server resolves paths correctly
    os.chdir(DOCS_DIR)

    url = f"http://localhost:{port}"
    print(f"Serving portfolio from  docs/  at  {url}")
    print("Press Ctrl+C to stop.\n")

    # Open the browser automatically
    webbrowser.open(url)

    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
