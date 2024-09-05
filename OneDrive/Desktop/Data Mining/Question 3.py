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
    print(perms)
    return perms

# Function to compute combinations
def compute_combinations(lst, r):
    combs = list(itertools.combinations(lst, r))
    print(f"Combinations of {lst} with length {r}:")
    print(combs)
    return combs

# Profiling permutations
def profile_permutations():
    print("\n--- Permutations ---")
    perms_A = compute_permutations(A)
    perms_B = compute_permutations(B)
    perms_C = compute_permutations(C)
    perms_D = compute_permutations(D)
    perms_E = compute_permutations(E)

# Profiling combinations
def profile_combinations():
    print("\n--- Combinations ---")
    combs_A2 = compute_combinations(A, 2)
    combs_B2 = compute_combinations(B, 2)
    combs_C2 = compute_combinations(C, 2)
    combs_D2 = compute_combinations(D, 2)
    combs_E2 = compute_combinations(E, 2)

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
