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

print(calibrationTotal)

#Part 02

for line in calibration:
    lineNumbers = ''
    if line 
    for value in line:
        if value.isdigit():
            lineNumbers += value
        elif 