# Tsedal handoff — 2026-10-01

## User intent

Set up an isolated Frappe LMS named **Tsedal** in the Projects folder, using non-default ports. The user has other LMS instances and explicitly asked not to inspect them. The user chose **native Frappe Bench** and plans to create a GitHub repository, push code there, and pull it onto DigitalOcean or another VPS later.

## Completed

- Project and Git repository: `/home/drse/Projects/tsedal`, branch `main`.
- Initial setup commit: `4ccbb1c`.
- Frappe 15.121.3, LMS 2.64.0, Payments 0.0.1, and custom Tsedal app 0.0.1 installed. Exact source revisions are in `versions.json`.
- Custom app source is `tsedal/`; `bench/apps/tsedal` links to the repository root.
- Tsedal branding and Africa/Addis_Ababa timezone applied.
- Dedicated MariaDB data directory, server process, database/user credentials and socket. Dedicated Redis processes and persistence files.
- Project-local Bench CLI, Python virtual environments, Node and Yarn. The underlying Python interpreter and MariaDB/Redis executables are shared installed binaries.
- All service listeners are loopback-only: web `18780`, realtime `18790`, MariaDB `18306`, Redis cache `18379`, Redis queue `18380`.
- User service `tsedal.service` was running when setup finished. It is started on demand, not at boot; verify current status rather than assuming it remains running.
- Generated secrets and runtime files are ignored by Git. A scan of tracked files found none of the generated credentials.
- Database, site configuration, and public/private file backups were created successfully in the ignored `backups/` directory.

## Access and operations

- Site: `http://tsedal.localhost:18780/lms`; login at `/login` as `Administrator`.
- Run `./scripts/credentials` locally to see the password. Do not copy it into notes or Git.
- From the project directory: `./scripts/up`, `./scripts/down`, `./scripts/status`, `./scripts/logs`, `./scripts/backup`.
- Bench commands: `./scripts/bench --site tsedal.localhost <command>`.
- Smoke check: `.local/bench-cli/bin/python scripts/check.py` while services run.

## Verification completed

The LMS page and 43 referenced assets loaded; branding was Tsedal; Administrator login and the authenticated LMS database API succeeded; Socket.IO handshake passed; compressed SQL backup integrity passed. The full stack was stopped and restarted, then checks passed again. `bench doctor` reported one worker online. These are smoke checks, not a full LMS feature test suite or a backup restore test.

## Compatibility and remaining work

- **MariaDB compatibility:** local MariaDB is **12.3.3**. Frappe 15 warned that it is outside the tested range. Site creation and the checks above passed, but full compatibility is unproven. Before deploying to a VPS, select and verify a supported MariaDB version. Move data using logical backups, not the raw data directory. Do not downgrade the user's shared system installation as a shortcut.
- Local Redis commands use Valkey 9.1.2. Local background jobs worked.
- No GitHub remote has been configured or pushed. The user will create the repository; connect it when its URL is provided.
- Git push/pull transfers code only. Database content, users, progress, uploads and encryption keys require separate secure migration.
- Direct edits inside ignored `bench/apps/lms` will not travel with this repository. Use a separate LMS fork for upstream frontend changes; keep Tsedal customizations here when possible.
- Installation/build regenerated LMS frontend dependency and component files. The resolved frontend lockfile and Python dependency snapshot are saved under `config/dependency-locks/`.
- VPS provisioning, production process management, HTTPS, email and payment configuration remain for the deployment phase. Local launchers are development tooling.
- Compatible wkhtmltopdf is not installed; PDF printing/certificate export has not been verified.

See `README.md` for daily workflow and `DEPLOYMENT.md` for the server migration sequence.

## Follow-up: branding and Help

The user requested removal of the LMS powered-by footer and Tsedal branding throughout Help for administrators, students and guests. `patches/lms-branding.patch` tracks the shared sidebar change, preserves administrator onboarding, and points its help articles to the custom app's `/tsedal-help` pages. The local Bench wrapper applies/checks the patch before builds. The server deployment notes include the equivalent explicit patch step.

`tsedal.branding.apply_branding` runs on installation and migration. It suppresses the default website footer attribution and replaces upstream support/about entries in the Desk Help menu with Tsedal guides, preserving keyboard shortcuts and standard hidden rows. Public help content lives in `tsedal/help_content.py` and `tsedal/www/tsedal_help.*`.

Verified in Chromium: guest and authenticated student help links, the administrator Help panel and a documentation popup, absence of the shared powered-by icon, and mobile help layout. All 14 admin article destinations and the other public guides returned successfully. The public login footer and Desk Help menu settings were checked. The temporary student test account was removed afterward. The guest view still logs an upstream `frappe.apps.get_apps` permission error from its app-switcher resource; it does not block the help or branding changes.

The separate landing-page integration is **paused at the user's request** while they edit `/home/drse/Projects/tsedallms`. Partial landing assets/templates and `tsedal/landing_modules.json` are untracked drafts, not enabled `/en` or `/am` routes. Wait for the user to say the source is ready before resuming that work; do not commit those drafts as part of the branding change.
