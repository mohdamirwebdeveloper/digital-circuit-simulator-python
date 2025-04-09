import simulator

while True:
    # A = int(input("Enter the first Binary bit : "))
    # B = int(input("Enter the Second Binary bit : "))
    # C = int(input("Enter the Third Binary bit : "))
    # D = int(input("Enter the Third Binary bit : "))
    
    # A1 = int(input("Enter the first Binary bit : "))
    # B1 = int(input("Enter the Second Binary bit : "))
    # C1 = int(input("Enter the Third Binary bit : "))
    # D1 = int(input("Enter the Third Binary bit : "))
    
    x = simulator.Mux4x1(1,1,0,1,0,0)
    print(x)

        #examples
        #examples
    A = int(input("Enter the first bit : "))
    B = int(input("Enter the second bit : "))
    
    print("AND operation : ",simulator.AND(A,B))
    print("OR operation : ",simulator.OR(A,B))
    print("NOT operation : ",simulator.NOT(A))
    print("NAND operation : ",simulator.NAND(A,B))
    print("NOR operation : ",simulator.NOR(A,B))
    print("XOR operation : ",simulator.XOR(A,B))
    print("XNOR operation : ",simulator.XNOR(A,B))
    
    #Implementing Full adder using MUX
    A = int(input("Enter the first Bit A : "))
    B = int(input("Enter the Second Bit B : "))
    Cin = int(input("Enter the Third Bit Cin (Carry IN) : "))
    
    Acomp = simulator.NOT(A)

    sum = simulator.Mux4x1(A,Acomp,Acomp,A,B,Cin)
    carry = simulator.Mux4x1(0,A,A,1,B,Cin)
    print(sum,carry)

        # full subtractor using MUX 

    print("<-----------------------Full subtracter------------------------------>")

    A = int(input("Enter the first Bit A : "))
    B = int(input("Enter the Second Bit B : "))
    Bin = int(input("Enter the Third Bit Cin (Carry IN) : "))
    Acomp = simulator.NOT(A)
    diff = simulator.Mux4x1(A,Acomp,Acomp,A,B,Bin)
    borrow = simulator.Mux4x1(0,Acomp,Acomp,1,B,Bin)
    print(diff,borrow)
    
