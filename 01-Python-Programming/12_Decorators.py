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
    
    


    


if __name__ == '__main__':    
    hello_function()