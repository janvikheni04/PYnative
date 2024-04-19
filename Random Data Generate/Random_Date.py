#Generate a random date between given start and end dates
import random
import time

def randdate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randGen = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randGen * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ", randdate("1/1/2016", "12/12/2018"))