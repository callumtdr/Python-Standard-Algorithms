numbersToCheck = [54, 32, 56, 83, 12, 53, 62, 18, 22, 54, 75]


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
            return x
    return -1

def bubbleSort(numberstoCheck):
    n = len(numbersToCheck)

    for x in range(n):
        for i in range(n-x-1):
            if numbersToCheck[i] > numbersToCheck[i+1]:
                numbersToCheck[i], numbersToCheck[i+1] = numbersToCheck[i+1], numbersToCheck[i]
    return numbersToCheck

def validInput():

    userInput = ""
    try:
        userInput = int(input("Enter a number: "))
    except ValueError:
        print("Error: you did not eneter a number")
        validInput()
    print("That was a valid Number!")
    return userInput

print(numbersToCheck)
print("The minimum value in the list is: ",(getMinNum(numbersToCheck)))
print("The maximum value in the list is: ",(getMaxNum(numbersToCheck)))
print("The number of values below 50 in the list is: ",(countOccurence(numbersToCheck)))
print("The value of 12 can be found in at index: ",(linearSearch(numbersToCheck)))
print("The sorted values are: ",(bubbleSort(numbersToCheck)))
validInput()
