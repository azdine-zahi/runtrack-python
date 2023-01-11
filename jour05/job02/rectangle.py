def rectangle(width, height):
    print("|" + "- " * width + "|")

    i = 2
    while i < (height):
        print("|" + "  " * width + "|")
        i = i + 1

    print("|" + "- " * width + "|")


rectangle(10, 3)