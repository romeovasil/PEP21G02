def add_numbers():
    output=[]
    num=int(input("Enter a number: "))
    sum=num
    output.append(num)
    while(sum<100):
        num = int(input("Enter a number: "))
        sum += num
        output.append(num)
    print(output)
add_numbers()

