numbersToCheck = [54, 32, 56, 83, 12, 53, 62, 18, 22, 54, 75]

targetNum = 12

def getMinNum (numbersToCheck):

    minValue = numbersToCheck[0]

    for x in numbersToCheck:
        if x < minValue:
            minValue = x  
    return minValue
   
def getMaxNum(numbersToCheck):

    maxValue = numbersToCheck[0]

    for x in numbersToCheck:
        if x > maxValue:
            maxValue = x
    return maxValue

def countOccurence(numbersToCheck):

    count = 0

    for x in numbersToCheck:
        if x < 50:
            count = count +1
    return count

def linearSearch(numbersToCheck):

    targetNum = 12

    for x in range(len(numbersToCheck)):
        if numbersToCheck[x] == targetNum:
            return x +1
    return -1

def bubbleSort(numberstoCheck):
    n = len(numbersToCheck)

    for x in range(n):
        for i in range(n-x-1):
            if numbersToCheck[i] > numbersToCheck[i+1]:
                numbersToCheck[i], numbersToCheck[i+1] = numbersToCheck[i+1], numbersToCheck[i]
    return numbersToCheck


print(getMinNum(numbersToCheck))
print(getMaxNum(numbersToCheck))
print(countOccurence(numbersToCheck))
print(linearSearch(numbersToCheck))
print(numbersToCheck)
print(bubbleSort(numbersToCheck))