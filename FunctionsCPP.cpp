
// Creating the library:
//   g++ -o FunctionsCPP.so -shared FunctionsCPP.cpp


// Functions to be added to the library, note extern "C" macro prevents the compiler from changing the function's name (which is done in C++ to handle overloading, but was not in C since overloading was not supported)
#define EXPORT extern "C"

EXPORT double AddCPP(double num1, double num2) {
    return num1 + num2;
}

EXPORT void MultByTwoCPP(double* numArr, unsigned int numElem) {
    for (int i = 0; i < numElem; i++) {
        numArr[i] = numArr[i] * 2.0;
    }
}