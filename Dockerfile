# ---- Base image ----
FROM python:3.11-slim

# ---- Working directory ----
WORKDIR /app

# ---- Copy dependencies ----
COPY requirements.txt .

# ---- Install dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy source ----
COPY . .

# ---- Expose FastAPI port ----
EXPOSE 8000

# ---- Run the app ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
