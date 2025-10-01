@echo off
REM Build and Run Script for C++ Python Extension

setlocal enabledelayedexpansion

set CONFIG=Release
set BUILD_ONLY=0
set RUN_ONLY=0
set CLEAN=0

REM Parse command line arguments
:parse_args
if "%~1"=="" goto end_parse
if /i "%~1"=="-BuildOnly" set BUILD_ONLY=1
if /i "%~1"=="-RunOnly" set RUN_ONLY=1
if /i "%~1"=="-Clean" set CLEAN=1
if /i "%~1"=="-Config" (
    shift
    set CONFIG=%~1
)
shift
goto parse_args
:end_parse

echo.
echo === C++ Python Extension Build and Run ===
echo.

REM Change to project root directory
cd /d "%~dp0.."

REM Clean build if requested
if %CLEAN%==1 (
    echo =^> Cleaning build directory...
    if exist build rmdir /s /q build
    echo Build directory cleaned
    echo.
)

REM Skip build if RunOnly is specified
if %RUN_ONLY%==0 (
    REM Create build directory
    if not exist build (
        echo =^> Creating build directory...
        mkdir build
    )

    REM Configure CMake
    echo =^> Configuring CMake...
    cd build
    cmake .. -G "Visual Studio 17 2022" -DPython_EXECUTABLE="C:/Python313/python.exe"
    if errorlevel 1 (
        echo Error: CMake configuration failed
        exit /b 1
    )
    echo CMake configured successfully
    echo.

    REM Build the project
    echo =^> Building C++ module...
    cmake --build . --config %CONFIG%
    if errorlevel 1 (
        echo Error: Build failed
        exit /b 1
    )
    echo C++ module built successfully
    echo.

    cd ..
)

REM Skip Python execution if BuildOnly is specified
if %BUILD_ONLY%==0 (
    REM Run Python script from src/python directory
    echo =^> Running Python script...
    cd src\python
    python main.py
    if errorlevel 1 (
        echo Error: Python script execution failed
        exit /b 1
    )

    echo Python script executed successfully
    echo.
    cd ..\..
    
)

echo All operations completed successfully!
echo.