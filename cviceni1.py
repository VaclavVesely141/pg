def add(a, b):
    c = a + b
    return c

def multiply(a, b, c):
    return a * b * c

def div(a,b): 
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def je_delitelne_beze_zbytku(a, b):
    if a% b == 0:
        return "je delitelne beze zbytku"
    else:
        return "neni delitelne beze zbytku"
    
def je_delitelne_tremi(a):
    return je_delitelne_beze_zbytku(a, 3)

if __name__ == "__main__":
    print(add(5, 7))
    print(multiply(1, 2, 3))
    print(div(10, 2))
    print(div(10, 0))   
    print(je_delitelne_beze_zbytku(10, 2))
    print(je_delitelne_beze_zbytku(10, 3))
    print(je_delitelne_tremi(10))
    print(je_delitelne_tremi(9))
