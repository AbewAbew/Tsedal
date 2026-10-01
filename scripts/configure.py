"""Generate local-only service configuration; never reads another bench."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
local = root / ".local"
local.mkdir(mode=0o700, exist_ok=True)
(local / "run").mkdir(exist_ok=True)
(local / "logs").mkdir(exist_ok=True)
(local / "mariadb.cnf").write_text(f"""[mysqld]
datadir={local}/mariadb
socket={local}/run/mariadb.sock
pid-file={local}/run/mariadb.pid
log-error={local}/logs/mariadb.log
bind-address=127.0.0.1
port=18306
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci
skip-name-resolve
innodb-buffer-pool-size=256M

[client]
socket={local}/run/mariadb.sock
port=18306
""")
config_path = root / "bench/sites/common_site_config.json"
if config_path.exists():
    config = json.loads(config_path.read_text())
    config.update(db_host="127.0.0.1", db_port=18306,
                  redis_cache="redis://127.0.0.1:18379",
                  redis_queue="redis://127.0.0.1:18380",
                  redis_socketio="redis://127.0.0.1:18380",
                  webserver_port=18780, socketio_port=18790,
                  socketio_host="127.0.0.1", file_watcher_port=18781,
                  serve_default_site=True, default_site="tsedal.localhost",
                  restart_supervisor_on_update=False, restart_systemd_on_update=False)
    config_path.write_text(json.dumps(config, indent=2) + "\n")
    (root / "bench/Procfile").write_text((root / "config/Procfile").read_text())
