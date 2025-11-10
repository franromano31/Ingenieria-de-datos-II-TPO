from fastapi import APIRouter, HTTPException
from app.models.models import (
    Paciente, Profesional, Turno, Habito, Riesgo, MetricaDashboard, LoginRequest
)
from app.crud import crud_operations as crud

router = APIRouter()

# -------------------------------
# PACIENTES
# -------------------------------
@router.post("/pacientes")
def create_paciente(paciente: Paciente):
    return crud.create_document("pacientes", paciente.dict())

@router.post("/login")
def login(login_request: LoginRequest):
    collection = "pacientes" if login_request.role == "patient" else "profesionales"
    user = crud.get_document_by_field(collection, "email", login_request.email)
    if user["password"] == login_request.password: #TODO: contraseña en texto plano, en produccion cambiar por hash
        return {"user":user}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    

@router.get("/pacientes")
def get_pacientes():
    return crud.get_all_documents("pacientes")

@router.get("/pacientes/{paciente_id}")
def get_paciente(paciente_id: str):
    paciente = crud.get_document_by_id("pacientes", paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/pacientes/{paciente_id}")
def update_paciente(paciente_id: str, paciente: Paciente):
    return crud.update_document("pacientes", paciente_id, paciente.dict())

@router.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: str):
    return crud.delete_document("pacientes", paciente_id)

# -------------------------------
# PROFESIONALES
# -------------------------------
@router.post("/profesionales")
def create_profesional(profesional: Profesional):
    return crud.create_document("profesionales", profesional.dict())

@router.get("/profesionales")
def get_profesionales():
    return crud.get_all_documents("profesionales")

# -------------------------------
# TURNOS
# -------------------------------
@router.post("/turnos")
def create_turno(turno: Turno):
    return crud.create_document("turnos", turno.dict())

@router.get("/turnos")
def get_turnos():
    return crud.get_all_documents("turnos")

@router.get("/turnos/paciente/{paciente_id}")
def get_turnos_by_paciente(paciente_id: str):
    turnos = crud.get_documents_by_field("turnos", "paciente_id", paciente_id)
    if not turnos:
        raise HTTPException(status_code=404, detail="No se encontraron turnos para este paciente")
    return turnos

# -------------------------------
# HABITOS
# -------------------------------
@router.post("/habitos")
def create_habito(habito: Habito):
    return crud.create_document("habitos", habito.dict())

@router.get("/habitos")
def get_habitos():
    return crud.get_all_documents("habitos")

# -------------------------------
# RIESGOS
# -------------------------------
@router.post("/riesgos")
def create_riesgo(riesgo: Riesgo):
    return crud.create_document("riesgos", riesgo.dict())

@router.get("/riesgos")
def get_riesgos():
    return crud.get_all_documents("riesgos")

# -------------------------------
# MÉTRICAS
# -------------------------------
@router.post("/metricas")
def create_metrica(metrica: MetricaDashboard):
    return crud.create_document("metricas_dashboard", metrica.dict())

@router.get("/metricas")
def get_metricas():
    return crud.get_all_documents("metricas_dashboard")
