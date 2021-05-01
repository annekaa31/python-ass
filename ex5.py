# ex5

t = "The quick brown fox jumps over the lazy dog"

s = 3
result = ''
diff = 0
pre_final = 0


for i in t:

    if (ord(i) + s) > 122:
        diff = (ord(i) + s) - 122
        pre_final = 96 + diff
        final = chr(pre_final)
        result = result + final

    elif 97 <= ord(i) <= 122:
        let = chr(ord(i) + s)
        result = result + let
    else:
        result += i


print("Encrypted text: " + result + "\n")
print("Shift: " + str(s) + "\n")
print("Decrypted text: " + t)
