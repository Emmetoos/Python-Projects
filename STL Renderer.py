from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection = '3d')

fileLocation = input("File Path: ")
numBytes = 84
with open(fileLocation, "rb") as file:
    file.seek(81)
    trianglesLeft = int.from_bytes(file.read(4), "little")

    while trianglesLeft > 0:
        file.seek(1, 1)
        x = int.from_bytes(file.read(1), "big")
        y = int.from_bytes(file.read(1), "big")
        z = int.from_bytes(file.read(1), "big")
        file.seek(1, 1)

        #print(str(x) + ", " + str(y) + ", " + str(z))

        ax.scatter(x, y ,z)

        trianglesLeft -= 1

plt.show()