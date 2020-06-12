def duplicate(lists):
    names = set()

    for i in lists:
        len1 = len(names)
        names.add(i)
        len2 = len(names)
        
        if len1 == len2:
            return i
            
        

def buy(sent):
    return "".join([i for i in sent if i.isdigit()])


def lottery(l1, l2):
    return [i for i in l1 if i in l2]

    l1 = [2,43,48,62,64,28,3]
    l2 = [1,28,42,70,2,10,62,31,4,14]

    l1 = set(l1)
    l2 = set(l2)
    print(list(l2.intersection(l1)))

# Given a non-empty list of integers,
# every element appears twice except for one. Find that single one.

lists = [1,1,2,2,3,3,4,5,5]

def out(l):
    for i in l:

        if l.count(i) == 1:
            return i

print(out(lists))
