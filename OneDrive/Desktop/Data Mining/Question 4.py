import cProfile
import pstats
import io
import itertools

# Define lists
A = [1, 2]
B = [3, 4]
C = [5, 6]
D = [7, 8]
E = [9, 10]

# Function to compute permutations
def compute_permutations(lst):
    perms = list(itertools.permutations(lst))
    print(f"Permutations of {lst}:")
    for perm in perms:
        print(perm)
    return perms

# Function to compute combinations
def compute_combinations(lst, r):
    combs = list(itertools.combinations(lst, r))
    print(f"Combinations of {lst} with length {r}:")
    for comb in combs:
        print(comb)
    return combs

# Profiling permutations
def profile_permutations():
    print("\n--- Permutations ---")
    compute_permutations(A)
    compute_permutations(B)
    compute_permutations(C)
    compute_permutations(D)
    compute_permutations(E)

# Profiling combinations
def profile_combinations():
    print("\n--- Combinations ---")
    compute_combinations(A, 2)
    compute_combinations(B, 2)
    compute_combinations(C, 2)
    compute_combinations(D, 2)
    compute_combinations(E, 2)

# Profiling all operations
def profile_operations():
    pr = cProfile.Profile()
    pr.enable()

    profile_permutations()
    profile_combinations()

    pr.disable()

    # Print profiling results
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()
    print("\n--- Profiling Results ---")
    print(s.getvalue())

# Run the profiling
profile_operations()
