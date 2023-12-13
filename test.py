#Python program to find nth rarest item in an array.
def nth_most_rate(list, n):
    # sort the array
    arr.sort()test.py
    # find the 1st rarest item in the array
    min_count = n + 1
    res = -1
    curr_count = 1
    for i in range (1, n):
        if (arr[i] == arr[i - 1]):
            curr_count = curr_count + 1
        else:
           if (curr_count < min_count):
               min_count = curr_count
               res = arr[i - 1]
        curr_count = 1
    # if last element is nth rarest item
    if (curr_count < min_count):
         min_count = curr_count
         res = arr[n - 1]
    return res
arr = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 1
print(nth_most_rate(arr, n))
