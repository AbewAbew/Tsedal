# Tsedal

An isolated local Frappe Bench with Frappe Learning and a separate Tsedal customization app. Project directory: `/home/drse/Projects/tsedal`.

Open **http://tsedal.localhost:18780/lms**. Login at `/login` as **Administrator**. Run `./scripts/credentials` to view the generated password. Modern browsers resolve `*.localhost` locally; no hosts-file changes were made.

## Daily use

Run these from this project directory:

```bash
./scripts/up          # Start MariaDB, Redis, web, realtime, scheduler and worker
./scripts/status      # Show service status
./scripts/logs        # Follow service logs; Ctrl+C exits log viewing
./scripts/down        # Stop only Tsedal; data stays intact
./scripts/backup      # Back up the database, configuration and public/private files
./scripts/bench --site tsedal.localhost list-apps
```

The service is named `tsedal.service` and runs under your user. It is started on demand, not automatically at boot. `./scripts/start` is a foreground alternative; Ctrl+C stops the stack. Do not run foreground and background modes together. Start again with `./scripts/up` after a reboot.

Python changes require `./scripts/down && ./scripts/up`. For frontend changes, run `./scripts/bench build --production`. There is no asset watcher running by default.

## Isolation

| Service | Address |
| --- | --- |
| Website | 127.0.0.1:18780 |
| Socket.IO | 127.0.0.1:18790 |
| MariaDB | 127.0.0.1:18306 |
| Redis cache | 127.0.0.1:18379 |
| Redis queue and realtime messaging | 127.0.0.1:18380 |

Tsedal has its own MariaDB server process, data directory, socket, credentials and database named `tsedal`. It does not connect to the system database on port 3306. MariaDB reads only `.local/mariadb.cnf`. Redis uses this Bench's configuration and persistence files. Python packages, Bench CLI, Node 24 and Yarn are project-local. Python's interpreter and the MariaDB/Redis executables are shared system installations; upgrading those system binaries can affect this project.

Frappe's realtime log prints `0.0.0.0`, but the development launcher restricts the actual listener to `127.0.0.1`. No Docker containers are used.

## Code and GitHub

This directory is the Git repository and also the installable `tsedal` Frappe app. `bench/apps/tsedal` links back to it. Put your custom hooks, DocTypes, fixtures, assets and patches under `tsedal/`. Branding defaults are applied by `tsedal/install.py`. Later settings changes should be exported as targeted fixtures or implemented in migration patches when they need to travel through Git.

Upstream apps live in `bench/apps/frappe`, `bench/apps/payments` and `bench/apps/lms`; their source commits are recorded in `versions.json`. They are not included in this repository. If you need to change LMS's Vue frontend directly, create a separate LMS fork and record that fork and its commit. Changes inside the ignored `bench/` directory will not be pushed with this repository.

The shared LMS sidebar branding is maintained as an explicit exception in `patches/lms-branding.patch`. It removes the powered-by link, brands the administrator onboarding as Tsedal, and sends help links to `/tsedal-help`. The local `./scripts/bench build` wrapper checks/applies the patch before every build and stops if the upstream source is incompatible. The Help pages are part of this custom app and work for guests, students and administrators. Website footer and Desk Help menu settings are applied on app installation and migration by `tsedal.branding.apply_branding`.

On a server, from the Bench directory, run `python apps/tsedal/scripts/apply-lms-branding.py apps/lms` **before** `bench build --production`; run `bench --site YOUR_DOMAIN migrate` to apply the persistent settings. Do not discard the LMS patch during updates. If a separate LMS fork is created later, move this patch into the fork and update the deployment workflow accordingly.

When you have created the GitHub repository:

```bash
git remote add origin git@github.com:YOUR_ACCOUNT/tsedal.git
git push -u origin main
```

Future code changes use `git add`, `git commit` and `git push`. On a configured server, pull the Tsedal app repository, run `bench setup requirements`, `bench build --production`, `bench --site YOUR_DOMAIN migrate`, and restart that server's managed services. Back up before deploying changes. A Git pull alone does not install a server or migrate its database.

## Data and backups

`.local/`, `bench/`, backups, passwords, sessions, uploads and virtual environments are excluded from Git. Credentials are in `.local/credentials.json`; actual site database credentials and encryption keys are in `bench/sites/tsedal.localhost/site_config.json`. Do not commit these files.

`./scripts/backup` makes a Bench backup and copies it into `backups/` with private permissions. Copy backups off this PC. For migration, transfer the SQL backup, both file archives and the site configuration securely. Preserve the original `encryption_key`, but configure the new server's database connection separately. See [DEPLOYMENT.md](DEPLOYMENT.md).

## Versions and checks

Installed: Frappe 15.121.3, LMS 2.64.0, Payments 0.0.1, Tsedal 0.0.1, Bench 5.31.0, Python 3.11.16, Node 24.21.0 and Yarn 1.22.22. Exact app commits are in `versions.json`.

`config/dependency-locks/` records the resolved LMS frontend lockfile and Python package constraints. LMS's install regenerated its frontend lockfile and the build regenerated component types; these are generated upstream working-tree changes, not Tsedal customizations. To reproduce the frontend, copy the saved lockfile into the server's `apps/lms/frontend/yarn.lock` before running `yarn install --frozen-lockfile` there. The Python constraints are a dependency snapshot; app sources must still be installed from the recorded commits.

The local system provides MariaDB 12.3.3 and Valkey 9.1.2 through the Redis commands. Frappe 15 warns that this MariaDB version is outside its tested range. Site creation and local verification work, but this does not establish full compatibility. Use a Frappe-supported MariaDB version on the VPS and migrate using logical backups, not by copying the raw data directory. PDF printing requires a compatible wkhtmltopdf installation, which is not installed here. Email, payment gateways, and public HTTPS are not configured.

Run `.local/bench-cli/bin/python scripts/check.py` while Tsedal is running to verify its page, assets, branding, login, database API, realtime handshake and compressed SQL backup integrity. This is a smoke check, not the full upstream LMS test suite.

Local configuration can be regenerated with `python scripts/configure.py` and `./scripts/bench setup redis` while the stack is stopped. The development launchers are intended for this local workstation, not public hosting.
