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
    #Implementing Full adder using MUX
    A = int(input("Enter the first Bit A : "))
    B = int(input("Enter the Second Bit B : "))
    Cin = int(input("Enter the Third Bit Cin (Carry IN) : "))
    
    Acomp = simulator.NOT(A)

    sum = simulator.Mux4x1(A,Acomp,Acomp,A,B,Cin)
    carry = simulator.Mux4x1(0,A,A,1,B,Cin)
    print(sum,carry)
    
