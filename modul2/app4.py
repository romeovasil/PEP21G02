txt= input("insert text: ")
i=0
for letter in txt:
    for voc in "aeiou":
        if letter==voc:
            letter=letter.upper()
            i=1
    if i==0:
            for voc in "AEIOU":
                if letter == voc:
                    letter=letter.lower()
    i=0
    print(letter,end="")
