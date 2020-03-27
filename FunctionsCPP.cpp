
// Creating the library via command line:
//   g++ -o FunctionsCPP.so -shared FunctionsCPP.cpp

// To create library in visual studio:
//   Create dll project
//   Change the build configuration to x64 NOTE THIS MUST BE DONE BEFORE DISABLING PRECOMPILED HEADERS OR YOU'll JUST HAVE TO DO IT AGAIN
//   Disable precompiled headers, and delete all the nonsense VS creates like dllmain and pch.h make sure to delete both the headers and the source files
//   Copy this file into a source file in VS
//   Build the solution, and the dll will be placed in the x64/debug in the project folder


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

EXPORT void MultByTwo2DCPP(double* numArr, unsigned int xDim, unsigned int yDim) {
    for (int j = 0; j < yDim; j++) {
        for (int i = 0; i < xDim; i++) {
            numArr[j * xDim + i] = numArr[j * xDim + i] * 2.0;
        }
    }
}