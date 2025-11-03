
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
        
        primes.append(input)
        numPrimes += 1
        
    
    if (numPrimes % interval == 0) & (numPrimes != targetLength) & (primes[numPrimes - 1] == input):
        
        timeTaken = time.time() - startTime

        interval = random.randint(9000, 11000)

        percentDone = (numPrimes / targetLength)

        estimatedTimeRemaining = ((timeTaken / numPrimes) * targetLength) - timeTaken

        print(str(format(percentDone, ".1%")) + " done. Genenerated " + str(numPrimes) + "/" + str(targetLength)+ " primes. "
        "Estimated time remaining: " + formatTime(estimatedTimeRemaining) + ".")

    input += 1

print(f"{1:.1%}" + " done. Genenerated " + str(numPrimes) + " primes. " +
      "The " + str(numPrimes) + "th prime is: " + str(primes[numPrimes - 1]) +
      ". Process took: " + formatTime(timeTaken) + ".")