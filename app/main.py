from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Vida Sana API")

# Incluir todas las rutas
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Vida Sana backend is running"}
