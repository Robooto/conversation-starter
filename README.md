# Conversations
Conversations can be hard but probably shouldn't be but everyone needs a few ideas sometime.

## Running the app

```bash
docker-compose up --build --detach
```
UI - http://localhost:8887

API - http://localhost:8886/docs

## backend
Python api using fastapi

## frontend
Vuejs app

## Rebuilding for security updates

`docker compose build --pull --no-cache` refreshes the base images and OS packages. Every runtime image checks the minimum Debian Brotli security version during its build; the API uses supported Python 3.12 and updated FastAPI/Pydantic/SQLAlchemy dependencies. Existing SQLite table definitions and the default `conversations.db` location are unchanged. `DATABASE_URL` can select an isolated database for validation.

The UI uses patched Node 22.23.4 only for its build and ships Nginx, not Node. The existing Vue 2/Webpack 4 dependencies are retained; Webpack's legacy hash compatibility flag applies to the build command only. A full frontend dependency/framework migration remains separate work. The existing development-mode build and `.env.development` API URL behavior are preserved. Retain the deployment's local API URL overrides when rebuilding.

Before recreating the API, back up `api/conversations.db` consistently and preserve local UI settings. Building a candidate does not deploy it. Test locally from `api/` with `python -m pip install -r requirements-dev.txt` then `python -m unittest discover -s tests -v`; the tests use a disposable existing-schema fixture, never the deployment database.

See [Debian's CVE tracker](https://security-tracker.debian.org/tracker/CVE-2026-111497) for the backported fixed package versions. GitHub Actions builds both images and exercises the API against the pre-existing SQLite schema.
