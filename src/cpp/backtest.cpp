#include <pybind11/pybind11.h>


bool backtest() 
{
    return true;
}



PYBIND11_MODULE(backtest, m) {
    m.doc() = "backtest module";
    m.def("backtest", &backtest, "A Backtest function");
}