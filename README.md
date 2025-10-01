### Project Setup

```cmd

venv/Scripts/Activate.ps1

pip install pybind11

mkdir build

cd build

cmake .. -G "Visual Studio 17 2022" -DPython_EXECUTABLE="C:/Python313/python.exe"

cmake --build .


# Quick build and run
.\build_and_run.bat

# Just build when developing C++
.\build_and_run.bat -BuildOnly

# Just run when testing Python changes
.\build_and_run.bat -RunOnly

```