# 20P
# 1) Prove that "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)

print(False or False and True or True)

print(False or(False and True) or True)
print((False or False)and(True or True))

#rezultatele ultimelor 2 printuri difera, iar al 2-lea print este cel echivalent cu primul,de unde rezulta
#ca "and" operation precede "or" operation