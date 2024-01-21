word = list(str(input()))

rotatable = True

letters = "IOSHZXN"

for i in word:
    if i not in letters:
        rotatable = False
        break

if rotatable:
    print("YES")
else:
    print("NO")
