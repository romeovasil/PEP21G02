# 25P - (use recursion)
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    pass
    # <your code here>
    if n<=0:
        return 0
    else:
        return ((1**2)*n)**2+sum_of_square(n-1)


print(sum_of_square(4))