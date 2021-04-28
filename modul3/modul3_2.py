def enc_dec(text , key):
    output=""
    for i in text:
        output=output+chr(ord(i) ^ key)

    return output

print(enc_dec("Hello World!", 129))

