f = open("extratest/testinputText.txt", "r")
for line in f:
    if '\t' in line:
        print("YES")

    if line[0] == " ":
        print("SPACE")
    print(line)

i=10
while i < 20:
    i += 1
    gundam = 10
    print(i)