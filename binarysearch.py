def binary_search(lists, item):
    first = 0
    last = len(lists) - 1
    found = False

    while first <= last and not found:
        mid = (first + last)//2
        if lists[mid] == item:
            found = True
        else:
            if item < lists[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


lists = [i for i in range(10,50,3)]
print(binary_search(lists, 40))
# binary_search(lists, 30)
