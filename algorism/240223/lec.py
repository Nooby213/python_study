def encoding(code):
    return code ^ 1004

def decoding(code):
    return code ^ 1004

result = encoding(7070)
print(result)
result2 = decoding(result)
print(result2)
t = 1
for i in range(5):
    print(bin(2**i))
    print(t, bin(t))
    print()
    t = t << 2

print(f'{0.1:.20f}')