# For-Loop, While Loop, Do-While Loop (custom)


def forLoops():
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


def whileLoops():
    flag = False
    while (flag):
        counter = 1
    else:
        print("Infinite Loop")

    counter = 0
    while (counter < 5):
        flag = False
        counter += 1
    else:
        print("Runs 5 Times")


def doWhileLoops():
    counter = 10
    while (True):
        flag = False
        # do Work, then Check Condition
        if counter <= 10:
            break
    else:
        print("if loop break, else will not Run")


if __name__ == "__main__":
    forLoops()
    whileLoops()
    doWhileLoops()
