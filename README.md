### Project Setup

```cmd

venv/Scripts/Activate.ps1

pip install pybind11

# Quick build and run
.\scripts\build_and_run.bat

# Just build when developing C++
.\scripts\build_and_run.bat -BuildOnly

# Just run when testing Python changes
.\scripts\build_and_run.bat -RunOnly

```