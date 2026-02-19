# Syntax -> np.isnan(array)
import numpy as np

# arr = np.array([1, 2, np.nan, 4, np.nan])

# It uses to find missing values in array
# print(np.isnan(arr))

# Syntax -> np.nan_to_num(array, nan = value) default value = 0

# arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# # It replaces the nan to given value in array
# cleaned_arr = np.nan_to_num(arr, nan=100)
# print(cleaned_arr)

# Syntax -> np.isinf(array)

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

# It uses to find the infinite value in array
print(np.isinf(arr))

# It replaces the infinite values in array
cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=1000)
print(cleaned_arr)


