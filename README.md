# Local AI Customer Support Platform

FastAPI plus Ollama (`qwen3.5:4b`) for a fictional clothing-brand prototype called Threadlane.

## What is connected

- `POST /api/chat`: grounded support answers plus a single approved tool action.
- `lookup_order`: read-only lookup against fabricated records in `data/demo_orders.json`. Both order number and matching email are required. No live store is connected.
- `GET /api/actions`: shows the action registry.
- `GET /api/knowledge`: shows loaded FAQ and policy sections.
- `/owner`: local business setup page for brand voice, FAQ/policies, escalation guidance, and enabling the demo order action.

The model can request a tool, but the backend allowlists the function and validates its arguments before running it. The owner page controls whether the read-only lookup is enabled. It cannot change orders. The demo order details are fictional; the support rules are documented in `business/rules.md`.

## Add business policies

Use `/owner` to add confirmed policies, one section per `## Topic`. Settings are saved under `%LOCALAPPDATA%\\ThreadlaneSupport\\business_settings.json`, outside the project repository. Do not make up shipping, returns, or refund rules. Replace the demo order lookup with a real store integration only after the store platform and credentials are available.

## Run on Windows

Activate the virtual environment, ensure Ollama is running, then launch:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

The owner page has no sign-in and is intended for this loopback-only local prototype. Do not expose the development server to a network. Settings remain local and are not part of Git commits.

Open `http://127.0.0.1:8000/` for the customer chat, `http://127.0.0.1:8000/owner` for business setup, or `http://127.0.0.1:8000/docs` for the API reference.