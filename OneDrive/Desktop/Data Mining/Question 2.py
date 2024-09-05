import cProfile
import pstats
import io
import numpy as np

# Define the list
data = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# I. Create a List
def create_list():
    return [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
def iterate_for_loop(lst):
    for item in lst:
        pass  # Replace pass with any operation if needed

# III. Iterate using for loop and range
def iterate_for_loop_range(lst):
    for i in range(len(lst)):
        item = lst[i]
        pass  # Replace pass with any operation if needed

# IV. List Comprehension
def list_comprehension(lst):
    return [x ** 2 for x in lst]

# V. Enumerate
def enumerate_function(lst):
    for index, item in enumerate(lst):
        pass  # Replace pass with any operation if needed

# VI. Iter function and next function
def iter_and_next(lst):
    iterator = iter(lst)
    for _ in lst:
        item = next(iterator)

# VII. Map function
def map_function(lst):
    return list(map(lambda x: x ** 2, lst))

# VIII. Using zip (Pairing the list with itself for demonstration)
def zip_function(lst):
    return list(zip(lst, lst))

# IX. Using NumPy Module
def numpy_operations(lst):
    np_data = np.array(lst)
    return np_data ** 2

# Profiling all operations
def profile_operations():
    pr = cProfile.Profile()
    pr.enable()

    create_list()
    iterate_for_loop(data)
    iterate_for_loop_range(data)
    list_comprehension(data)
    enumerate_function(data)
    iter_and_next(data)
    map_function(data)
    zip_function(data)
    numpy_operations(data)

    pr.disable()

    # Print profiling results
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()
    print(s.getvalue())

# Run the profiling
profile_operations()
