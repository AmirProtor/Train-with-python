from time import sleep
from os import system

train = '''
                          """""""""
                           |     |
                           |     |              """"""""""
    .|----------------------------------         |     ||
    .|                                  =        |     ||
    .|                                   =       /     ||----
    .|                                    =     /       |    : ''
    .|                                     =====              ""':
    .|                                                        ""':
    .|       '  '           '  '                  '  '       : ''
    .|     '      '       '      '              '      '    /
    .|_____'      '_______'      '______________'      '___|
             '  '           '  '                  '  '
 '''

slicedTrain = train.splitlines()

input("Press ENTER to start!")

while True:
    for i in slicedTrain:
        print(i)

    for j in range(len(slicedTrain)):
        slicedTrain[j] = " " + slicedTrain[j]

    sleep(0.05)
    system('cls')
