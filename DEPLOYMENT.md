# Moving Tsedal to a VPS

This repository contains the Tsedal app and local development tooling. A new VPS requires a separate production Bench installation before the push/pull workflow works. Do not expose `scripts/start` publicly.

The public site is intended for `tsedal.et`: `/en` and `/am` are the English and Amharic landing pages, `/` redirects to `/en`, and `/lms/courses` is the course catalogue. Configure HTTPS and the production `host_name` accordingly. See [LANDING.md](LANDING.md) for landing assets, routes and editing instructions.

## First deployment

1. Choose the domain and server, then provision supported Frappe 15 dependencies. Use a dedicated OS user, a compatible MariaDB release (Frappe 15's installation guide lists 10.6.6+), Redis, Python 3.11, Node 24 and Yarn. Verify current upstream support when deploying. Avoid upgrading to Frappe 16/17 as part of the initial move.
2. Install Bench 5.31.0 in a dedicated CLI environment. Initialize a production Bench with Frappe 15, and check out the Frappe commit in `versions.json`. Fetch and install Payments and LMS at their recorded commits. Run `bench setup requirements` after pinning their source revisions. Preserve the dependency snapshots in `config/dependency-locks/`; copy the saved frontend lockfile to `apps/lms/frontend/yarn.lock` and run `yarn install --frozen-lockfile` in that frontend directory before building.
3. Use `bench get-app --branch main https://github.com/AbewAbew/Tsedal.git` to install this custom app into the server Bench. The local service scripts will not be used there.
4. Create the domain's site with unique database and Administrator credentials. Install `payments`, `lms`, then `tsedal` for a fresh empty site; for a migration, restore the local site's backup with all these apps already available on the Bench.
5. On this PC, run `./scripts/backup`. Transfer the database SQL gzip, public/private file archives and site configuration securely. Keep them outside Git and public web paths.
6. Restore using the server Bench, substituting the real paths:

   ```bash
   bench --site YOUR_DOMAIN restore /secure/backup-database.sql.gz \
     --with-public-files /secure/backup-files.tgz \
     --with-private-files /secure/backup-private-files.tgz
   ```

   Preserve the original site's encryption key in the destination site configuration. Keep the destination's database host, port, name and password. Do not overwrite them with localhost development values.
7. Set `host_name` to `https://YOUR_DOMAIN`; disable `developer_mode`. From the server Bench, run `python apps/tsedal/scripts/apply-lms-branding.py apps/lms` before `bench build --production`. Then run `bench --site YOUR_DOMAIN migrate` and enable the scheduler. The patch preserves the Tsedal sidebar/Help branding; migration applies website footer and Desk Help settings.
8. Configure production process management, Gunicorn, nginx, HTTPS, firewall rules, email delivery and off-server backups. Keep the database and Redis private. Verify login, courses, uploads, background jobs and certificates before switching DNS traffic.

## Google login

Configure production Google login after `https://tsedal.et` is deployed with working HTTPS. Create a Google OAuth web application and register the exact callback URL:

```text
https://tsedal.et/api/method/frappe.integrations.oauth2_logins.login_via_google
```

Configure the Google provider in the site's Social Login Key settings, store the client secret outside Git, and test both existing-account login and new-user access. Keep username/password login available. Local testing is optional and should use separate development credentials with an explicitly registered localhost callback. Google login is not enabled in the current installation.

## Subsequent updates

Back up first. In the server's `apps/tsedal` checkout, pull the reviewed commit from GitHub. From the server Bench, install changed requirements, run `python apps/tsedal/scripts/apply-lms-branding.py apps/lms`, build assets, migrate the site and restart its services. If the branding patch check fails after an upstream update, review and refresh the patch before deploying. Changes to upstream app versions are separate, deliberate deployments using an updated `versions.json`.

Database content (courses, lessons, users, progress) and uploaded files do not travel through Git. Do not restore a development database over a live production database containing student activity.

## Upstream references

- [Frappe LMS source and installation](https://github.com/frappe/lms)
- [Frappe framework installation](https://docs.frappe.io/framework/user/en/installation)
- [Bench backup](https://docs.frappe.io/framework/user/en/bench/reference/backup)
- [Bench restore](https://docs.frappe.io/framework/user/en/bench/reference/restore)
