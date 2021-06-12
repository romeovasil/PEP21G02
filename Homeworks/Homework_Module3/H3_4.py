# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    pass
    # <your code here>
    mySplit=text.split(sep=' ',maxsplit=1)
    a=mySplit[0].upper()
    b=mySplit[1]
    for i in range(len(b)):
        if b[i]<"a" or b[i]>"z":
            b=b.replace(b[i],"_")

    myTuple=(a,b)
    return myTuple




print(process_text('1234567a Text to te5t'))