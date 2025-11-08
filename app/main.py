from fastapi import FastAPI
from app.api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Vida Sana API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # o ["*"] durante desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todas las rutas
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Vida Sana backend is running"}
