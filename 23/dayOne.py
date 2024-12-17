numberList = []
sum = 0
textFile = 'dayOne.md'

def dayOne():
    with open(textFile, 'r') as file:
        for line in file:
            for letter in line:
                if letter.isdigit():
                    a = letter
                    break
            for letter in reversed(line):                            
                if letter.isdigit():
                    b = letter
                    break

            c = a + b
            numberList.append(int(c))
            sum += int (c)
    print(sum)

def dayOnePartTwo(sum):
    """ sorted(
    [('abc', 121), ('abc', 231), ('abc', 148), ('abc', 221)], 
    key=lambda x: x[1]
) """
    firstAndLasts = []
    validDigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digitValues = {"1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    with open(textFile, "r") as file:
        for line in file:
            inLineDigits = []
            for digit in validDigits:
                index = line.find(digit)
                if ( index >= 0):
                    inLineDigits.append((digit,index))

                index = line.rfind(digit)
                if ( index >= 0):
                    inLineDigits.append((digit,index))
                    
            inLineDigits.sort(key=lambda x: x[1])                    
            c = digitValues[inLineDigits[0][0]] + digitValues[inLineDigits[-1][0]]            
            firstAndLasts.append(c)

    for digit in firstAndLasts:
        sum += int(digit)
    print(firstAndLasts)
    print(sum)    

print(numberList)


def main():
    dayOnePartTwo(sum)

if __name__ == '__main__':
    main()