Set-Location ..

if (!(Test-Path -Path "venv")) {
    python -m venv venv
}

& "venv\Scripts\Activate.ps1"

Write-Output "Virtual environment 'venv' is now activated."

pip install -r requirements.txt

Set-Location ./QOL_scripts
python setup.py

Write-Host "Press any key to exit..."
$x = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

exit