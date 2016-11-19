for i in range(10):
    x = input("Enter your guess: ")
    if i == x:
        print("You win!")
        break
else:
    print("Truly incompetent!")
