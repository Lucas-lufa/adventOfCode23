"""12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs"""
textFile = 'dayTwo.sql'

def findFirstNumber(line:str):
    """"""
    character = ''
    for _ in line:
        if _.isdigit():
            character +=_
            continue
        if character.isdigit():
            return int(character)

def dayTwo():
    count = 0
    with open(textFile, 'r') as file:
        for _,line in enumerate(file):
            game = line[7:]
            gameEnd = len(game) -1
            for index, character in enumerate(game):
                if character.isdigit():
                    cube = game[index:index+2]
                    if cube.isdigit():
                        colourCode = game[index+3]
                        if int(cube) > 14:
                            break

                        if int(cube) == 14 and colourCode != 'b':
                            break
                        
                        if int(cube) == 13:
                            if colourCode == 'r':
                                break

                if index == gameEnd :
                    count+= findFirstNumber(line)

    print(count)

def theMost(character,rgb,index):
    dice = int(character)
    if rgb[index] < dice:
        rgb[index] = dice
    return ''

def dayTwoPartTwo():
    """  """
    sumList = []
    with open(textFile, 'r') as file:
        for line in file:
            rgb = [0,0,0]
            character = ''
            for i in line:
                if i.isdigit():
                    character +=i
                    continue
                if character.isdigit():
                    match i:
                        case ':':
                            character = ''
                        case 'r':
                            index = 0
                            character = theMost(character,rgb,index)
                        case 'g':
                            index = 1
                            character = theMost(character,rgb,index)
                        case 'b':
                            index = 2
                            character = theMost(character,rgb,index)

            sumList.append(rgb[0]*rgb[1]*rgb[2])
    print(sum(sumList))
                

def main():
    """ """
    dayTwoPartTwo()
if __name__ == '__main__':
    main()