# FastAPI + React Demo

This directory contains a minimal example of a FastAPI backend with a React frontend.
Persistent data is stored in `backend/data.pkl` using `pandas` and `pickle`.

## Running the backend

```bash
cd webapp/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API exposes:
- `GET /data` – list stored entries
- `POST /data` – add an entry using JSON `{ "name": str, "value": float }`

## Running the frontend

```bash
cd webapp/frontend
npm install
npm run dev
```

The frontend uses Vite and proxies requests starting with `/api` to the FastAPI backend running on port 8000.
