import numpy as np
import cProfile
import pstats
import io

# Define matrices using NumPy arrays
A = np.array([[3.7827, 3.3454, 3.2341],
              [2.2122, 3.5678, 3.9087],
              [1.1234, 2.8934, 5.9087]])

B = np.array([[3.1234, 3.0987, 3.1234],
              [2.1111, 3.2222, 3.3333],
              [1.0987, 1.3456, 5.1234]])

# Function to add matrices
def add_matrices_np(M1, M2):
    return M1 + M2

# Function to multiply matrices
def multiply_matrices_np(M1, M2):
    return np.dot(M1, M2)

# Profiling the matrix addition
def profile_addition_np():
    result_add = add_matrices_np(A, B)
    return result_add

# Profiling the matrix multiplication
def profile_multiplication_np():
    result_mul = multiply_matrices_np(A, B)
    return result_mul

# Create a stream for profiling results
pr = cProfile.Profile()
pr.enable()

# Run the functions you want to profile
profile_addition_np()
profile_multiplication_np()

pr.disable()

# Print profiling results
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
ps.print_stats()
print(s.getvalue())
