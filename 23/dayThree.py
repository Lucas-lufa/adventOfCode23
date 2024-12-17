
textFile = 'dayThree.md'

width = 141
length = 140

symbols = ['&', '+', '/', '-', '=', '@','%', '#', '$', '*']
number = ""
numberLength = 0
sum = 0

def isSymbolAdjacent(list:list,symbols:list):
    """ """
    for char in list:
        if char in symbols:
            return True

def keepIn(index:int,width:int):
    width -= 1
    if index > 0 and index <= width:
        return 1
    else:
        return 0
    
def notTooShort(int:int):
    """If length is too short return zero"""
    if int == 1:
        return 0
    else:
        return int

def SymbolsMiddleTopBottom(lineNumber,numberEnd,number,width,length,symbols,textFile):
    """Looks for symbols adjacent to number"""
    numberLength = len(number)
    paddingBeginning = keepIn(numberEnd - numberLength, width)
    paddingEnd = keepIn(numberEnd,width)
    lookBeginning = numberEnd - notTooShort(numberLength) - paddingBeginning
    readRange = numberLength + paddingBeginning + paddingEnd
    
    with open(textFile, 'r') as file:
        file.seek((lineNumber * width) + lookBeginning)
        _ = file.read(readRange)
        if isSymbolAdjacent(_,symbols):
            return True
        if lineNumber > 0:
            file.seek((lineNumber * width - width) + lookBeginning)
            _ = file.read(readRange)
            if isSymbolAdjacent(_,symbols):
                return True
        if lineNumber < (length - 1):
            file.seek((lineNumber * width + width) + lookBeginning)
            _ = file.read(readRange)            
            if isSymbolAdjacent(_,symbols):
                return True
        return False
        
def numberMiddleTopBottom(gear,gearIndex,lineNumber,width,length,textFile):
    """ """
    lookForLength = len(gear)
    paddingBeginning = keepIn(gearIndex - 1, width)
    paddingEnd = keepIn(gearIndex,width)
    lookBeginning = gearIndex - notTooShort(1) - paddingBeginning
    readRange = 1 + paddingBeginning + paddingEnd

    with open(textFile, 'r') as file:
        numberPlace = []
        #theRange = 0
        place = (lineNumber * width) + lookBeginning
        numberLength = 0
        for i in range(readRange):
            file.seek(place + i)
            _ = file.read(1)           
            if _.isdigit():
                while _.isdigit(): # to find the beginning of the number
                    place = file.tell()
                    file.seek(place - 1)
                    _ = file.read(1)

                place += 1
                file.seek(place)
                _ = file.read(1)
                while _.isdigit():
                    numberLength += 1
                    file.seek(place + numberLength)

                numberPlace.append(tuple(file.read(numberLength),place))

            if lineNumber > 0:
                place = file.seek((lineNumber * width - width) + lookBeginning)
                _ = file.read(1)           
                if _.isdigit():
                    while _.isdigit(): # to find the beginning of the number
                        place -= 1
                        file.seek(place)
                        _ = file.read(1)

                    place += 1
                    file.seek(place)
                    _ = file.read(1)
                    while _.isdigit():
                        numberLength += 1
                        file.seek(place + numberLength)
                        _ = file.read(1)


                    numberPlace.append(tuple([file.read(numberLength),place]))

            if lineNumber < (length - 1):
                place = file.seek((lineNumber * width + width) + lookBeginning)
                _ = file.read(1)           
                if _.isdigit():
                    while _.isdigit(): # to find the beginning of the number
                        place = file.tell()
                        file.seek(place - 1)
                        _ = file.read(1)

                    place += 1
                    file.seek(place)
                    _ = file.read(1)
                    while _.isdigit():
                        numberLength += 1
                        file.seek(place + numberLength)

                    numberPlace.append(tuple(file.read(numberLength),place))
    
        numberPlace




def dayThree():
    sum = int
    with open(textFile, 'r') as file:   
        for lineNumber, line in enumerate(file):
            for characterIndex, character in enumerate(line):
                if character.isdigit():
                    number += character
                    continue
                numberLength = len(number)
                if numberLength > 0:
                    if SymbolsMiddleTopBottom(lineNumber,characterIndex,number,width,length,symbols,textFile):
                        sum += int(number)                    
                    number = ""
                    numberLength = 0
    print(sum)

def dayThree_part_two(textFile):
    """Looks for star and two numbers that collide"""
    gear = '*'
    sum = int
    with open(textFile, 'r') as file:   
        for lineNumber, line in enumerate(file):
            for characterIndex, character in enumerate(line):
                if character == gear:
                    numberMiddleTopBottom(gear,characterIndex,lineNumber,width,length,textFile)


def main():
    """ """
    with open(textFile, 'r') as file:
        width = len(file.readline())
        length = len(file.readlines())

        dayThree_part_two(textFile)
    
    
if __name__ == '__main__':
    main()