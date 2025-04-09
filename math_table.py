while True:
    n = int(input("Insert a whole number: "))
    print('-----------------')
    print(f"TABLE OF {n}")

    if n == 0:
        print("The results of the table of 0 are always equal to 0")
    else:
        i = 1

        while i <= 10:
            for c in range(n, n*10+n, n):
                print(f'{n} * {i} = {c}')
                i += 1
    print('-----------------')

