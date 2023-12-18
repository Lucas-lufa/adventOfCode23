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


def main():
    """ """
    dayTwo()
if __name__ == '__main__':
    main()