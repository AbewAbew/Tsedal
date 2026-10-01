# Tsedal landing page

The finished design from `~/Projects/tsedallms` is integrated into the custom Tsedal app. The original source directory is unchanged; `config/landing-source.json` records the imported file hashes.

## Routes

- `/` redirects to `/en` for all visitors.
- `/en` renders the English landing page.
- `/am` renders the Amharic landing page.
- `/lms/courses` opens the course catalogue.
- `/login?redirect-to=/lms/courses` opens real sign-in, then returns to courses.
- `/tsedal-help` remains the shared Help destination.

The language switcher and course links work without JavaScript. Landing-page language is determined by the URL; it does not change the account's LMS language preference. Header, hero, certificate-section and footer course links all use the same-origin catalogue route and work on localhost or the future production domain.

The prototype's Google sign-in simulation and editable destination modal were replaced with actual sign-in links and fixed relative course URLs. Google OAuth is not configured; if enabled later, the regular login page can offer it. Old demo `localStorage` destinations are ignored.

## Editing and deployment

- Shared page markup: `tsedal/templates/includes/landing.html`.
- Complete Amharic copy: `tsedal/landing_am.json`; English source text is in the template.
- Page controllers: `tsedal/www/en.py`, `tsedal/www/am.py`, and `tsedal/landing.py`.
- CSS, JavaScript and logo: `tsedal/public/landing/`.
- Three.js r128 is served locally from `vendor/`, with its license retained. Google Fonts remains an external font stylesheet, with system/Ethiopic font fallbacks.
- Reduced-motion preferences disable the ambient animation. A 2D fallback is used if WebGL is unavailable.

There is no separate landing-page server or frontend build process. Bench's asset linking serves the static files at `/assets/tsedal/landing/`. For a fresh server installation run `bench build --app tsedal` (or the normal full build) to create asset links. Restart the web processes and clear the website cache after changing Python controllers or translations. These files are tracked with the Tsedal app and travel through GitHub.

On the VPS configure the site domain, DNS, HTTPS and `host_name=https://tsedal.et`. The existing `/en` and `/am` routes then serve `https://tsedal.et/en` and `https://tsedal.et/am`; canonical and alternate-language URLs use that site configuration. No public-domain/DNS changes were made locally.

Run `bench/env/bin/python scripts/check-landing.py` from the local project to check routes, translation markers, canonical links, static assets and LMS destinations. Browser checks also cover desktop/mobile layout, language switching, real sign-in and course navigation, and operation without JavaScript.
