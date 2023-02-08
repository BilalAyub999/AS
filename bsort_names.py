# sort the names in one dimensional array (names) of size 100 using bubble sort
def bsort_names():
    temp = ""
    swapped = False
    max = 10
    count = 0
    names = ["Ali", "Jawad", "Anas", "Bilal", "Arwa", "Affan", "Rohail", "Taimoor", "Faiq", "Taha"]
    print(f'list before sorting:\n{names}\n\n')
    while True:
        swapped = False
        for i in range(0, max - 1):
            count = count + 1
            if names[i] > names[i + 1]:
                temp = names[i]
                names[i] = names[i + 1]
                names[i + 1] = temp
                swapped = True
        max = max - 1   
        if not swapped:
            break
    print(f'list after sorting:\n{names}\n\ncompare count: {count}')

bsort_names()
