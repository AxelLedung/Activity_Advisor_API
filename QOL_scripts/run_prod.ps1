Set-Location ..

& "venv\Scripts\Activate.ps1"

waitress-serve --port=8000 main:app