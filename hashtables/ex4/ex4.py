def has_negatives(a):
    result = []
    d = {}

    positives = [v for v in a if v >= 0]
    negatives = [v for v in a if v < 0]

    for val in positives:
        d[val] = False

    for val in negatives:
        if val * -1 in d:
            d[val * -1] = True

    result = [v[0] for v in d.items() if v[1] == True]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
