# List [ Mutable,   Ordered,   Duplicate,    All DataTypes,    List-wise OP, Passed by Reference ]
# what if I  /10, or + 30 or - 40 or * 3

import copy
def lists():
    array:list[int | str | ...] = [10, 12.2, "Hassan", True, None, "check"]  
    tupleToList = list((10, 12, 14))
    
    len(array)
    array[::]
    array[-1]
    array[2:3]
    
    
    array[2:3] = tupleToList            # Works
    # array[-1] = [10, 12]              # Nested
    array[-1::] = ["Now", "it", "works"]         
    
    array.append("last")
    array.insert(50, "exceeded Index so at Last")
    array.pop()
    array.pop(0)
    array.extend(["new Array", "extend at last"])
    try:
        array.remove("not in list")
    except ValueError:
        print("Not in List")


    # del array
    # del array[2]
    # array.clear()
    
    array[::-1]
    print(array.reverse())
    print(list(reversed(array)))
    

    arrayStr = ''.join(array)
    zerosArray = [0] * len(array)
    # array.sort()
    array.index(None)                      # Check either if not Exist should it give -1.
    array.count(10)
    
    shallowCopyList = array
    shallowCopyArray = array.copy()
    deepCopyList = copy.deepcopy(array)

    evenListComprehension = [value for value in range(40) if value % 2 == 0]

    print(evenListComprehension)
    

if __name__ == "__main__":
    lists()