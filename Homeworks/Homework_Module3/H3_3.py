# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n: int):
    pass
    # <your code here>
    if(n==1):
        return 1
    else:
        return (n**2)*factorial_of_squares(n-1)


print(factorial_of_squares(5))