class Shape():
    pass
 
def sameORnot(obj1,obj2):
    return obj1 is obj2
    
sq1 = Shape()
sq2 = sq1
print(sameORnot(sq1,sq2))
