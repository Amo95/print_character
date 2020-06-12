# Search algorithm

def search(num_list, num):
    for i in num_list:
        if i == num:
            return True
        else:
            return False

lists = range(1, 101)
print(search(lists, 101))

