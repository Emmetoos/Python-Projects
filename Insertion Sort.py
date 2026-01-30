import random

inputLength = int(input("How many elements should be in the list: "))

i=0
inputList = []

while (i < inputLength):
    inputList.append(random.randrange(0, inputLength))
    i += 1

print(inputList)

maxInput = (0,0)
for i in range(len(inputList)):
    if inputList[i] > maxInput[1]:
        maxInput = (i, inputList[i])

outputList = [maxInput[1]]
inputList.pop(maxInput[0])

for i in inputList:
    for j in range(len(outputList)):
        if i < outputList[j]:
            outputList.insert(j, i)
            break

print(outputList)