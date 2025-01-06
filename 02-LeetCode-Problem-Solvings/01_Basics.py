#  2109. Adding Spaces to a String  (string, loop)
def addSpaces() -> str:
    s: str = "LeetcodeHelpsMeLearn"
    spaces1: list[int] = [8,13,15]
    
    # Method 01
    spacesTracker = 0
    output = ""
    for index in range(len(s)):
    
        if spacesTracker < len(spaces) and index == spaces[spacesTracker]:
            output += " "
     
            if spacesTracker < len(spaces):
                spacesTracker += 1

        output += s[index]
    return output



# 3110:  Score of a String (sliding-window, loop, string)
def scoreOfString(s: str) -> int:
    if len(s) == 0:
        return 0
    
    if len(s) == 1:
        return ord[s[1]]
    
    prev = 0
    nexts = 1
    sums = 0
    while nexts < len(s):
        
        sums += abs(ord(s[prev]) - ord(s[nexts]))
        prev += 1
        nexts += 1
    return sums
