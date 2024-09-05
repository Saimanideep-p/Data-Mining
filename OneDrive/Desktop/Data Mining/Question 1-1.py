import cProfile
import pstats
import io

# Define matrices
A = [[3.7827, 3.3454, 3.2341],
     [2.2122, 3.5678, 3.9087],
     [1.1234, 2.8934, 5.9087]]

B = [[3.1234, 3.0987, 3.1234],
     [2.1111, 3.2222, 3.3333],
     [1.0987, 1.3456, 5.1234]]

# Function to add matrices
def add_matrices(M1, M2):
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

# Function to multiply matrices
def multiply_matrices(M1, M2):
    return [[sum(M1[i][k] * M2[k][j] for k in range(len(M2))) for j in range(len(M2[0]))] for i in range(len(M1))]

# Profiling the matrix addition
def profile_addition():
    result_add = add_matrices(A, B)
    return result_add

# Profiling the matrix multiplication
def profile_multiplication():
    result_mul = multiply_matrices(A, B)
    return result_mul

# Create a stream for profiling results
pr = cProfile.Profile()
pr.enable()

# Run the functions you want to profile
profile_addition()
profile_multiplication()

pr.disable()

# Print profiling results
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
ps.print_stats()
print(s.getvalue())
