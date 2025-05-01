# Strings are Immutable but Assignable.

def strings():
    channel: str = "Chai \"aur Code!"
    len(channel)
    channel[1:10:1]     # Slicing: [start:stop:step]
    channel[::]
    channel[:-1]
    channel[-1]
    channel[::2]
    channel[1:20:3]
    print(f"Reverse is {channel[::-1]}")
    print(''.join(list(reversed(channel))))

    multiLineStr = """   Hello, World!      
                    Welcome to Python  " """
    print(multiLineStr.strip())

    channel.count('c')
    channel.index("aur")
    channel.find("aur")      # Returns -1 if not found.
    channel.rfind("aur")
    channel.isdigit()        # True if all chars digits.
    channel.isalpha()        # True if all chars alphabets.       

    try:
        channel[2] = "check"
    except Exception as e:
        print(e)

    channel += "check"
    channel.replace(" ", "-")  # Not inplace

    print(channel.capitalize() + "\n" + channel.title() + "\n" + channel.upper() + "\n" + str(channel.strip().split()))


if __name__ == "__main__":
    strings()
