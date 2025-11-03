from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import time

startTime = time.time()

def formatTime(time: float):

    hours = round(time / 3600)
    minutes = round((time % 3600) / 60)
    seconds = round((time % 3600) % 60, 1)

    if hours == 1:
        hours = str(hours) + " hour"
    else:
        hours = str(hours) + " hours"

    if minutes == 1:
        minutes = str(minutes) + " minute"
    else:
        minutes = str(minutes) + " minutes"

    if seconds == 1:
        seconds = str(seconds) + " second"
    else:
        seconds = str(seconds) + " seconds"
    
    return(hours + ", " + minutes + ", and " + seconds)


fig = plt.figure()
ax = plt.axes(projection = '3d')

trianglesDone = 0

fileLocation = input("File Path: ")
numBytes = 84
with open(fileLocation, "rb") as file:
    file.seek(81)
    triangles = int.from_bytes(file.read(4), "little")

    while trianglesDone < triangles:
        file.seek(12, 1)
        x = float(file.read(12))
        y = float(file.read(12))
        z = float(file.read(12))
        file.seek(2, 1)

        #print(str(x) + ", " + str(y) + ", " + str(z))

        ax.scatter(x, y ,z)

        trianglesDone += 1

        if (trianglesDone % (triangles / 1000) == 0):
        
            timeTaken = time.time() - startTime

            percentDone = (trianglesDone / triangles)

            estimatedTimeRemaining = ((timeTaken / trianglesDone) * triangles) - timeTaken

            print(str(format(percentDone, ".1%")) + " done. Plotted " + str(trianglesDone) + "/" + str(triangles)+ " triangles. "
            "Estimated time remaining: " + formatTime(estimatedTimeRemaining) + ".")

plt.show()