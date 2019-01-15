#this is Example for ------------>complex

""" Definition : --> complex is one of the class and it is treated as fundamental data type.

                 --> The purpose of this data type is to store complex numbers data
                     which is in the format of a+bj (or) a-bj

                 --> here a is called - Real part and
                          b is called - imaginary part
                          j is represented as - square root of -1

                 --> To seperate complex number data we use predefined datamember called 1. real
                                                                                         2. imag
                     which are present in complex class.
"""

###### Examples :

a=10+20j
b=4+2j

print("\n a , b  =",a,b)

print("\n Type of a ---->    ",type(a))

print("\n a+b    =",a+b)

print("\n a-b    =",a-b)

c=a*b
print("\n a*b    =",c)

print("\n Type of c ---->      ",type(c))


### a.real
### a.imag

print("\n real part of a is ---->    ",a.real)

print("\n imaginary part of b is ---->    ",b.imag)






