from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HistoriaClinica(BaseModel):
    fecha: datetime
    diagnostico: str
    tratamiento: Optional[str] = None

class Paciente(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    historia_clinica: Optional[List[HistoriaClinica]] = []
    profesional_asignado: Optional[str] = None
    activo: bool = True
    password: str

class Profesional(BaseModel):
    nombre: str
    apellido: str
    especialidad: str
    email: str
    pacientes_ids: Optional[List[str]] = []
    activo: bool = True
    password: str

class Habito(BaseModel):
    paciente_id: str
    fecha: datetime
    sueno: dict
    alimentacion: dict
    actividad_fisica: Optional[dict]
    sintomas: Optional[List[str]] = []
    origen: Optional[str] = "manual"

class Turno(BaseModel):
    paciente_id: str
    profesional_id: str
    fecha: datetime
    motivo: Optional[str]
    estado: str = "pendiente"
    recordatorio_enviado: bool = False

class Riesgo(BaseModel):
    paciente_id: str
    score_riesgo: float
    factores: List[str]
    recomendaciones: List[str]
    fecha_calculo: datetime
    fuente: Optional[str] = "algoritmo_basico"

class MetricaDashboard(BaseModel):
    profesional_id: str
    total_pacientes: int
    promedio_sueno: float
    promedio_calorias: float
    promedio_riesgo: float
    ult_actualizacion: datetime
