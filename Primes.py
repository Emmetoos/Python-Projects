
#import libraries
import time
import random

#variables
targetLength = int(input("How many primes? "))
primes = []
input = 2
numPrimes = 0

interval = random.randint(9000, 11000)

startTime = time.time()
timeTaken = 0

#fucntions
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

#main loop
while numPrimes < targetLength:

    isPrime = True
    
    for prime in primes:
        
        if (prime ** 2 >= input):
            break

        if (input % prime == 0):
    
            isPrime = False
            break
    
    if (isPrime == True):
        
        numPrimes += 1
        primes.append(input)
    
    if (numPrimes % interval == 0) & (numPrimes != targetLength) & (primes[numPrimes - 1] == input):
        
        timeTaken = time.time() - startTime

        interval = random.randint(9000, 11000)

        percentDone = round((numPrimes / targetLength) * 100, 1)

        etr = ((timeTaken / numPrimes) * targetLength) - timeTaken

        print(str(percentDone) + "%% done. Genenerated " + str(numPrimes) + "/" + str(targetLength)+ " primes. "
        "Estimated time remaining: " + formatTime(etr) + ".")

    input += 1

print("100%% done. Genenerated " + str(numPrimes) + " primes. " +
      "The " + str(numPrimes) + "th prime is: " + str(input) +
      ". Process took: " + formatTime(etr) + ".")