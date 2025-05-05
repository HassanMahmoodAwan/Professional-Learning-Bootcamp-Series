# For-Loop, While Loop, Do-While Loop (custom)

# Finite Number of Iterations
def for_loops():
    for i in range(0, 10, 2):
        a = 10

    for c in "hello, world!":
        char = c

    for value in [10, 12, 14]:
        val = value

    for index, value in enumerate([[10, 12, 14]]):                    
        print(index, ": ", value)

    for one, two in zip([10, 12, 14], [15, 23, 234, 2343]):
        print("Zip gives combination, provide matching, ignore others")


# Can be infinite, but should not be.
def while_loops():
    flag = False
    while (flag):
        counter = 1
    else:
        print("Infinite Loop if True, otherwise only else part will execute.")

    counter = 0
    while (counter < 5):
        flag = False
        counter += 1
    else:
        print("Runs 5 Times")

# Do Work, then Check Condition
def do_while_loops():
    counter = 10
    while (True):
        flag = False
        
        if counter <= 10:
            break
    else:
        print("if loop break, else will not Run, This code is unreachable.")


if __name__ == "__main__":
    forLoops()
    whileLoops()
    doWhileLoops()
