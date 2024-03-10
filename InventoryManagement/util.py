def capitalizeFirstLetter(value: str):
    capitalizedArr = []
    valueArr = value.split(" ")

    for word in valueArr:
        letterArr = []
        for index, letter in enumerate(word):
            if(index == 0):
                letterArr.append(letter.upper())
            else:
                letterArr.append(letter.lower())
        capitalizedArr.append("".join(letterArr))
    
    finalString = " ".join(capitalizedArr)
    return finalString