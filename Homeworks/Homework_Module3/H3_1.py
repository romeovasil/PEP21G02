# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
    pass
    # <your code here>
    newlist=[]
    for i in range(len(list_of_objects)):
        if(list_of_objects[i] == True):
            newlist.append(1)
        elif(list_of_objects[i]==False):
            newlist.append(0)
        elif(type(list_of_objects[i])==str):
            newlist.append(int(list_of_objects[i]))
        elif(type(list_of_objects[i])==int):
            newlist.append(list_of_objects[i])
        else:
            newlist.append(len(list_of_objects[i]))
    return sorted(newlist,reverse=True)

print(ordered_ints([1, True, '123', False, 6, ()]))

