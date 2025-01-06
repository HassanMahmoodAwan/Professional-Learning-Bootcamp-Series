# Global Variable
value = 10

def camelCase_Default(param01, param02 = 20) -> tuple:
    global value
    value = 20
    return param01, param02          # Tuple Return


def allMainConcepts():
    
    def nameParams(p01, p02):
        print(f"p01 = {p01} and p02 = {p02}")
    nameParams(p02=30, p01=5)
    
    def kargs(*params):              # Tuple in Arguments.
        print(params)
    kargs(10, 12, 23, 4324)
    
    def keyValueArgs(**keyValueParams):
        print(keyValueParams)
    keyValueArgs(first="Hassan", mid="Mahmood", last="Awan")
        


def anonymousFunction():
    result = lambda x, y = 20 : x + y
    print(result(10))



if __name__ == "__main__":
    print(value)
    camelCase_Default(10, 30)
    print(value)
    allMainConcepts()
    anonymousFunction()
    