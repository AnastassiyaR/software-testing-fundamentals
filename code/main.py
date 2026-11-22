import math
from ctypes import POINTER, byref, c_double, c_int, cdll


DLL_PATH = r"testimisprojekt\quadratic.dll"

SOLUTION_OK = 0
ERROR_A_IS_ZERO = 1
ERROR_NO_REAL_ROOTS = 2
EPSILON = 1e-9


dll = cdll.LoadLibrary(DLL_PATH)
dll.setA.restype = None
dll.setA.argtypes = [c_double]
dll.setB.restype = None
dll.setB.argtypes = [c_double]
dll.setC.restype = None
dll.setC.argtypes = [c_double]
dll.getSolution.restype = c_int
dll.getSolution.argtypes = [POINTER(c_double), POINTER(c_double)]


def solve(a, b, c):
    dll.setA(a)
    dll.setB(b)
    dll.setC(c)
    x1, x2 = c_double(), c_double()
    status = dll.getSolution(byref(x1), byref(x2))
    return status, x1.value, x2.value

def ref(a, b, c):
    if a == 0:
        return ERROR_A_IS_ZERO, None, None
    d = b*b - 4*a*c
    if d < 0:
        return ERROR_NO_REAL_ROOTS, None, None
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return SOLUTION_OK, x1, x2

def check(name, a, b, c):
    status, x1, x2 = solve(a, b, c)
    exp_status, ex1, ex2 = ref(a, b, c)
    print("Expected: " + str(exp_status) +  " | " +  str(ex1) + "," + str(ex2))
    print("Actual: " + str(status) + ' | ' + str(x1) + "," + str(x2))
    status_ok = status == exp_status
    roots_ok = True
    if exp_status == SOLUTION_OK and status_ok:
        roots_ok = (
            (abs(x1 - ex1) < EPSILON and abs(x2 - ex2) < EPSILON) or
            (abs(x1 - ex2) < EPSILON and abs(x2 - ex1) < EPSILON)
        )
    result = "PASS" if (status_ok and roots_ok) else "FAIL"
    print(f"[{result}] {name}")
    if not status_ok:
        print(f"status: got {status}, expected {exp_status}")
    if not roots_ok:
        print(f"roots: got ({x1:.6f}, {x2:.6f}), expected ({ex1:.6f}, {ex2:.6f})")
    print("\n")

check("TC01 x^2-4=0", 1, 0, -4)
check("TC02 x^2-5x+6=0", 1, -5, 6)
check("TC03 x^2+2x+1=0", 1, 2, 1)
check("TC04 x^2+4=0", 1, 0, 4)
check("TC05 a=0", 0, 2, 1)
check("TC06 all zeros", 0, 0, 0)
check("TC07 x^2=0", 1, 0, 0)
check("TC08 2x^2+4x-6=0", 2, 4, -6)
check("TC09 -x^2+4=0", -1, 0, 4)
check("TC10 large b", 1, 1e6, 1)
print("TC11 stability (10 runs):")
results = [solve(1, 0, -4) for _ in range(10)]
for i, r in enumerate(results, 1):
    print(f"run {i:2d}: status={r[0]}, x1={r[1]:.6f}, x2={r[2]:.6f}")
all_same = all(r == results[0] for r in results)
print(f"[{'PASS' if all_same else 'FAIL'}]")

# Bugs
check("TC12 large a", 1e15, 1, -1)
check("TC13 tiny c", 1, 1, 1e-15)
check("TC12 large a", 1e15, 1, -1)
check("TC14 all negative", -2, -3, -1)
check("TC15 both roots negative", 1, 3, 2)
check("TC16 large roots", 1, -1e8, 1)
check("TC17 large a and c", 1e10, 1, 1e10)
