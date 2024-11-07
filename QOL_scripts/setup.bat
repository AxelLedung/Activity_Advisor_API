@echo off

cd ..
IF NOT EXIST venv (
    python -m venv venv
)

call venv/scripts/activate

echo Virtual environment 'venv' is now activated.
exit