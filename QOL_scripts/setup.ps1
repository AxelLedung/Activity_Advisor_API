Set-Location ..

if (!(Test-Path -Path "venv")) {
    python -m venv venv
}

& "venv\Scripts\Activate.ps1"

Write-Output "Virtual environment 'venv' is now activated."

exit