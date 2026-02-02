txt = "My name is Stle"

encode = {
    77: 43,   # M -> +
    121: 72,  # y -> H
    32: 42    # space -> *
}

decode = {
    43: 77,   # + -> M
    72: 121,  # H -> y
    42: 32    # * -> space
}

encodeTxt = txt.translate(encode)
decodeTxt = encodeTxt.translate(decode)

print(encodeTxt)
print(decodeTxt)

char=" "

# print(ord(char))