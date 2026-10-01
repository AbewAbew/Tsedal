"""Create Tsedal once; keep generated credentials outside Git."""
import json
import os
from pathlib import Path
import secrets
import subprocess

root = Path(__file__).resolve().parent.parent
if (root / "bench/sites/tsedal.localhost/site_config.json").exists():
    raise SystemExit("Tsedal already exists; use Bench migrations or restore instead.")
os.umask(0o077)
path = root / ".local/credentials.json"
if path.exists():
    credentials = json.loads(path.read_text())
else:
    credentials = {key: secrets.token_urlsafe(30) for key in
                   ("database_admin_password", "administrator_password")}
    path.write_text(json.dumps(credentials, indent=2) + "\n")
password = credentials["database_admin_password"]
sql = "\n".join(
    f"CREATE USER IF NOT EXISTS 'tsedal_admin'@'{host}' IDENTIFIED BY '{password}';\n"
    f"GRANT ALL PRIVILEGES ON *.* TO 'tsedal_admin'@'{host}' WITH GRANT OPTION;"
    for host in ("localhost", "127.0.0.1")
)
subprocess.run(["mariadb", "--no-defaults", "--protocol=socket",
                f"--socket={root}/.local/run/mariadb.sock", "-u", os.environ["USER"]],
               input=sql, text=True, check=True)
subprocess.run([str(root / "scripts/bench"), "new-site", "tsedal.localhost",
                "--db-host", "127.0.0.1", "--db-port", "18306",
                "--db-name", "tsedal", "--db-root-username", "tsedal_admin",
                "--db-root-password", password,
                "--admin-password", credentials["administrator_password"],
                "--mariadb-user-host-login-scope", "127.0.0.1",
                "--install-app", "payments", "--install-app", "lms", "--set-default"],
               check=True)
