#Advent Day 01
#Part 01
with open("calibrationInput.txt", "r") as calibrationData:
    calibration = calibrationData.readlines()

lineNumbers = ''
calibrationTotal = 0

for line in calibration:
    lineNumbers = ''
    for value in line:
        if value.isdigit():
            lineNumbers += value
    calibrationTotal += int(lineNumbers[0] + lineNumbers[-1])

#print(calibrationTotal)

#Part 02
calibrationTotal = 0
numberSet = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberDict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0'}
stringSet = ''

for line in calibration:
    lineNumbers = ''
    stringSet = ''

    for value in line:
        if value.isdigit():
            lineNumbers += value
        else:
            stringSet += value
            for number in numberSet:
                if number in stringSet:
                    lineNumbers += (numberDict[number])
                    stringSet = ''
    
    print(lineNumbers)
    calibrationTotal += int(lineNumbers[0] + lineNumbers[-1])

#print(calibrationTotal)
    
#Line 22 might pose a problem :/