a = [2,3,1,5]
b = [0, 5, 3, 2, 2]
c = [-2, -5, -45]
d = [-23,0,6,-4,34]

# bubble sort
def bubble_sort(str):
    for i in range(len(str)-1):
        for j in range(len(str)-1-i):
            if str[j] > str[j+1]:
                str[j], str[j+1] = str[j+1], str[j]
    return str
print(bubble_sort(a))
print(bubble_sort(b))
print(bubble_sort(c))
print(bubble_sort(d))

# insertion sort
def insertion_sort(str):
    for i in range(len(str)-1):
        while i <len(str) and str[i] > str[i+1]:
            str[i], str[i+1] = str[i+1], str[i]
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
    
