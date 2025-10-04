brickCount = 94
bricksInState = [brickCount]
brickStates = [4, 10, 19]

def solutionA():
    heights = []
    while bricksInState[len(bricksInState) - 1] < brickCount:


        currentHeight = 0

        newHeight = True

        for height in heights:
            if currentHeight == height:
                newHeight = False
                break
        
        if newHeight:
            heights.append(currentHeight)

        print(str(len(heights)) + ", " + str(currentHeight))

    print(len(heights))
    print(heights)

def solutionB():
    heights = set()

    for state0Bricks in range(brickCount + 1):
        otherBricks = brickCount - state0Bricks
        for state1Bricks in range(otherBricks + 1):
            state2Bricks = otherBricks - state1Bricks
            height = (state0Bricks * brickStates[0]) + (state1Bricks * brickStates[1]) + (state2Bricks * brickStates[2])
            heights.add(height)

    heightsList = []
    for height in heights:
        heightsList.append(height)

    heightsList.sort()

    print(f"B AMOUNT {len(heightsList)}")
    print(f"B AMOUNT {heightsList}")

    

solutionA()
solutionB()
