# implementing a AND gate in python 

def AND(A:int , B:int) ->int:
    """
    Performs logical AND operation on two binary inputs.

    Returns 1 only if both inputs are 1; otherwise, returns 0.

    Parameters
    ----------
    A : int
        First binary input (0 or 1).
    B : int
        Second binary input (0 or 1).

    Returns
    -------
    int
        Result of A AND B.

    Example
    -------
    >>> AND(1, 1)
    1
    >>> AND(1, 0)
    0
    """
    
    if(A == 1 and B==1):
        return 1
    else:
        return 0

def ANDthreeIN(A:int,B:int,C:int) ->int:
    """
    Performs logical AND operation on three binary inputs.

    Returns 1 only if all three inputs are 1; otherwise, returns 0.

    Parameters
    ----------
    A : int
        First binary input (0 or 1).
    B : int
        Second binary input (0 or 1).
    C : int
        Third binary input (0 or 1).

    Returns
    -------
    int
        Result of A AND B AND C.

    Example
    -------
    >>> ANDthreeIN(1, 1, 1)
    1
    >>> ANDthreeIN(1, 0, 1)
    0
    """
    
    if(A==1 and B==1 and C == 1):
        return 1
    else:
        return 0

def OR(A:int, B:int)->int:

    
    if(A == 0 and B == 0):
        return 0
    else:
        return 1 
        
def NOT(A:int)-> int:
    """
    Performs a logical NOT operation on a binary input.

    The NOT gate inverts the input: returns 1 if input is 0, and 0 if input is 1.

    Args:
        A (int): Binary input (0 or 1).

    Returns:
        int: Inverted value of A.

    Example:
        >>> NOT(0)
        1
        >>> NOT(1)
        0
    """
    
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
    """
    Computes the sum and carry outputs of a Half Adder circuit using logic gates.

    A Half Adder takes two binary inputs and produces a sum and carry output,
    which are the result of XOR and AND operations respectively.

    Parameters
    ----------
    A : int
        First binary input (0 or 1).
    B : int
        Second binary input (0 or 1).

    Returns
    -------
    list
        A list containing two integers:
        - sum (int): Result of A XOR B.
        - carry (int): Result of A AND B.

    Example
    -------
    >>> HalfAdder(1, 0)
    [1, 0]


    """
    
    sum = XOR(A,B)
    carry = AND(A,B)
    return [sum, carry]
    
def FullAdder(A:int,B:int ,Cin:int)->list:
    
    """
    Computes the sum and carry outputs of a Full Adder circuit.

    A Full Adder adds three binary inputs: A, B, and Carry-in (Cin).
    It uses two Half Adders internally and an OR gate to produce the final sum and carry.

    Parameters
    ----------
    A : int
        First binary input (0 or 1).
    B : int
        Second binary input (0 or 1).
    Cin : int
        Carry-in input (0 or 1).

    Returns
    -------
    list
        A list containing:
        - sum (int): Result of the addition (A ⊕ B ⊕ Cin).
        - carry (int): Final carry output (1 if any two or more inputs are 1).

    Example
    -------
    >>> FullAdder(1, 1, 0)
    [0, 1]

    """
    
    hs = HalfAdder(A,B)
    fs = HalfAdder(hs[0], Cin)
    carry = OR(fs[1], hs[1])
    return[fs[0],carry]

def ArrayAdder4bit(A0:int,A1:int,A2:int,A3:int, B0:int,B1:int,B2:int,B3:int, Cin:int)->list:
    
    """
    Computes the 4-bit binary sum of two 4-bit inputs using chained Full Adders.

    This function performs binary addition of two 4-bit numbers represented as individual bits,
    along with an initial carry-in. The addition is performed bitwise from LSB to MSB,
    propagating the carry through each stage.

    Parameters
    ----------
    A0, A1, A2, A3 : int
        Bits of the first 4-bit binary number (A0 is LSB, A3 is MSB).
    B0, B1, B2, B3 : int
        Bits of the second 4-bit binary number (B0 is LSB, B3 is MSB).
    Cin : int
        Initial carry-in (usually 0).

    Returns
    -------
    list
        A list containing:
        - Sum bits [S0, S1, S2, S3] (int): The resulting 4-bit sum from LSB to MSB.
        - Carry-out (int): The final carry after the MSB addition.

    Example
    -------
    >>> ArrayAdder4bit(1, 0, 1, 1, 1, 1, 0, 1, 0)
    [0, 0, 0, 1, 1]"""

    sl0 = FullAdder(A0,B0,Cin)
    sl1 = FullAdder(A1,B1,sl0[1])
    sl2 = FullAdder(A2,B2,sl1[1])
    sl3 = FullAdder(A3,B3,sl2[1])
    return[sl0[0],sl1[0],sl2[0],sl3[0],sl3[1]]


def Mux4x1(A:int,B:int,C:int,D:int,S0:int,S1:int)->int:
    
    """
    Simulates a 4x1 multiplexer using basic logic gates.

    The multiplexer selects one of the four input values (A, B, C, D) based on the values 
    of the two select lines (S0, S1), and returns the selected input.

    Selection Mapping:
        S1 S0 | Output
        ------|--------
        0  0 | A
        0  1 | B
        1  0 | C
        1  1 | D

    Args:
        A (int): First input (selected when S1=0 and S0=0).
        B (int): Second input (selected when S1=0 and S0=1).
        C (int): Third input (selected when S1=1 and S0=0).
        D (int): Fourth input (selected when S1=1 and S0=1).
        S0 (int): Select lines.
        S1 (int): select lines.
    """
    
    compS0 = NOT(S0)
    compS1 = NOT(S1)
    
    
    AO = AND(AND(compS0,compS1),A)
    BO = AND(AND(compS0,S1),B)
    CO = AND(AND(S0,compS1),C)
    DO = AND(AND(S0,S1),D)

    x = OR(AO,BO)
    y = OR(CO,DO)

    mux = OR(x,y)

    return mux



    

    
    
    
    
