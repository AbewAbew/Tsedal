"""Smoke check the running local site without printing credentials."""
import gzip
import json
from pathlib import Path
import re

import requests

root = Path(__file__).resolve().parent.parent
base = "http://127.0.0.1:18780"
session = requests.Session()
session.headers["Host"] = "tsedal.localhost:18780"

page = session.get(base + "/lms", timeout=30)
page.raise_for_status()
assert "<title>Tsedal</title>" in page.text
assets = set(re.findall(r'(?:src|href)="(/assets/[^"?#]+)', page.text))
assert assets, "No frontend assets found"
for asset in assets:
    session.get(base + asset, timeout=30).raise_for_status()
print(f"LMS page and {len(assets)} referenced assets: OK")

branding = session.get(base + "/api/method/lms.lms.api.get_branding", timeout=30)
branding.raise_for_status()
assert branding.json()["message"]["app_name"] == "Tsedal"
credentials = json.loads((root / ".local/credentials.json").read_text())
login = session.post(base + "/api/method/login", data={
    "usr": "Administrator", "pwd": credentials["administrator_password"]}, timeout=30)
login.raise_for_status()
assert login.json()["message"] == "Logged In"
identity = session.get(base + "/api/method/frappe.auth.get_logged_user", timeout=30)
identity.raise_for_status()
assert identity.json()["message"] == "Administrator"
courses = session.get(base + "/api/resource/LMS Course", timeout=30)
courses.raise_for_status()
print("Branding, Administrator login, and LMS database API: OK")

realtime = requests.get("http://127.0.0.1:18790/socket.io/?EIO=4&transport=polling", timeout=15)
realtime.raise_for_status()
assert realtime.text.startswith('0{')
print("Socket.IO handshake: OK")
for backup in (root / "backups").glob("*.gz"):
    with gzip.open(backup, "rb") as stream:
        while stream.read(1024 * 1024):
            pass
print("Compressed database backup integrity: OK")
