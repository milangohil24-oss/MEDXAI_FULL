# MEDXAI Frontend

Futuristic spatial React frontend for the existing MedXAI FastAPI + MongoDB backend.

## Run

```cmd
npm install
copy .env.example .env.local
npm run dev
```

Default backend:
`http://127.0.0.1:8000`

Change `VITE_API_BASE_URL` in `.env.local` if needed.

## Expected backend routes

- POST /auth/register
- POST /auth/login
- GET /auth/me
- POST /auth/logout
- POST /auth/change-password
- POST /predict
- GET /analyses
- GET /analyses/{id}
- DELETE /analyses/{id}
- GET /dashboard/stats
- GET /profile
- PUT /profile
- GET /reports
- POST /reports/{analysis_id}
- GET /reports/{report_id}/download
- POST /explain/lime

The API layer is centralized in `src/services/api.ts`, so if your backend uses different route names, update them there rather than changing every page.
