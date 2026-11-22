# Quadratic dll testing

Black-box testing of the dynamic link library `quadratic.dll`, which solves
quadratic equations of the form `a*x^2 + b*x + c = 0`.
Project for the course "Fundamentals of Software Testing", TalTech, 2026.

## What was tested

The library was tested through its public interface only (`setA`, `setB`,
`setC`, `getSolution`) using a Python script and `ctypes`.
Methods: equivalence partitioning, boundary value testing, repeat tests.
11 test cases (TC01-TC11) and 6 reported bugs (TC12-TC17).

## Test environment

Windows 11, Python 3.13, `quadratic.dll` in the same folder as the script.
