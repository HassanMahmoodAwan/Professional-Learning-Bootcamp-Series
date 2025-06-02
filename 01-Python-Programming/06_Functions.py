# Global Variable
value = 10

def lower_case_default(param01, param02 = 20) -> tuple:
    global value
    value = 20
    return param01, param02          # Tuple Return


def all_main_concepts():
    
    def name_params(p01, p02):
        print(f"p01 = {p01} and p02 = {p02}")
    name_params(p02=30, p01=5)
    
    def kargs(*params):              # Tuple in Arguments.
        print(params)
    kargs(10, 12, 23, 4324)
    
    def key_value_args(**keyValueParams):
        print(keyValueParams)
    key_value_args(first="Hassan", mid="Mahmood", last="Awan")
        


def anonymous_function():
    result = lambda x, y = 20 : x + y
    print(result(10))
    
    print((lambda : print("Hello world!"))())



def clousure_scope():
    
    def adder(num):
        def inner(x):
            return x**num
        return inner           # return Function defination, closure sends all referred varaible with func defination.
    
    result = adder(2)
    print(result(2))    
    


if __name__ == "__main__":
    # print(value)
    # lower_case_default(10, 30)
    # print(value)
    # all_main_concepts()
    # anonymous_function()
    clousure_scope()