# implementing a AND gate in python 

def AND(A:int , B:int) ->int:
    if(A == 1 and B==1):
        return 1
    else:
        return 0

def OR(A:int, B:int)->int:
    if(A == 0 and B == 0):
        return 0
    else:
        return 1 
        
def NOT(A:int)-> int:
    if(A == 0):
        return 1
    else:
        return 0
    
def NAND(A:int , B:int)->int:
    result = AND(A,B)
    
    return NOT(result)

def NOR(A:int , B:int)->int:
    result = OR(A,B)
    
    return NOT(result)

def XOR(A:int , B:int)-> int:
    nab = NAND(A,B)
    nab1 = NAND(A, nab)
    nab2 = NAND(B, nab)
    xor = NAND(nab1, nab2)
    return xor

def HalfAdder(A:int ,B:int)->list:
    sum = XOR(A,B)
    carry = AND(A,B)
    return [sum, carry]
    
def FullAdder(A:int,B:int ,Cin:int)->list:
    hs = HalfAdder(A,B)
    fs = HalfAdder(hs[0], Cin)
    carry = OR(fs[1], hs[1])
    return[fs[0],carry]

def ArrayAdder4bit(A0:int,A1:int,A2:int,A3:int, B0:int,B1:int,B2:int,B3:int, Cin:int)->list:
    
    sl0 = FullAdder(A0,B0,Cin)
    sl1 = FullAdder(A1,B1,sl0[1])
    sl2 = FullAdder(A2,B2,sl1[1])
    sl3 = FullAdder(A3,B3,sl2[1])
    return[sl0[0],sl1[0],sl2[0],sl3[0],sl3[1]]
    
    
while True:
    A = int(input("Enter the first Binary bit : "))
    B = int(input("Enter the Second Binary bit : "))
    C = int(input("Enter the Third Binary bit : "))
    D = int(input("Enter the Third Binary bit : "))
    
    A1 = int(input("Enter the first Binary bit : "))
    B1 = int(input("Enter the Second Binary bit : "))
    C1 = int(input("Enter the Third Binary bit : "))
    D1 = int(input("Enter the Third Binary bit : "))
    
    print(ArrayAdder4bit(A,B,C,D,A1,B1,C1,D1,0))
    

    
    
    
    
