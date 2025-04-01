import random
import time

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces (maximum 8 elements): ")
    arr = list(map(int, user_input.split()))
    if len(arr) > 8:
        print("Error: The list can contain at most 8 elements.")
    else:
        print("Original list:", arr)
        start_time = time.time()
        sorted_arr = bogo_sort(arr)
        end_time = time.time()
        print("Sorted list:", sorted_arr)
        print(f"Time taken: {end_time - start_time:.6f} seconds")

