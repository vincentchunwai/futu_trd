cmake_minimum_required(VERSION 3.10)
project(backtest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python first
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Set pybind11 to use the found Python
set(PYBIND11_PYTHON_VERSION ${Python_VERSION})
set(PYBIND11_FINDPYTHON ON)

include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.13.6 
)
FetchContent_MakeAvailable(pybind11)

# Create Python module
pybind11_add_module(backtest src/cpp/backtest.cpp)

# Copy the built module to the source directory for easy import
add_custom_command(TARGET backtest POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:backtest> ${CMAKE_SOURCE_DIR}/src/python
)