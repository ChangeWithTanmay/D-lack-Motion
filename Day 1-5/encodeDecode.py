import string
import random

chars = string.printable  
# printable = letters + digits + punctuation + space + newline etc.

print(chars)

shuffled = list(chars)
random.shuffle(shuffled)

encode = {ord(a): ord(b) for a, b in zip(chars, shuffled)}
decode = {ord(b): ord(a) for a, b in zip(chars, shuffled)}

txt = "My name is Stle 123!"

encoded = txt.translate(encode)
decoded = encoded.translate(decode)

print("Original:", txt)
print("Encoded :", encoded)
print("Decoded :", decoded)
