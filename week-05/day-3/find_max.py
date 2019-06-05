def find_max(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        if arr[0] > arr[1]:
            arr[1] = arr[0]
            return find_max(arr[1:])
        else:
            return find_max(arr[1:])