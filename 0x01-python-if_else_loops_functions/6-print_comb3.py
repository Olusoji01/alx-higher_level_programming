#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if (i < 9) and (j < 10):
            print("{}{}, ".format(i, j), end='')
        if (i == 8) and (j == 9):
            print("{}{}".format(i, j))
       # print()  # Print a newline after each inner loop iteration
