def linear_search(keys, target):
    """Find the index of target in a list of keys.
    Parameters:
        keys: a list of key values
        target: a value for which to search
    Return value:
        the index of an occurrence of target in keys
    """
    for i in range(len(keys)):
        if keys[i] == target:
            return i
    else:
        return -1

def binary_search(keys, target):
    """Find the index of target in a sorted list of keys.
    Parameters:
        keys: a list of key values
        target: a value for which to search
    Return value:
        the index of an occurrence of target in keys
        or None if the target does not occur in keys
    """
    n = len(keys)
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right, keys[mid])
        if target < keys[mid]:
            right = mid - 1
        elif target > keys[mid]:
            left = mid + 1
        else:
            while keys[mid] == keys[mid - 1]:
                mid = mid - 1
            return mid
    return right, left

data = ['B', 'E', 'N', 'N', 'N', 'N' , 'U', 'U']
print(binary_search(data, 'N'))
