import time
import random

# 📌 Bubble Sort Implementation
def bubble_sort(arr):
    """
    Bubble Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n = len(arr)
    # Loop through the entire list
    for i in range(n):
        # Last i elements are already sorted, so we skip them
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if they're in wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 📌 Selection Sort Implementation
def selection_sort(arr):
    """
    Selection Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n = len(arr)
    # Loop through the entire list
    for i in range(n):
        # Assume current position has the minimum value
        min_idx = i
        # Look for any smaller value in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of both sorting algorithms.
    """
    # Create test datasets
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    
    print("\n🔹 Small Dataset (50 elements):")
    
    # Bubble Sort test
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Large Dataset (1000 elements):")
    
    # Bubble Sort test
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort (for comparison)
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# Run the performance test
test_sorting_performance()