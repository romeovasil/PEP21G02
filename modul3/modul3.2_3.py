nr = 0;

my_gen=(i for i in range(0,99,3))

for i in my_gen:
    print(i)
    next(my_gen)
    next(my_gen)


