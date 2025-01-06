# Exception: Program Syntactically Correct, Internal Event stop flow of Program.
# Advantages:      [ Readable,   Debugging,   CleanerCode,   Relibility]
# DisAdvantages:   [ Lengthy, Slow Performance]

def exceptionHandling():
    # ValueError
    # ZeroDivisionError
    # NameError
    # IndexError
    # TypeError
    
    try:
        a = 10
        b = "20"
        print(a + b)
    except TypeError:
        print("Type Error Faced.")
    except Exception as e:
        print(f"Error Occured:  {e}")
    else:
        print("When Try run Successfully")
    finally:
        print("Runs EveryTime.")
    
    
    try:
        a = 10
        b = 0
        c = a / b
    except ZeroDivisionError:
        print("Zero Division Error")
    except:
        print("Any Error Occur Look at it. Not run in this case.")


    try:
        raise NameError("Manually rasied Error")
    except NameError:
        print("Name Error Occured")
    except:
        print("Error")


    try:
        raise NameError("Manually rasied Error")
    except NameError:
        print("Name Error Occured")
        raise                          # Throw Error, Run to Check.
    except:
        print("Error")


if __name__ == "__main__":
    exceptionHandling()