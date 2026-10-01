# Tsedal project context

Read `HANDOFF.md`, `README.md`, and `DEPLOYMENT.md` before changing this setup.

- The user explicitly chose native Frappe Bench, not Docker.
- Keep Tsedal's database, Redis, runtime data and ports isolated. Do not inspect or modify the user's other LMS instances.
- Track Tsedal customizations in this repository. Never commit credentials, site configuration, backups, uploads or runtime environments.
- The intended workflow is GitHub push/pull for code, with separate secure backup/restore for database content and files.
- The local MariaDB version is outside Frappe 15's tested range. Review database compatibility before VPS deployment; local smoke checks do not prove full compatibility.
