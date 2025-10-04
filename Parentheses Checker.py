input = input("Input a String: ")
counter = 0
pairs = 0

for i in input:
    if (i == "("):
        counter += 1
    
    elif (i == ")"):
        counter -= 1

        if (counter < 0):
            break
        
        pairs += 1

if (counter != 0 or counter < 0):
    print("-1")
else:
    print(pairs)