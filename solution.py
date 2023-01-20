if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:  # check if n is even and in the range of 2 to 5 inclusive
        print("Not Weird")
    elif n >= 6 and n <= 20:  # check if n is even and in the range of 6 to 20 inclusive
        print("Weird")
    elif n > 20:  # check if n is even and greater than 20
        print("Not Weird")
