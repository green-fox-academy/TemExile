a = [2, 3, 1, 5]
b = [0, 5, 3, 2, 2]
c = [-2, -5, -45]
d = [-23, 0, 6, -4, 34]

# bubble sort
def bubble_sort(str):
    for i in range(len(str) - 1):
        for j in range(len(str) - 1 - i):
            if str[j] > str[j + 1]:
                str[j], str[j + 1] = str[j + 1], str[j]
    return str
print(bubble_sort(a))
print(bubble_sort(b))
print(bubble_sort(c))
print(bubble_sort(d))

# insertion sort
def insertion_sort(str):
    for i in range(len(str) - 1):
        while i <len(str) and str[i] > str[i + 1]:
            str[i], str[i + 1] = str[i + 1], str[i]
            i += 1
    return str
print(insertion_sort(a))
print(insertion_sort(b))
print(insertion_sort(c))
print(insertion_sort(d))

# quick sort
def quick_sort(str):
    if len(str) <= 1:
        return str
    else:
        ref = str[0]
        greater = [i for i in str[1:] if i >= ref]
        smaller = [i for i in str[1:] if i < ref]
        return quick_sort(smaller) + [ref] + quick_sort(greater)
print(quick_sort(a))
print(quick_sort(b))
print(quick_sort(c))
print(quick_sort(d))

# merge sort
def merge_sort(str):
    if len(str) > 1:
        stop = len(str) // 2
        left = str[:stop]
        right = str[stop:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                str[k] = left[i]
                i += 1
            else:
                str[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            str[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            str[k] = right[j]
            j += 1
            k += 1
    return str
print(merge_sort(a))
print(merge_sort(b))
print(merge_sort(c))
print(merge_sort(d))

# heapsort
## build heap
def b_heap(str, cur_root, t_size):
    large = cur_root
    left = cur_root * 2 + 1
    right = cur_root * 2 + 2
    if left < t_size and str[left] > str[large]:
        large = left
    if right < t_size and str[right] > str[large]:
        large = right
    if large != cur_root:
        str[large], str[cur_root] = str[cur_root], str[large]
        b_heap(str, large, t_size)
## define the sort function
def heap_sort(str):
    size = len(str)
    for i in range(size // 2 - 1, -1, -1):
        b_heap(str, i, size)
    for i in range(size - 1, 0, -1):
        str[0], str[i] = str[i], str[0]
        b_heap(str, 0, i)
    return str
print(heap_sort(a))
print(heap_sort(b))
print(heap_sort(c))
print(heap_sort(d))
