# Strings are Immutable but Assignable.

def strings():
    channel: str = "Chai \"aur Code!"
    len(channel)
    channel[1:10]
    channel[::]
    channel[:-1]
    print(f"Reverse is {channel[::-1]}")
    print(''.join(list(reversed(channel))))

    multiLineStr = """   Hello, World!      
                    Welcome to Python  " """
    print(multiLineStr.strip())

    print(channel.count('c'))
    print(channel.index("aur"))

    try:
        channel[2] = "check"
    except Exception as e:
        print(e)

    channel += "check"
    channel.replace(" ", "-")  # Not inplace

    print(channel.capitalize() + "\n" + channel.title() + "\n" + channel.upper() + "\n" + str(channel.strip().split()))


if __name__ == "__main__":
    strings()
