import time


timer = int(input("Enter the time in seconds: "))

for i in range(timer, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i // 3600)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    # end="\r" is used to overwrite the previous line in the console
    time.sleep(1)