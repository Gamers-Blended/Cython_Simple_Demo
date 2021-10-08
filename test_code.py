import run_python
import run_cython
import time

number = 10

# Python
start = time.time()
run_python.test(number)
end =  time.time()

py_time = end - start
print("Python time = {}".format(py_time))

# Cython
start = time.time()
run_cython.test(number)
end =  time.time()

cy_time = end - start
print("Cython time = {}".format(cy_time))

# Calculate ratio
print("Speedup = {}".format(py_time / cy_time))