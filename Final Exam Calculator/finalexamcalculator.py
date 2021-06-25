currentPercentage = input("What is your current percentage?: ")
convertedCurrentPecentage = float(currentPercentage)
print(convertedCurrentPecentage)

while True:
    finalExamPercentage = input("What final grade do you want?: ")

    if finalExamPercentage == "A":
        

    firstPart = convertedCurrentPecentage*(.8)
    secondPart = convertedFinalPecentage*(.2)

    print(firstPart + secondPart)


