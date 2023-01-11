def tapis(n):
    print(" + " + "- " * n + " + ")
    i = 0
    while i <= n:
        print("|", end=" ")
        j = 0
        while j <= n:
            if i + j == n:
                print(" ", end=" ")
            else:
                print("#", end=" ")
            j += 1
        print("|")
        i += 1
    print(" + " + "- " * n + " + ")

tapis(10)