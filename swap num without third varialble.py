#program to swap two numbersn without using the third variable.
def swap_numbers(a,b):

    a , b = b , a
    print("a =",a,"b =",b)

a = 55
b = 66
swap_numbers(a,b)