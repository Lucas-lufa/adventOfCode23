
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

def middleTopBottom(lineNumber,numberEnd,number,width,length,symbols,textFile):
    """Looks for symbols adjacent"""
    numberLength = len(number)
    paddingBeginning = keepIn(numberEnd - numberLength, width)
    paddingEnd = keepIn(numberEnd,width)
    numberBeginning = numberEnd - numberLength - paddingBeginning
    readRange = numberLength + paddingBeginning + paddingEnd
    
    with open(textFile, 'r') as file:
        file.seek((lineNumber * width) + numberBeginning)
        _ = file.read(readRange)
        if isSymbolAdjacent(_,symbols):
            return True
        if lineNumber > 0:
            file.seek((lineNumber * width - width) + numberBeginning)
            _ = file.read(readRange)
            if isSymbolAdjacent(_,symbols):
                return True
        if lineNumber < (length - 1):
            file.seek((lineNumber * width + width) + numberBeginning)
            _ = file.read(readRange)            
            if isSymbolAdjacent(_,symbols):
                return True
        return False
        
      

with open(textFile, 'r') as file:
    width = len(file.readline())
    length = len(file.readlines())

with open(textFile, 'r') as file:   
   for lineNumber, line in enumerate(file):
       for characterIndex, character in enumerate(line):
           if character.isdigit():
               number += character
               continue
           numberLength = len(number)
           if numberLength > 0:
               if middleTopBottom(lineNumber,characterIndex,number,width,length,symbols,textFile):
                   sum += int(number)
            #    print(len(line))
            #    print(line[characterIndex-numberLength-1:characterIndex+1] in symbols)
            #    file.seek(147)
            #    number = file.read(numberLength)
            #    print(number)
               number = ""
               numberLength = 0
print(sum)

            
def main():
    """ """
    
if __name__ == '__main__':
    main()