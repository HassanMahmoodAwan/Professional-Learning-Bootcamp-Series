""" Decorators: Every function pass through your Decorator custom Function. You can control the behaviour of your Function through Decorators.  """

# **************** Simple Decorator *****************
def simple(func):
    def wrapper():
        print(f"Function name: {func.__name__}")
        result = func()
        return result
    
    return wrapper  

@simple
def hello_function():
    print("Hello world!")
# ===================================================
    
    
# *************** Function Execution Time Calculator Decorator ******************
import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        print(f"Function Name: {func.__name__}", end="\n\n")
        
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"Execution Time: {endTime - startTime}")
        return result
    
    return wrapper

@time_calculator
def db_fetch_data(n):
    time.sleep(n)
    return "Data Fetch from DB."
# ===============================================================================

    

# ******************************* Debug Function *********************************
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        
        print(f"{func.__name__} has Args: {args_value} and keyword Args: {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    
    return wrapper

@debug
def greetings(name, greeting="Hello!"):
    print(f"{greeting} {name}.")
#  ===============================================================================


# **************************** Cache Handling *************************************
def cache(func):
    cacheStorage = {}
    def wrapper(*args):
        if args in cacheStorage:
            print(f"Cached Result: {cacheStorage[args]}", )
            return cacheStorage[args]
        
        result = func(*args)
        cacheStorage[args] = result
        
        print(result)
        return result
    
    return wrapper

@cache
def db_call(id, username):
    time.sleep(4)
    return f"user found in DB: {id}, {username}"
# =================================================================================


if __name__ == '__main__':    
    # hello_function()
    # db_fetch_data(4)
    # greetings("Hassan", greeting="Hello ")
    db_call("114", "Hassan Mahmood")
    db_call("114", "Hassan Mahmood")
    db_call("115", "Abdullah Rehan")
