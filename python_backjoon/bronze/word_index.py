word = input().lower()
c_dict = {chr(i) : 0 for i in range(97, 123)}
# print(c_dict)

for c in c_dict:
    try:
        c_dict[c] = word.index(c)
    except: # ValueError
        c_dict[c] = -1

for i in c_dict:
    print(c_dict[i])
