def check(lst):
    counter = -1
    for i in lst:
        counter += 1
        if i != '':
            if counter not in [1, 2, 5, 4, 6, 8, 9, 10, 12]:
                print counter, i
