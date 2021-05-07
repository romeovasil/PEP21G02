data = """
_____
Section1
_____
value1
value2
_____
Section2
_____
value1
value2
_____
Section3
_____
value1
value2
"""



def parse_data(data:str):
    my_section = False
    linii = data.splitlines()
    result = []
    print(linii)
    for line in linii:
        if line=="":
            continue
        if "_____" == line and my_section is False:
            my_section = True
            print("New section")
        elif "_____" == line and my_section is True:
            my_section = False
            print("End new section")
        elif my_section:
            print("Section name is", line)
            result.append([line])
        elif not my_section:
            result[-1].append(line)

        print(line)
    return result
var = parse_data(data)
print(var)