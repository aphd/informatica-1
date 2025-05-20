## Exercise 1

Given the binary number \((-1101.1101)_2\), calculate its floating-point representation, and then determine the values of \(S\), \(M\), and the exponent \(esp\), following the convention \(1.M\). Consider 1 bit for the sign \(S\), 5 bits for the exponent \(esp\) (with a bias of 15), and 10 bits for the mantissa \(M\). Indicate the sequence of bits for \(S\), \(esp\), and \(M\) separated by a comma (0.0000000000).

### Solution

1. **Sign Bit (S)**: 1 (since the number is negative)
2. **Normalized Form**: \(-1.1011101 \times 2^3\)
3. **Exponent Calculation**: 
   - Actual exponent: 3
   - Biased exponent: \(3 + 15 = 18\)
   - Binary representation of 18: \(10010\)
4. **Mantissa (M)**: 
   - From the normalized form: \(1011101000\) (10 bits)

**Final Answer**:  
`1,10010,1011101000`


## Exercise 2

Given the decimal number \(16\) and its corresponding binary number in 8 bits \( (16)_{10} = 0001\ 0000_2 \), determine the negative corresponding number using 1's complement and 2's complement representation. Write the values of both representations separated by a comma (for example, 00000000, 00000000).

### Solution

1. **Binary Representation of \(16\)**: 
   - \(0001\ 0000\)

2. **1's Complement**: 
   - Invert all bits: \(1110\ 1111\)

3. **2's Complement**: 
   - Add 1 to the 1's complement: 
     - \(1110\ 1111 + 1 = 1111\ 0000\)

**Final Answer**:  
`11101111,11110000`