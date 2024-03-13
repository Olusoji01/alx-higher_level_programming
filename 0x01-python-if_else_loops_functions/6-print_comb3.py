#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if (i < 9) and (j < 10):
            if (i == 0) and (j == 1):
                print("{}{}".format(i, j), end='')
            else:
                print(", {}{}".format(i, j), end='')
            if (i == 8) and (j == 9):
                print('')

