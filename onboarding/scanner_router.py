from fastapi import APIRouter, HTTPException
from .scanner_schema import ScannerInput, ScannerOutput
from .scanner_service import process_scanner
from masesora_backend.reports.scanner_report import generate_scanner_pdf

router = APIRouter(
    prefix="/onboarding",
    tags=["Onboarding"]
)


@router.post("/scanner", response_model=ScannerOutput)
def submit_scanner(payload: ScannerInput):
    try:
        result = process_scanner(payload)

        # Generar PDF
        pdf_path = generate_scanner_pdf(result)
        result.pdf_url = pdf_path

        # Guardar resultado en memoria
        SCANNER_RESULTS[result.codigo] = result

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando el escáner: {str(e)}")