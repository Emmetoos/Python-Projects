fileLocation = input("File Path: ")

with open(fileLocation, "rb") as file:
    #Header Chunk
    MThd = file.read(4)
    header_length = int.from_bytes(file.read(4), "big")
    format = int.from_bytes(file.read(2), "big")
    n_tracks = int.from_bytes(file.read(2), "big")
    bpm = int.from_bytes(file.read(2), "big")

    print(str(MThd) + ", " + str(header_length) + ", " + str(format) + ", " + str(n_tracks) + ", " + str(bpm))