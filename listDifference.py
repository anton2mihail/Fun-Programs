def difflist(lst) :
    newlist = []
    for i in range(0, len(lst)-1) :
        n = lst[i+1]
        m = lst[i]
        newlist.append(n-m)
    return newlist


def main():
    ze = [1, 4, 5, 7, 8, 9, 6, 4, 3, 5, 7, 8]
    newLI = difflist(ze)
    print([x for x in newLI])


main()