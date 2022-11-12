counter = 0
summ = 0
while True:
    choice = input("do you want to add a number(y/n)")
    if choice == 'y':
        counter += 1  # counter = counter + 1
        summ += int(input("input new number"))
    else:
        print('mean =', summ / counter)
        break
