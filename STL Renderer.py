import matplotlib.pyplot as plt

import plotly.express as plex
import plotly
import time
import struct
import math

startTime = time.time()

x = []
y = []
z = []

def formatTime(time: float):

    hours = math.floor(time / 3600)
    minutes = math.floor((time % 3600) / 60)
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

trianglesDone = 0

fileLocation = input("File Path: ")

with open(fileLocation, "rb") as file:
    file.seek(80, 1)
    triangles = int.from_bytes(file.read(4), "little")

    print(str(triangles) + " triangles in model")

    #print(file.read(50))

    while trianglesDone < triangles:

        file.seek(12, 1) #skip the normal vector

        for i in range(3):
            x.append(struct.unpack('<f', file.read(4))[0])
            y.append(struct.unpack('<f', file.read(4))[0])
            z.append(struct.unpack('<f', file.read(4))[0])

        file.seek(2, 1)

        #print(str(x) + ", " + str(y) + ", " + str(z))

        trianglesDone += 1

        if (trianglesDone % int(triangles / 1000) == 0):
        
            timeTaken = time.time() - startTime

            percentDone = (trianglesDone / triangles)

            estimatedTimeRemaining = ((timeTaken / trianglesDone) * triangles) - timeTaken

            print(str(format(percentDone, ".1%")) + " done. Plotted " + str(trianglesDone) + "/" + str(triangles)+ " triangles. "
            "Estimated time remaining: " + formatTime(estimatedTimeRemaining) + ".")

#fig = plex.scatter_3d(x, y, z,)
#fig.show()


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, 'green')
plt.show()