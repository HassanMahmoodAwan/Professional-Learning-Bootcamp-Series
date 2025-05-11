# Tuple (Immutable,  ordered,   All-DataTypes,  NotChangeable,  Faster compare to List,  Passed by Reference, Tuple-wise Op )

def tuples():
    myTuple:tuple = (10, 12, 13, "Hassan", True)
    secTuple:tuple = 1,2,3,4
    singleElementTuple: tuple = ("one",)
    
    a,b,c = myTuple               # Error:  same varaibles == unpack values.
    print(a, end="\n")
    print(c)
    print(secTuple * 3)
    
    # myTuple.append(10)             # Not working
    # myTuple[2] = 123              #  Not WOrking
    
    myTuple.index(13)
    myTuple.count(20)
    max(secTuple)                   # max, min also works on LIST, STRINGS, TUPLES.
    min(secTuple)
    
    


if __name__ == "__main__":
    tuples()
    