from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from masesora_backend.database.database import connect_to_mongo, close_mongo_connection

# Routers oficiales
from masesora_backend.routers.clients import router as clients_router
from masesora_backend.routers.contracts import router as contracts_router
from masesora_backend.routers.symptom_master import router as symptom_master_router
from masesora_backend.routers.catalog import router as catalog_router
from masesora_backend.routers.clinical_eval import router as clinical_eval_router
from masesora_backend.routers.clinical import router as clinical_router
from masesora_backend.routers.batch_router import router as batch_router

# Routers clínicos avanzados
from masesora_backend.onboarding.scanner_router import router as scanner_router
from masesora_backend.intake.intake_router import router as intake_router
from masesora_backend.clinical.progress.review_router import router as review_router
from masesora_backend.clinical.s10.s10_router import router as s10_router

app = FastAPI(title="MASESORA Backend – Motor Clínico Universal")

# -------------------------
# Routers oficiales
# -------------------------

# ❌ Desactivar por ahora (no necesarios para Fase 3)
# app.include_router(clients_router, prefix="/clients")
# app.include_router(contracts_router, prefix="/contracts")

# ✔ Mantener (solo lectura, no interfiere)
app.include_router(symptom_master_router, prefix="/symptom-master")
app.include_router(catalog_router, prefix="/catalog")

# -------------------------
# Motores clínicos
# -------------------------

# ❌ Desactivar motor clínico antiguo (interfiere con el nuevo)
# app.include_router(clinical_router, prefix="/clinical")

# ✔ Mantener motor clínico correcto
app.include_router(clinical_eval_router, prefix="/clinical-eval")

# ✔ Mantener batch
app.include_router(batch_router, prefix="/batch")

# -------------------------
# Flujo onboarding → intake → progreso → s10 → alta
# -------------------------

# ✔ ACTIVAR SCANNER (EPIC 1)
app.include_router(scanner_router, prefix="/onboarding")

# ❌ Desactivar flujos avanzados (no forman parte de Fase 3)
# app.include_router(intake_router, prefix="/intake")
# app.include_router(review_router, prefix="/review")
# app.include_router(s10_router, prefix="/s10")

# -------------------------
# CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)