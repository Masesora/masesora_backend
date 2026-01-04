# Ir a la raíz del proyecto
cd "C:\Users\Masesora\OneDrive\MASESORA\CLINICA"

# Establecer PYTHONPATH para que Python reconozca masesora_backend como módulo
$env:PYTHONPATH="C:\Users\Masesora\OneDrive\MASESORA\CLINICA"

# Lanzar FastAPI en una nueva ventana para evitar bloqueo
Start-Process powershell -ArgumentList 'uvicorn masesora_backend.main:app --reload'

# Abrir Swagger automáticamente
Start-Process "http://localhost:8000/docs"