def setOperation(seta, setb):
    # Write your code here
    seta = set(seta)
    setb = set(setb)
    union = seta.union(setb)
    intersection = seta.intersection(setb)
    diff1 = seta.difference(setb)
    diff2 = setb.difference(seta)
    symdiff = seta.symmetric_difference(setb)
    frozenseta = frozenset(seta)
    return(union, intersection, diff1, diff2, symdiff, frozenseta )


if __name__ == '__main__':
    seta_count = int(input().strip())

    seta = []

    for _ in range(seta_count):
        seta_item = input()
        seta.append(seta_item)

    setb_count = int(input().strip())

    setb = []

    for _ in range(setb_count):
        setb_item = input()
        setb.append(setb_item)

    un, intersec, diffa, diffb, sydiff, frset = setOperation(seta, setb)
    print(sorted(un))
    print(sorted(intersec))
    print(sorted(diffa))
    print(sorted(diffb))
    print(sorted(sydiff))
    print("Returned value is {1} frozenset".format(frset, "a" if type(frset) == frozenset else "not a"))