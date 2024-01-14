import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

small_data = [random.randint(0, 2_000) for _ in range(2_000)]
medium_data = [random.randint(0, 11_000) for _ in range(11_000)]
big_data = [random.randint(0, 20_000) for _ in range(20_000)]

time_small_insertion = timeit.timeit(lambda: insertion_sort(small_data[:]), number=11)
time_small_merge = timeit.timeit(lambda: merge_sort(small_data[:]), number=11)
time_small_timsort = timeit.timeit(lambda: sorted(small_data[:]), number=11)
time_small_timsort_s = timeit.timeit(lambda: small_data[:].sort(), number=11)

time_medium_insertion = timeit.timeit(lambda: insertion_sort(medium_data[:]), number=11)
time_medium_merge = timeit.timeit(lambda: merge_sort(medium_data[:]), number=11)
time_medium_timsort = timeit.timeit(lambda: sorted(medium_data[:]), number=11)
time_medium_timsort_s = timeit.timeit(lambda: medium_data[:].sort(), number=11)

time_big_insertion = timeit.timeit(lambda: insertion_sort(big_data[:]), number=11)
time_big_merge = timeit.timeit(lambda: merge_sort(big_data[:]), number=11)
time_big_timsort = timeit.timeit(lambda: sorted(big_data[:]), number=11)
time_big_timsort_s = timeit.timeit(lambda: big_data[:].sort(), number=11)

print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time big data': <20}")
print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f}) | {time_big_insertion:<20.5f}")
print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}) | {time_big_merge:<20.5f}")
print(f"{'| Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}) | {time_big_timsort:<20.5f}")
print(f"{'| Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f}) | {time_big_timsort_s:<20.5f}")