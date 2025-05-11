# ---------- Build frontend ----------
FROM node:slim AS frontend
    WORKDIR /app
    COPY frontend ./frontend
    WORKDIR /app/frontend
    RUN npm install
    RUN npm run build
    
    # ---------- Backend with FastAPI ----------
    FROM python:alpine
    WORKDIR /app
    
    # Install backend dependencies
    COPY backend/requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy backend code
    COPY backend ./backend
    
    # Copy exported static frontend files
    COPY --from=frontend /app/frontend/out ./frontend/out
    
    EXPOSE 8080
    
    # Run the FastAPI app from inside /backend
    CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
    