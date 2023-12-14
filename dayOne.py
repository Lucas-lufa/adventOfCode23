numberList = []
sum = 0

with open('dayOne.md', 'r') as file:
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
        

print(numberList)

print(sum)
