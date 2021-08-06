print("Swapping Files Data App")

def swapFileData():
    data_a = 1

    data_b = 2

    file1 = input("What's the name of your first file? ")
    file2 = input ("What's the name of your second file? ")



    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

    print("The data has been swapped! Check", file1, "and", file2)

swapFileData()

