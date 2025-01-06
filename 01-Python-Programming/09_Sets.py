# Sets { Unordered,   No Indexing,   Unique,   All-DataTypes Allowed, Mutable }
# FrozenSets ==> Immutable

def sets():
    mySet:set = {1,3,4,3,"Hassan", True}
    emptySet:set = set()                     # {} is for Dict(), not for Set
    
    mySet.add(10)
    mySet.pop()                               # From Front
    mySet.remove(3)
    mySet.discard(True)                       # if NOT exist, no Error
    print(mySet)
    
    
    # mySet.clear()
    shallowSet = mySet.copy()
    
    # FrozenSet
    frozenSet = frozenset([1,2,3,4,5,5])
    print(frozenSet)
    


if __name__ == "__main__":
    sets()