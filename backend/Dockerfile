# ---------- Backend with FastAPI ----------
    FROM python:alpine
    WORKDIR /app
    
    # Install backend dependencies
    COPY backend/requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy backend code
    COPY backend ./backend
    
    
    EXPOSE 8080
    
    # Run the FastAPI app from inside /backend
    CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
    