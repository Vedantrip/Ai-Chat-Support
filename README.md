# Local AI Customer Support Platform

FastAPI plus Ollama (`qwen3.5:4b`) for a fictional clothing-brand prototype called Threadlane.

## What is connected

- `POST /api/chat`: grounded support answers plus a single approved tool action.
- `lookup_order`: read-only lookup against fabricated records in `data/demo_orders.json`. Both order number and matching email are required. No live store is connected.
- `GET /api/actions`: shows the action registry.
- `GET /api/knowledge`: shows loaded FAQ and policy sections.

The model can request a tool, but the backend allowlists the function and validates its arguments before running it. It cannot change orders. The demo order details are fictional; the support rules are documented in `business/rules.md`.

## Add business policies

Add confirmed real policies to `knowledge/faq.md`, one section per `## Topic`. Do not make up shipping, returns, or refund rules. Replace the demo order lookup with a real store integration only after the store platform and credentials are available.

## Run on Windows

Activate the virtual environment, ensure Ollama is running, then launch:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/` for the chat page or `http://127.0.0.1:8000/docs` for the API reference.