def collatz(number):
    if number % 2 == 0:
        val = (number // 2)
        return int(val)

    else:
        val = ((number * 3) + 1)
        return int(val)


print("Enter number: ")

while True:
    try:
        userInput = int(input())
        collatz(userInput)
        print(collatz(userInput))
        if collatz(userInput) != 1:
            continue
        else:
            break
    except ValueError:
        print('Error: Invalid Argument. Please enter an integer.')
