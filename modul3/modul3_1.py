import math
def is_prime(number):
    if(number ==1 or number ==0):
        return False
    elif(number==2):
        return True
    elif(number%2==0):
        return False
    else:
        for i in range(3,int(math.sqrt(number)+1)):
            if(number%i==0):
                return False
    return True

def primes(limit):
    result=[]
    for i in range(1,limit):
        if(is_prime(i)==True):
            result.append(i)
    return result



print(primes(10))