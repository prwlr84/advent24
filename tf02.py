from tf02i import inputString
import numpy as np

# 1
data = [list(map(int, line.split())) for line in inputString.splitlines()]


def filter_arr(arr):
    diffs = np.abs(np.diff(arr))
    return np.all((1 <= diffs) & (diffs <= 3)) and (all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or all(
        arr[i] > arr[i + 1] for i in range(len(arr) - 1)))


print('First:', sum(map(filter_arr, data)))

# 2
passing, failing = [], []

for arr in data:
    (passing if filter_arr(arr) else failing).append(arr)

for arr in failing:
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1 or (0 < abs(arr[i - 1] - arr[i + 1]) < 4):
            variation = arr[:i] + arr[i + 1:]
            if filter_arr(variation):
                passing.append(arr)
                break

print('Second:', len(passing))

# 1 long
# data = [list(map(int, line.split())) for line in inputString.splitlines()]
#
#
# def filter_arr(arr):
#     if any(x > 3 or x < 1 for x in np.abs(np.diff(np.array(arr)))):
#         return False
#     is_increasing = all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
#     is_decreasing = all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))
#     if not is_increasing and not is_decreasing:
#         return False
#     return True
#
#
# print('First:', len(list(filter(filter_arr, data))))

# 2 long
# passing, failing = [], []
# for arr in data:
#     (passing if filter_arr(arr) else failing).append(arr)
#
# for arr in failing:
#     variations = []
#     for i in range(len(arr)):
#         if 0 < i < len(arr) - 1:
#             left = arr[i - 1]
#             right = arr[i + 1]
#             diff = abs(left - right)
#             if 0 < diff < 4:
#                 variations.append(arr[:i] + arr[i + 1:])
#         else:
#             # First or last element — no neighbor check
#             variations.append(arr[:i] + arr[i + 1:])
#
#     for v in variations:
#         if filter_arr(v):
#             passing.append(arr)
#             break
#
#
# print('Second:', len(passing))
